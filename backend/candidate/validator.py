from rest_framework import serializers


class CandidateFinderValidator(serializers.Serializer):
    title = serializers.CharField(required=True)
    skill = serializers.IntegerField(required=True)
