from django.contrib import admin
from Accounts.models.Profile import Profile
from django.contrib.auth.models import User

class ProfileInline(admin.TabularInline):
    model = Profile

class UserProfileAdmin(admin.ModelAdmin):
    model = User
    inlines = Profile

admin.site.register(Profile)