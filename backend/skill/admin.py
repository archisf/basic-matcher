from django.contrib import admin
from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Skill, SkillAdmin)

