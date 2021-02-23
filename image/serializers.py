from rest_framework import serializers
from image.models import Image


class DownloadImageSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Image
        fields = ('created', 'image', 'owner')
