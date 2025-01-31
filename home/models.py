# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Club(models.Model):

    #__Club_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    #__Club_FIELDS__END

    class Meta:
        verbose_name        = _("Club")
        verbose_name_plural = _("Club")


class Player(models.Model):

    #__Player_FIELDS__
    preferred foot = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Clubhistory(models.Model):

    #__Clubhistory_FIELDS__
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Clubhistory_FIELDS__END

    class Meta:
        verbose_name        = _("Clubhistory")
        verbose_name_plural = _("Clubhistory")


class Match(models.Model):

    #__Match_FIELDS__
    home team = models.ForeignKey(Club, on_delete=models.CASCADE)
    away team = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    video = models.CharField(max_length=255, null=True, blank=True)
    home score = models.IntegerField(null=True, blank=True)
    away score = models.IntegerField(null=True, blank=True)

    #__Match_FIELDS__END

    class Meta:
        verbose_name        = _("Match")
        verbose_name_plural = _("Match")


class Performance(models.Model):

    #__Performance_FIELDS__
    non penalty goal = models.IntegerField(null=True, blank=True)
    shots total = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    shots creating actions = models.IntegerField(null=True, blank=True)
    passes attempted = models.IntegerField(null=True, blank=True)
    passes completed = models.IntegerField(null=True, blank=True)
    tackles = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    clearances = models.IntegerField(null=True, blank=True)
    aerials won = models.IntegerField(null=True, blank=True)
    performer = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    #__Performance_FIELDS__END

    class Meta:
        verbose_name        = _("Performance")
        verbose_name_plural = _("Performance")


class Scout(models.Model):

    #__Scout_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    experience = models.IntegerField(null=True, blank=True)

    #__Scout_FIELDS__END

    class Meta:
        verbose_name        = _("Scout")
        verbose_name_plural = _("Scout")


class Playermatchinsight(models.Model):

    #__Playermatchinsight_FIELDS__
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    scout = models.ForeignKey(Scout, on_delete=models.CASCADE)
    technical skill = models.IntegerField(null=True, blank=True)
    game sense / awareness = models.IntegerField(null=True, blank=True)
    ball control = models.IntegerField(null=True, blank=True)
    sprinting speed = models.IntegerField(null=True, blank=True)
    handling speed = models.IntegerField(null=True, blank=True)

    #__Playermatchinsight_FIELDS__END

    class Meta:
        verbose_name        = _("Playermatchinsight")
        verbose_name_plural = _("Playermatchinsight")



#__MODELS__END
