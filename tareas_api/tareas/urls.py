from django.urls import path
from .views import TareaListCreateAPIView

urlpatterns = [
    path('', TareaListCreateAPIView.as_view(), name='tarea-list-create'),
]
