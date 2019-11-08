# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from book.forms import UserForm, ProfessionalsForm, RecruitersForm, GPForm, HDForm,OHForm, SpecialtiesForm, SpecialistForm, MyForm, BookFormset
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View
from book.models import User, Professionals, Recruiters, Specialties, Specialists, Post, Book, Date

def index(request):
	return render(request, 'book/form.html')

class UserRegistration(View):
	userform = UserForm
	professionalsform = ProfessionalsForm
	recruitersform = RecruitersForm
	ohform = OHForm
	hdform = HDForm
	specialtiesform = SpecialtiesForm
	specialistform = SpecialistForm

	# display blank form
	def get(self, request):
		userform = self.userform(None)
		professionalsform = self.professionalsform(None)
		recruitersform = self.recruitersform(None)
		ohform = self.ohform(None)
		hdform = self.hdform(None)
		specialtiesform = self.specialtiesform(None)
		specialistform = self.specialistform(None)
		return render(request, 'book/form2.html', {'userform': userform, 'professionalsform': professionalsform, 'recruitersform': recruitersform, 'hdform': hdform, 'ohform': ohform,'specialtiesform': specialtiesform, 'specialistform': specialistform})

	# process form data
	def post(self, request):
		userform = self.userform(request.POST) 
		professionalsform = self.professionalsform(request.POST)
		recruitersform = self.recruitersform(request.POST)
		hdform = self.hdform(request.POST)
		ohform = self.ohform(request.POST)
		specialtiesform = self.specialtiesform(request.POST)
		specialistform = self.specialistform(request.POST)
		
		# validate
		user_valid = userform.is_valid()
		professional_valid = professionalsform.is_valid()
		recruiter_valid = recruitersform.is_valid()
		hd_valid = hdform.is_valid()
		oh_valid = ohform.is_valid()
		specialty_valid = specialtiesform.is_valid()
		specialist_valid = specialistform.is_valid()

		if user_valid:
			user = userform.save(commit=False)
			password = userform.cleaned_data['password']
			user.set_password(password)
			user.save()

			if professional_valid:
				professional = professionalsform.save(commit=False)
				professional.cancellations = 0
				professional.bookings = 0
				professional.professional_user_id = user
				professional.save()
	
				if hd_valid is not None and user.profession == "Doctor":
					hd = hdform.save(commit=False)
					hd.hd_license_number = professional
					hd.save()
				
				if oh_valid is not None and user.profession == "Doctor":
					oh = ohform.save(commit=False)
					oh.oh_license_number = professional
					oh.save()

				if specialty_valid:
					specialty = specialtiesform.save(commit=False)
					specialty.save()

					if specialist_valid:
						specialist = specialistform.save(commit=False)
						specialist.license_number = professional
						specialist.specialty = specialty
						specialist.save()
				
			if recruiter_valid:
				recruiter = recruitersform.save(commit=False)
				recruiter.recruiter_user_id = user
				recruiter.save()

		return render(request, 'book/form2.html', {'userform': userform, 'professionalsform': professionalsform, 'recruitersform': recruitersform, 'hdform': hdform, 'ohform': ohform,'specialtiesform': specialtiesform, 'specialistform': specialistform})

