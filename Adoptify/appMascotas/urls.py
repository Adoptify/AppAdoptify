from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('crear/', views.crear, name="crear"),
    path('<int:id>/', views.publicacion, name="publicacion"),
    path('filtrar', views.filtrarPublicacion, name="filtrar"),
    path('reportar/<int:pk>', views.reportar, name="reportar"),
]