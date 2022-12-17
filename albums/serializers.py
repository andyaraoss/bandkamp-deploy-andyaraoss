from rest_framework import serializers


from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj: Album) -> str:
        return obj.user.id

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
