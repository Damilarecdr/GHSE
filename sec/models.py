
from django.db import models
from django.core.validators import FileExtensionValidator

class Slide(models.Model):
    caption = models.CharField(max_length=200)
    #description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/slides/', blank=True, null=True) 
    #button_text = models.CharField(max_length=100, blank=True, null=True)
    #button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.caption
class Update(models.Model):
    news = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.news


class Whyu(models.Model):
    heading = models.CharField(max_length=30)

    def __str__(self):
        return self.heading

class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    t_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/teachers/images/', blank=True, null=True) 
    def __str__(self):
        return self.full_name

class School_Info(models.Model):
    logo =  models.ImageField(upload_to='uploads/logo/images/', blank=True, null=True) 
    #img2 =  models.ImageField(upload_to='uploads/logo/images/', blank=True, null=True) 
    school_name = models.CharField(max_length=50)
    ab = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    facebook =  models.URLField(blank=True, null=True)
    youtube =  models.URLField(blank=True, null=True)
    instagram =  models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length= 12)
    working_hours = models.CharField(max_length=50)
    f_logo = models.ImageField(upload_to='uploads/logo/images/', blank=True, null=True) 

    def __str__(self):
        return self.school_name

class Welcome(models.Model):
    name= models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/teachers/images/', blank=True, null=True) 
    message = models.TextField()
    signature= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name





# students/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Student(AbstractUser):
    student_id = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()

    # Adding unique related_names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name='student_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='student_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
