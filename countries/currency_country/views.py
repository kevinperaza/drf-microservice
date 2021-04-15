from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer


@api_view(["GET", "POST"])
def country(req):
    if req.method == "GET":
        return Response(CountrySerializer(Country.objects.all(), many=True).data)
    elif req.method == "POST":
        serializer = CountrySerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)