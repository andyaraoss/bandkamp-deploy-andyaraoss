from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
import ipdb


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        album_id = self.kwargs["pk"]
        album_obj = get_object_or_404(Album, pk=album_id)

        songs = Song.objects.filter(album=album_obj)

        return songs

    def perform_create(self, serializer):
        album_id = self.kwargs["pk"]
        album_obj = get_object_or_404(Album, pk=album_id)

        serializer.save(album=album_obj)
