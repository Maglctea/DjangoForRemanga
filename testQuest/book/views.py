from builtins import min
from django.db.models import F
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render, _get_queryset, get_list_or_404
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Title, Tag, Chapter, Volume
from .serializers import TitleSerializer, ChapterListSerializer, ChapterRetrieveSerializer, VolumeSerializer


# class TitleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
#     queryset = Title.objects.all()
#     serializer_class = TitleSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Title.objects.all()
#         return Title.objects.filter(pk=pk)

class TitleViewPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class ChapterViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None, vol=None, num=None):
        title = get_object_or_404(Title, pk=pk)
        volume = get_object_or_404(Volume, number=vol, title_id=title.id)
        chapter = get_object_or_404(Chapter, volume_id=volume, number=num)
        Chapter.objects.filter(pk=chapter.pk).update(views_counter=F('views_counter')+1)
        return Response(ChapterRetrieveSerializer(chapter).data)

    def update(self, request, pk=None, vol=None, num=None):
        # chapter = Chapter.objects.filter(volume_id=Volume.objects.filter(title_id=Title.objects.get(pk=pk).id, number=vol).first().number, number=num).first()
        # # Chapter.objects.filter(pk=chapter.pk).update(views_counter=F('views_counter') + 1)
        # Chapter.objects.filter(pk=chapter.pk).update(like_counter=F('like_counter') + 1)
        title = get_object_or_404(Title, pk=pk)
        volume = get_object_or_404(Volume, number=vol, title_id=title.id)
        chapter = get_object_or_404(Chapter, volume_id=volume, number=num)
        Chapter.objects.filter(pk=chapter.pk).update(like_counter=F('like_counter')+1)
        return Response({'status': 'success'})


class VolumeViewSet(viewsets.ViewSet):
    def list(self, request):
        volume = Volume.objects.all()
        return Response(TitleSerializer(volume, many=True).data)



class TitleViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TitleSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            queryset = Title.objects.all()
        else:
            queryset = Title.objects.filter(pk=pk)
        return queryset

    pagination_class = TitleViewPagination