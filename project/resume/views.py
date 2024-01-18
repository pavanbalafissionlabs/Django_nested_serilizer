
from .models import *
from .serializers import  *
from rest_framework import viewsets
from rest_framework.decorators import action



from django.db.models import Q

class ResumeViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing users
    """
    
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()

    def list(self, request, *args, **kwargs):
        """
        override the list method
        """
        self.include_only = self.request.query_params.get("include_only")
        return super().list(request, *args, **kwargs)

