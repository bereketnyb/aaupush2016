from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Department(models.Model):
   name     = models.CharField(max_length=100)
   code     = models.CharField(max_length=5)

   def __str__(self):
      return self.name


class Lecturer(models.Model):
   user = models.ForeignKey(User)
   email = models.EmailField()
   name = models.CharField(max_length=100)
   course = models.ManyToManyField(Course)
   department = models.ForeignKey(Department)

   def __str__(self):
      #return self.name
      return self.user.first_name + ' ' + self.user.last_name

   def name(self):
      return self.user.first_name + ' ' + self.user.last_name

class Section(models.Model):
   name = models.CharField(max_length=100)
   year = models.IntegerField()     
   number = models.IntegerField()
   code = models.CharField(max_length=10)
   
   course = models.ManyToManyField(Course)
   department = models.ForeignKey(Department)

   def __str__(self):
      return self.name

class Announcement(models.Model):
   pub_date = models.DateTimeField('Date Published')
   exp_date = models.DateTimeField('Expiry Date')
   message  = models.TextField()
   
   lecturer = models.ForeignKey(Lecturer)
   section  = models.ManyToManyField(Section)

   def __str__(self):
      return 'By: ' + self.lecturer.user.first_name

def upload_path(instance, filename):
    return 'uploads/'+instance.folder.name+'/'+filename

class Material(models.Model):
   name        = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   file = models.FileField(upload_to=upload_path)
   pub_date = models.DateTimeField('Date Published')
       
   section     = models.ManyToManyField(Section)
   lecturer    = models.ForeignKey(Lecturer)
   course = models.ForeignKey(Course)

   def __str__(self):
      return self.name