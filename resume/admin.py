from django.contrib import admin
from .models import *

admin.site.register([
    SocialMedia,
])


@admin.register(Skill)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
