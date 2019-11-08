# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Post, User, Professionals, Recruiters, OH_professionals, HD_professionals, Specialties, Specialists


# Register your models here.
@admin.register(User)
class UserAdmin(DjangoUserAdmin):

	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name','middle_name', 'gender', 'birthday', 'address', 'phone_number', 'registration_date', 'profession')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	list_display = ('email', 'profession','last_name','first_name', 'middle_name','gender','is_staff')
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('email',)

admin.site.register(Post)
admin.site.register(Professionals)
admin.site.register(Recruiters)
admin.site.register(OH_professionals)
admin.site.register(HD_professionals)
admin.site.register(Specialties)
admin.site.register(Specialists)