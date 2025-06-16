from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

class TareaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
