from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%d', null=True)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ItemBase(models.Model):
    subject = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item/%Y/%d')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject

    class Meta:
        abstract = True
        ordering = ["created_date"]

class Course(ItemBase):
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('category', 'subject')

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Lesson(ItemBase):
    content = RichTextField(null=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=CASCADE)
    tags = models.ManyToManyField(Tag, related_name='lessons', null=True)

    class Meta:
        unique_together = ('course', 'subject')

    
