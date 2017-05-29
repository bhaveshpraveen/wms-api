from django.shortcuts import render
from rest_framework import generics
from .serializer import ReadingSerializer
from .models import Reading
from rest_framework import permissions


class CreateView(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    # IsAuthenticated will deny permission to any unauthenticated user
    # IsAuthenticatedOrReadOnly which permits unauthenticated users
    # if the request is one of the "safe"  methods(GET, HEAD and OPTIONS)
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticated,)