def post(request, method="POST"):
	# LATEST ALGORITHM
	if request.method == "POST":

		post_data = request.POST.dict()
		# post details
		new_post = Post.save(commit=False)
		new_post.what = post_data.get("what")
		new_post.where = post_data.get("where")
		new_post.profession = post_data.get("where")
		new_post.setting = post_data.get("setting")
		new_post.incentives = post_data.get("incentives", None)
		new_post.incentives_date = post_data.get("incentives_date", None)
		new_post.salary_date = post_data.get("salary_date")
		new_post.requirements = post_data.get("requirements", None)
		new_post.patients_number = post_data.get("patients_number")
		new_post.person_to_look_for = post_data.get("person_to_look_for")
		new_post.others = post_data.get("others", None)
		new_post.save()
		# determine if it's for several vs similar professionals or similar 
		type_of_post = post_data.get("post_type")
		# if for different professionals
		if type_of_post == "different_professionals":
			# get NUMBER OF POSTS
			number_of_posts = post_data.get("number_of_posts")
			# iterate thru number of posts
			for i in number_of_posts + 1, i++ {
			#access post details by indexing
				post_details = Date.save(commit=False)
				post_details.post = new_post
				post_details.start_date = post_data.get("start_date")[i]
				post_details.end_date = post_data.get("end_date")[i]
				post_details.start_time = post_data.get("start_time")[i]
				post_details.end_time = post_data.get("end_time")[i]
				post_details.total_hours = post_data.get("total_hours")[i]
				post_details.net_rate = post_data.get("net_salary")[i]

				# total number of posts
				total_posts = post_data.get("total_posts")[i]
				# determine if it's AND or OR
				determinant = post_data.get("determinant")[i]
				# get the no. of males needed
				male = post_data.get("male")[i]
				# get the no. of females needed
				female = post_data.get("female")[i]

				if total_posts != 0;
				# if AND
					if determinant == "AND";
						
						if male != 0;

							post_details.sex_of_professional = "Male"
							post_details.is_taken = False
							post_details.save()

							for i = 1; i < male; i++
								#create post
								post_details.pk = None
								post_details.sex_of_professional = "Male"
								post_details.is_taken = False
								post_details.save()

								#redirect to the posts page
							# use for loop to iterate thru female
							for i = 1; i < female; i++
								#create post
								post_details.pk = None
								post_details.sex_of_professional = "Female"
								post_details.is_taken = False
								post_details.save()

						else if female != 0;

							post_details.sex_of_professional = "Female"
							post_details.is_taken = False
							post_details.save()

							for i = 1; i < female; i++
								#create post
								post_details.pk = None
								post_details.sex_of_professional = "Female"
								post_details.is_taken = False
								post_details.save()

						#if 0 male and 0 female
						else
							#return error message
							return render(request, 'book/post2.html')


					# else if OR
					else if determinant == "OR";
					# CREATE AN INITIAL POST FIRST TO BE COPIED LATER


						post_details.sex_of_professional = "Male"
						post_details.is_taken = False
						post_details.save()

						post_details.pk = None
						post_details.sex_of_professional = "Female"
						post_details.is_taken = False
						post_details.save()
					
					# use for loop to iterate thru male ONLY
						for i = 1; i < total_posts; i++
							#create post
							post_details.pk = None
							post_details.sex_of_professional = "Male"
							post_details.is_taken = False
							post_details.save()

							post_details.pk = None
							post_details.sex_of_professional = "Female"
							post_details.is_taken = False
							post_details.save()
			}

		# else for same professionals 
		else if type_of_post == "same_professionals":
			number_of_posts = post_data.get("number_of_posts")

			determinant = post_data.get("determinant")
			# get the no. of males needed
			male = post_data.get("male")
			# get the no. of females needed
			female = post_data.get("female")
			# iterate thru number of posts
			for i = 1; i < number_of_posts + 1; i++:
				#access post details by indexing
			# iterate thru number of posts
				#access post details by indexing
					post_details = Date.save(commit=False)
					post_details.post = new_post
					post_details.start_date = post_data.get("start_date")[i]
					post_details.end_date = post_data.get("end_date")[i]
					post_details.start_time = post_data.get("start_time")[i]
					post_details.end_time = post_data.get("end_time")[i]
					post_details.total_hours = post_data.get("total_hours")[i]
					post_details.net_rate = post_data.get("net_salary")[i]

			
					# determine if it's AND or OR
					determinant = post_data.get()
					# get the no. of males needed
					male = post_data.get("male")
					# get the no. of females needed
					female = post_data.get("female")

					# if AND
						if determinant == "AND";
							
							if male != 0;

								post_details.sex_of_professional = "Male"
								post_details.is_taken = False
								post_details.save()

								for i = 1; i < male; i++
									#create post
									post_details.pk = None
									post_details.sex_of_professional = "Male"
									post_details.is_taken = False
									post_details.save()

							else if female != 0;

								post_details.sex_of_professional = "Female"
								post_details.is_taken = False
								post_details.save()

								for i = 1; i < female; i++
									#create post
									post_details.pk = None
									post_details.sex_of_professional = "Female"
									post_details.is_taken = False
									post_details.save()

							#if 0 male and 0 female
							else

								#return error message

						else if determinant == "OR";
						# CREATE AN INITIAL POST FIRST TO BE COPIED LATER

							if male != 0;
								post_details.sex_of_professional = "Male"
								post_details.is_taken = False
								post_details.save()

								post_details.pk = None
								post_details.sex_of_professional = "Female"
								post_details.is_taken = False
								post_details.save()
						
						# use for loop to iterate thru male ONLY
								for i = 1; i < male; i++
									#create post
									post_details.pk = None
									post_details.sex_of_professional = "Male"
									post_details.is_taken = False
									post_details.save()

									post_details.pk = None
									post_details.sex_of_professional = "Female"
									post_details.is_taken = False
									post_details.save()

	
	else 
		return

	# if request.method is post, accept each the entries
	if request.method == "POST":
		what = request.POST.get['what']


		def login_view(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user_type = login_data.get("user_type")
        print(user_type, username, password)
        return HttpResponse("This is a post request")
    else:
        return render(request, "base.html")
	

def load_post(request, method="POST"):
	# get the word from where textbox on keydown
	if request.method == "POST":
		if request.POST.get('request') == 1:
	        	term = request.POST.get('search')
	        posts = Post.objects.filter(string__contains=term)
	        results = []
	        for r in posts:
	        	row_result = []
	        	row_result["value"] = r.post_id
	        	row_result["label"] = r.where
	        	results.append(row_result)

	        data = json.dumps(results)
	        exit()

		elif (request.POST.get('request') == 2):
			userid = request.POST.get('userid')
			post_details = Post.objects.filter(id=userid)
			user_array = []

			for q in post_details:
			 	user_id = q['post_id']
			 	profession = q['profession']
			 	qualification = q['qualification']
				pay_given = q['pay_given']
				incentives = q['incentives']
				incentives_given = q['incentives_given']
				requirements = q['requirements']
				expected_number_patients = q['expected_number_patients']
				toxicity = q['toxicity']
				person_to_look_for = q['person_to_look_for']
				
				user_array[] = ["user_id": user_id, "profession": profession, "qualification": qualification, "pay_given": pay_given, "incentives": incentives, "incentives_given": incentives_given, "requirements": requirements, "expected_number_patients": expected_number_patients, "toxicity": toxicity, "person_to_look_for": person_to_look_for]

			data = json.dumps(user_array)
	        exit()

	else:
        data = 'fail'
   		mimetype = 'application/json'
   
    return HttpResponse(data, mimetype)
