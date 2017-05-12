from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.
# MVC MODEL VIEW CONTROLLER

class images(models.Model):

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='pytesser' , blank=True)
    content = models.TextField()
    


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
