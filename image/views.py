from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from image.serializers import DownloadImageSerializer


class DownloadImage(APIView):
    def post(self, request):
        serializer = DownloadImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
