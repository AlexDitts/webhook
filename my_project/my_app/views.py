import os

from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.serializers import VarEnvSerializer, HookSerializer


class HookView(APIView):
    def get(self, request):
        serializer = HookSerializer()
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = HookSerializer(data)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(status=200, data=data)
            