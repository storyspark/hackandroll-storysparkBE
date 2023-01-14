from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import *
from .models import Storyboard
from django_filters.rest_framework import DjangoFilterBackend

class StoryboardViewset(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    queryset = Storyboard.objects.all()
    serializer_class = StoryboardSerializer
    filterset_fields = ['author', 'tone']

    # def get_queryset(self):
    #     queryset = Storyboard.objects.all()
    #     author = self.request.query_params.get('author')
    #     print(author)
    #     if author is not None:
    #         queryset = queryset.filter(storyboard__author=author)
    #     return queryset

    def create(self, request, *args, **kwargs):
            serializer = StoryboardSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"invalid" : "data is invalid"}, status=400)