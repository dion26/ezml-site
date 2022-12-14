from cgitb import lookup
from email.policy import default
from operator import truediv
from django.db import models, IntegrityError
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models import Q
from datetime import date
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.conf import settings
import random
import os
import re

class PlayerQuerySet(models.QuerySet):
    def search(self, query):
        lookup = Q(nickname__icontains=query) | Q(fullname__icontains=query) | Q(alternate_ids__icontains=query)
        qs = self.filter(lookup)
        return qs

class PlayerManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return PlayerQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query)

class Position(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=30)

class Player(models.Model):
    ROLE = (
        ('P', 'Player'),
        ('A', 'Analyst'),
        ('C', 'Coach'),
        ('S', 'Caster'),
    )
    STATUS = (
        ('A', 'Active'),
        ('R', 'Retired'),
        ('I', 'Inactive'),
        ('L', 'Loan'),
    )
    public_id = models.PositiveIntegerField(unique=True)
    nickname = models.CharField(max_length=60, unique=True)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE, default='P')
    slug = models.SlugField(null=True)
    image = models.ImageField(default="avatar.svg")
    image_url = models.URLField(blank=True, null=True)
    position = models.ManyToManyField(Position, related_name="players", blank=True)
    dob = models.DateField(null=True, blank=True)
    alternate_ids = models.CharField(null=True, blank=True, max_length=300)
    earning = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')

    objects = models.Manager()
    search_objects = PlayerManager()

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        if self.image_url:
            base_name = os.path.basename(self.image.url)
            base_file_name = os.path.basename(self.image_url)
            base_file_name = re.sub('[^a-zA-Z0-9_\.]', '', base_file_name)
            abs_url = f'{settings.MEDIA_ROOT}/player/{base_file_name}'
            if os.path.isfile(abs_url):
                os.remove(abs_url)
            if (base_name == 'avatar.svg' or base_name != base_file_name):
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(self.image_url).read())
                img_temp.flush()
                self.image.save(f"player/{base_file_name}", File(img_temp))
        while True:
            try:
                return super(Player, self).save(*args, **kwargs)
            except IntegrityError:
                r_num = random.randint(0, 100)
                self.slug = slugify(''.join(self.nickname, str(r_num)))
                return super(Player, self).save(*args, **kwargs)
    
    def get_remote_image(self):
        base_name = os.path.basename(self.image.url)
        base_file_name = os.path.basename(self.image_url)
        base_url = settings.MEDIA_ROOT
        if self.image_url and (base_name != 'avatar.svg' and base_name != base_file_name):
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image.save(f"{base_file_name}", File(img_temp))

    @property
    def get_age(self):
        today = date.today()
        try:
            birthday = self.dob.replace(year = today.year)

        # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = self.dob.replace(year = today.year,
                    month = self.dob.month + 1, day = 1)
    
        if birthday > today:
            return today.year - self.dob.year - 1
        else:
            return today.year - self.dob.year


class SocialMedia(models.Model):
    owner = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="social")
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    vk = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.owner.nickname + ' social media'


