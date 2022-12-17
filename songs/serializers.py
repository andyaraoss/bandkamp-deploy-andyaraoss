from rest_framework import serializers
from .models import Song
import ipdb


class SongSerializer(serializers.ModelSerializer):
    album_id = serializers.SerializerMethodField()

    def get_album_id(self, obj: Song) -> str:
        return obj.album.id

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
        read_only_fields = ["album_id"]
