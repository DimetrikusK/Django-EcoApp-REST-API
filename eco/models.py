from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, HttpResponseRedirect


class Profile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    coursename = models.TextField(db_column='courseNameID')
    isactive = models.IntegerField(db_column='isActive')
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fulldescription = models.TextField(db_column='fullDescription', blank=True, null=True)
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('eco:card', args=[str(self.id)])

    class Meta:
        managed = True
        db_table = 'Course'

    def __str__(self):
        return self.coursename


class Ecocard(models.Model):
    cardname = models.TextField(db_column='cardNameID')
    coursenameid = models.ForeignKey(Course, on_delete=models.CASCADE)
    isactive = models.IntegerField(db_column='isActive')
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fulldescription = models.TextField(db_column='fullDescription', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EcoCard'

    def __str__(self):
        return self.cardname


class Ecosoviet(models.Model):
    cardnameid = models.ForeignKey(Ecocard, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'EcoSoviet'

    def __str__(self):
        return self.title
