from email.policy import default
from operator import truediv
from django.db import models, IntegrityError
from django_countries.fields import CountryField
from django.utils.text import slugify
from datetime import date
import random

# Create your models here.

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
    nickname = models.CharField(max_length=60, unique=True)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE, default='P')
    slug = models.SlugField(null=True)
    image = models.ImageField(default="avatar.svg")
    position = models.ManyToManyField(Position, related_name="players", blank=True)
    dob = models.DateField(null=True, blank=True)
    alternate_ids = models.CharField(null=True, blank=True, max_length=300)
    earning = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='A')

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        while True:
            try:
                return super(Player, self).save(*args, **kwargs)
            except IntegrityError:
                r_num = random.randint(0, 100)
                self.slug = slugify(''.join(self.nickname, str(r_num)))
                return super(Player, self).save(*args, **kwargs)

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
    tiktok = models.URLField(blank=True, null=True)
    vk = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)


