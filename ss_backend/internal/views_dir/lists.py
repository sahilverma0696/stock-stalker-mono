# views.py
from rest_framework import generics
from internal.models import Lists
from internal.serializers import ListsSerializer
#from rest_framework.permissions import IsAuthenticated

class ListsListCreateView(generics.ListCreateAPIView):
    queryset = Lists.objects.all()
    serializer_class = ListsSerializer
    #permission_classes = [IsAuthenticated]

class ListsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lists.objects.all()
    serializer_class = ListsSerializer
    #permission_classes = [IsAuthenticated]
