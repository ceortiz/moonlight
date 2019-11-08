from django.conf.urls import url
#from book.views import RegistrationWizard
from book.forms import UserForm, ProfessionalsForm, RecruitersForm, GPForm, SpecialtiesForm, SpecialistForm
from . import views

#registration_forms = [UserForm, ProfessionalsForm, RecruitersForm, GPForm, SpecialtiesForm, SpecialistForm,]
appname = 'book'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.UserRegistration.as_view(), name='registration'),
   	url(r'^post/$', views.post, name='post'),
   	url(r'^ajax/load-posts/$', views.load_posts, name='ajax_load_posts'),
]

