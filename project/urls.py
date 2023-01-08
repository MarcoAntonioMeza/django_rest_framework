from rest_framework import routers
from .api import ProjectsViewSet


rutas = routers.DefaultRouter()

rutas.register('api/projects',ProjectsViewSet,'proyectos')

urlpatterns = rutas.urls

