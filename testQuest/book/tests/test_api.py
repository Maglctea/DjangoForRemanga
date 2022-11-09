from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from book.models import Title, Volume, Chapter
from book.serializers import TitleSerializer, ChapterRetrieveSerializer


class BooksApiTestCase(APITestCase):
    def test_get_titles(self):
        title_1 = Title.objects.create(ru_name='Русское название',
                                       eng_name='Английское название',
                                       alt_name='Альтернативное название',
                                       description='Описание')
        title_2 = Title.objects.create(ru_name='Русское название 2',
                                       eng_name='Английское название 2',
                                       alt_name='Альтернативное название 2',
                                       description='Описание 2')

        url = reverse('title-list')
        response = self.client.get(url)
        serializer_data = TitleSerializer([title_1, title_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json().get('results'))

    def test_get_title(self):
        title = Title.objects.create(ru_name='Русское название',
                                     eng_name='Английское название',
                                     alt_name='Альтернативное название',
                                     description='Описание')

        url = reverse('title-list') + f'{title.pk}/'
        response = self.client.get(url)
        serializer_data = TitleSerializer(title).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_chapter(self):
        title = Title.objects.create(ru_name='Русское название',
                                     eng_name='Английское название',
                                     alt_name='Альтернативное название',
                                     description='Описание')

        volume = Volume.objects.create(title=title,
                                       name='Название тома',
                                       price=150,
                                       number=1)

        chapter = Chapter.objects.create(volume=volume,
                                         number=1,
                                         content='ТекстТекстТекстТекстТекстТекстТекстТекстТекстТекстТекстТекст',
                                         views_counter=0,
                                         like_counter=1)

        url = f'/api/v1/title={title.pk}/volume={volume.number}/chapter={chapter.number}/'
        response = self.client.get(url)
        serializer_data = ChapterRetrieveSerializer(chapter).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_like_chapter(self):
        title = Title.objects.create(ru_name='Русское название',
                                     eng_name='Английское название',
                                     alt_name='Альтернативное название',
                                     description='Описание')

        volume = Volume.objects.create(title=title,
                                       name='Название тома',
                                       price=150,
                                       number=1)

        chapter = Chapter.objects.create(volume=volume,
                                         number=1,
                                         content='ТекстТекстТекстТекстТекстТекстТекстТекстТекстТекстТекстТекст',
                                         views_counter=0,
                                         like_counter=1)

        url = f'/api/v1/title={title.pk}/volume={volume.number}/chapter={chapter.number}/like/'
        response = self.client.put(url)
        print(response.status_code)