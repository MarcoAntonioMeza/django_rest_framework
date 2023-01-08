from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    """
    Para comprobar si esta autenticado se utiliza
    permission_classes = [permissions.IsAuthenticated]
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

