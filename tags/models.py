from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagItems(models.Model):
    # What tag is applied to what object 
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Generic way of identifying an object. to do that
    # we need two pieces of information.
    # 1: The Type(Products, Video, Article etc) of the object we want to tag with -> Object type
    # 2: The ID of the object we want to tag -> record
    # Using these two pieces of information, we can identify an object in our application.
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

