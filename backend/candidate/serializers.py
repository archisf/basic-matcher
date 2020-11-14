from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    order_weight = serializers.IntegerField()

    class Meta:
        model = Candidate
        fields = ['id', 'title', 'skill', 'order_weight', 'get_skills']
