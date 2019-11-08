
from django import forms

class BUserForm(forms.Form):
	MALE = 'M'
	FEMALE = 'F'
	SEX_CHOICES = (
		('', 'Choose..'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
	)
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
		('', 'Choose..'),
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
	last_name = forms.CharField(max_length=30)
	first_name = forms.CharField(max_length=30)
	middle_name = forms.CharField(max_length=30)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	gender = forms.ChoiceField(choices=SEX_CHOICES)
	birthday = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
	address = forms.CharField(max_length=30)
	phone_number = forms.CharField(initial='+63',max_length=13)
	profession = forms.ChoiceField(choices=PROFESSIONS_CHOICES)

class BProfessionalsForm(forms.Form):
	Reliever_Regular_Posts = 'BOTH'
	Reliever_Posts = 'RELI'
	Regular_Posts = 'REGU'
	POSTS_PREFERENCE = (
		('', 'Choose..'),
		(Reliever_Regular_Posts, 'Reliever & Regular Posts'),
		(Reliever_Posts, 'Reliever Posts'),
		(Regular_Posts, 'Regular Posts'),
	)
	#cv = forms.FileField()
	#prc_id = forms.FileField()
	license_number = forms.IntegerField()
	post_preference = forms.ChoiceField(choices=POSTS_PREFERENCE)

class BRecruitersForm(forms.Form):
	agency = forms.CharField(max_length=250)

class BGPForm(forms.Form):
	oh_certified = forms.BooleanField(required=False)
	hd_experience = forms.BooleanField()

class BSpecialtiesForm(forms.Form):
	Anaesthesiology = 'ANESTH'
	Dermatology = 'DERMA'
	Emergency_Medicine = 'ERMD'
	ENT = 'ENT'
	Family_Community = 'FCM'
	Internal_Medicine = 'IM'
	Obstetrics_GYN = 'OBGYN'
	Ophthalmology = 'OPHTHA'
	Orthopedics = 'ORTHO'
	Pathology = 'PATHO'
	Pediatrics = 'PEDIA'
	Primary_Care = 'PCP'
	Psychiatry = 'PSYCH'
	Radiology = 'RADIO'
	Rehabilitation_Medicine = 'REHAB'
	Surgery = 'SURG'
	SPECIALTIES = (
		('', 'Choose..'),
		(Anaesthesiology, 'Anaesthesiology'),
		(Dermatology, 'Dermatology'),
		(Emergency_Medicine, 'Emergency Medicine'),
		(ENT, 'ENT'),
		(Family_Community, 'Family & Community Medicine'),
		(Internal_Medicine, 'Internal Medicine'),
		(Obstetrics_GYN, 'Obstetrics & Gynecology'),
		(Ophthalmology, 'Ophthalmology'),
		(Orthopedics, 'Orthopedics'),
		(Pathology, 'Pathology'),
		(Pediatrics, 'Pediatrics'),
		(Primary_Care, 'Primary Care'),
		(Psychiatry, 'Psychiatry'),
		(Radiology, 'Radiology'),
		(Rehabilitation_Medicine, 'RehabilitationMedicine'),
		(Surgery, 'Surgery'),
	)
	specialty = forms.ChoiceField(choices=SPECIALTIES)

class BSpecialistForm(forms.Form):
	diplomate_status = forms.BooleanField()
	consultant_status = forms.BooleanField()
