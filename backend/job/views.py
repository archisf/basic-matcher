from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from backend.config.exceptions import BMNoContent
from .models import Job
from .serializer import JobSerializer


class JobListView(ListAPIView):

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        if jobs:
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
        raise BMNoContent
