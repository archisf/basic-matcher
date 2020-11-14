from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    skill_name = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Job
        fields = ['id', 'title', 'skill', 'skill_name']

    def get_skill_name(self, job_object):
        if job_object.skill:
            return job_object.skill.name
