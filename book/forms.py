from django.db import models
from django.forms import ModelForm, formset_factory
from django import forms
from django.contrib.auth.models import User
from book.models import User, Professionals, HD_professionals, OH_professionals, Recruiters, Specialties, Specialists, Post, Date

class UserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['last_name', 'first_name', 'middle_name', 'email', 'password', 'gender', 'birthday','address', 'phone_number', 'profession']

class ProfessionalsForm(ModelForm):
	class Meta:
		model = Professionals
		fields = ['license_number', 'preference']

class RecruitersForm(ModelForm):
	class Meta:
		model = Recruiters
		fields = ['agency']

class GPForm(forms.Form):
	oh_certified = forms.BooleanField(required=False)
	hd_experience = forms.BooleanField()

class HDForm(ModelForm):
	class Meta:
		model = HD_professionals
		fields = ['hd_experience']

class OHForm(ModelForm):
	class Meta:
		model = OH_professionals
		fields = ['oh_experience']
		
class SpecialtiesForm(ModelForm):
	class Meta:
		model = Specialties
		fields = ['specialty']

class SpecialistForm(ModelForm):
	class Meta:
		model = Specialists
		fields = ['diplomate_status', 'consultant_status']
		
class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['what', 'where', 'profession', 'setting', 'pay_given', 'incentives', 'incentives_given', 'requirements', 'expected_number_patients', 'person_to_relieve', 'recruiter', 'person_to_look_for', 'others']

class DateForm(ModelForm):
	class Meta:
		model = Date
		fields = ['start_date', 'end_date', 'start_time', 'end_time', 'total_hours', 'salary', 'net_rate', 'sex_of_professional', 'and_or'] 