from django.db import models
from django_countries.fields import CountryField
from django.utils.text import slugify
import random

# Create your models here.
class Player(models.Model):
    ROLE = (
        ('P', 'Player'),
        ('A', 'Analyst'),
        ('C', 'Coach'),
        ('S', 'Caster'),
    )
    nickname = models.CharField(max_length=60)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE, default='P')
    slug = models.SlugField(null=True)
    # team =
    # past teams =
    # Heros
    # Match history
    # links twitch/twitter/youtube
    # form history (hltv)
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

