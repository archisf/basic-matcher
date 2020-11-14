import re

from django.http import JsonResponse
from rest_framework.views import APIView

from config.exceptions import BMBadRequest, BaseBMException
from .models import Candidate
from .serializers import CandidateSerializer
from .validator import CandidateFinderValidator


class CandidateFinderView(APIView):

    def get_queryset(self, params):
        pattern = None
        if 'title' not in params or 'skill' not in params:
            raise BMBadRequest
        qs = Candidate.objects.all()
        if 'title' in params and 'skill' in params:
            pattern = re.compile("|".join(params['title'].split(" ")))
        result = []
        for candidate in qs:
            number_of_matches = len(pattern.findall(candidate.title.lower()))
            if number_of_matches:
                if int(params['skill']) in [skill['id'] for skill in candidate.skill.values('id')]:
                    number_of_matches += 1
                candidate.order_weight = number_of_matches
                result.append(candidate)
        return result

    def get(self, request, *args, **kwargs):
        validator = CandidateFinderValidator(data=request.query_params)
        if not validator.is_valid():
            raise BMBadRequest(validator.errors)
        data = self.get_queryset(request.query_params)
        if data:
            serializer = CandidateSerializer(data, many=True)
            return JsonResponse(serializer.data, safe=False)
        raise BaseBMException
