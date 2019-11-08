# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.
class UserManager(BaseUserManager):

	user_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The given email must be set.')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
	"""User model"""

	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	objects = UserManager()
	
	Choose = ''
	MALE = 'M'
	FEMALE = 'F'
	SEX_CHOICES = (
		(Choose, ''),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
	)
	Choose = ''
	Allied_Medical_Professional = 'AMP'
	Dentist = 'DEN'
	Dietician = 'DIE'
	Doctor = 'DOC'
	Medical_Coder = 'COD'
	Medical_Technologist = 'MTC'
	Nurse = 'NUR'
	Pharmacist = 'PHA'
	Recruiter = 'REC'
	PROFESSIONS_CHOICES = (
		(Choose, ''),
        (Allied_Medical_Professional, 'Allied Medical Professional'),
        (Dentist, 'Dentist'),
        (Dietician,'Dietician'),
        (Doctor,'Doctor'),
        (Medical_Coder,'Medical Coder'),
        (Medical_Technologist,'Medical Technologist'),
        (Nurse,'Nurse'),
        (Pharmacist,'Pharmacist'),
        (Recruiter,'Recruiter'),
	)
	middle_name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1, choices=SEX_CHOICES, default=Choose)
	birthday = models.DateField(default=date.today, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	address = models.CharField(max_length=250)
	phone_number = models.CharField(max_length=13)
	registration_date = models.DateTimeField(default=datetime.now)
	profession = models.CharField(max_length=30, choices=PROFESSIONS_CHOICES, default=Choose)

class Professionals(models.Model):
	Choose = ''
	Reliever_Regular_Posts = 'BOTH'
	Reliever_Posts = 'RELI'
	Regular_Posts = 'REGU'
	POSTS_PREFERENCE = (
		(Choose, ''),
		(Reliever_Regular_Posts, 'Reliever & Regular Posts'),
		(Reliever_Posts, 'Reliever Posts'),
		(Regular_Posts, 'Regular Posts'),
	)
	license_number = models.IntegerField(primary_key=True)
	#cv = models.FileField()
	#prc_id = models.FileField()
	professional_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	cancellations = models.IntegerField(default=0)
	bookings = models.IntegerField(default=0)
	preference = models.CharField(max_length=4, choices=POSTS_PREFERENCE, default=Choose)

	def __str__(self):
		return str(self.professional_user_id.id) + ' ' + self.professional_user_id.last_name + ', ' + self.professional_user_id.first_name + ' - ' + self.professional_user_id.profession

class Recruiters(models.Model):
	agency = models.CharField(max_length=250)
	recruiter_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.recruiter_user_id) + ' ' + self.recruiter_user_id.last_name + ', ' + self.recruiter_user_id.first_name 

class OH_professionals(models.Model):
	oh_license_number = models.ForeignKey(Professionals, on_delete=models.CASCADE)
	oh_experience = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.oh_license_number.professional_user_id.id) + ' ' + self.oh_license_number.professional_user_id.last_name + ', ' + self.oh_license_number.professional_user_id.first_name 

class HD_professionals(models.Model):
	hd_license_number = models.ForeignKey(Professionals, on_delete=models.CASCADE)
	hd_experience = models.BooleanField(default=False)

	def __str__(self):
		return str(self.hd_license_number.professional_user_id.id) + ' ' + self.hd_license_number.professional_user_id.last_name + ', ' + self.hd_license_number.professional_user_id.first_name 

class Specialties(models.Model):
	specialty = models.CharField(max_length=70)

	def __str__(self):
		return self.specialty

class Specialists(models.Model):
	license_number = models.ForeignKey(Professionals, on_delete=models.CASCADE)
	diplomate_status = models.BooleanField(default=False)
	consultant_status = models.BooleanField(default=False)
	specialty = models.ForeignKey(Specialties, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.license_number) + ' - ' + self.specialty.specialty

class Post(models.Model):
	what = models.CharField(max_length=250)
	where = models.CharField(max_length=250)
	profession= models.CharField(max_length=250)
	setting = models.CharField(max_length=30)
	#qualification = models.CharField(max_length=250)
	pay_given = models.CharField(max_length=250)
	incentives = models.TextField()
	incentives_given = models.CharField(max_length=250)
	#oh_experience = models.BooleanField(default=False)
	#hd_experience = models.BooleanField(default=False)
	requirements = models.TextField()
	expected_number_patients = models.IntegerField()
	person_to_relieve = models.CharField(max_length=250)
	recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
	person_to_look_for = models.CharField(max_length=250)
	others = models.TextField()
	# transfer here the is_taken and sex of professionals attributes

	def get_absolute_url(self):
		return reverse('book:index')
	
	def __str__(self):
		return self.what + ' - ' + self.where

class Date(models.Model):
	OR = 'OR'
	AND = 'AND'
	OPTIONS = (
	(OR, 'OR'),
	(AND, 'AND')
	)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	start_date = models.DateField() # may be use durationfield instead
	end_date = models.DateField()
	start_time = models.TimeField() # may be use durationfield instead
	end_time = models.TimeField()
	total_hours = models.DecimalField(max_digits=4, decimal_places=2) #you might want to edit this
	salary = models.DecimalField(max_digits=8, decimal_places=2)
	net_rate = models.DecimalField(max_digits=8, decimal_places=2)
	sex_of_professional = models.CharField(max_length=6)
	#male_professionals_needed = models.IntegerField(default=0)
	and_or = models.CharField(max_length=3, choices=OPTIONS)
	#female_professionals_needed = models.IntegerField(default=0)
	is_taken = models.BooleanField(default=False)
	#taker = models.ForeignKey(Professionals, on_delete=models.CASCADE)

class Post_Reviews(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	toxicity = models.IntegerField()
	review = models.TextField(default="Type Here.")
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	#date_stamp = models.DateTimeField(auto_now=True)

class Taker(models.Model):
	date = models.ForeignKey(Date, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	taker = models.ForeignKey(Professionals, on_delete=models.CASCADE)





