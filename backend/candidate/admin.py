from django.contrib import admin

from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_skills', 'create_at')


admin.site.register(Candidate, CandidateAdmin)
