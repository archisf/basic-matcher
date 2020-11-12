
from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'skill_name', 'create_at')

    def skill_name(self, obj):
        return obj.skill.name

    skill_name.admin_order_field = 'skill_name'


admin.site.register(Job, JobAdmin)

