import os

from rest_framework.test import APITestCase
from rest_framework import status
from django.forms.models import model_to_dict

from users.models import User
from lms.models import Course, Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create(email='user_1@test.ru')
        self.course_1 = Course.objects.create(
            title="title_course_1",
            description="description_course_1",
            preview=os.path.join('lms', 'courses', 'previews', 'shutterstock.webp'),
            creator=self.user_1
        )
        self.lesson_1 = Lesson.objects.create(
            title="title_lesson_1",
            description="description_lesson_1",
            video_url="http://youtube.com/test_lesson.mp4",
            preview=os.path.join('lms', 'lessons', 'previews', 'shutterstock.webp'),
            course=self.course_1,
            creator=self.user_1
        )
        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user_1)

    def test_create_lesson(self):
        """ Тестирование создания урока """

        response = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )

        # Проверяем создание записи
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверяем содержимое созданной записи
        self.assertEqual(
            response.json(),
            {
                'id': response.json()['id'],
                'title': 'title_lesson_1',
                'description': 'description_lesson_1',
                'preview': response.json()['preview'],
                'video_url': 'http://youtube.com/test_lesson.mp4',
                'creator': self.user_1.pk,
                'course': response.json()['course']
            }
        )

        # Проверяем наличие записи в базе данных
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """ Тестирование вывода списка """

        response = self.client.get(
            '/lms/lesson/'
        )

        # Проверяем вывод списка записей
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем содержимое выводимой записи
        self.assertEqual(
            response.json(),
            {
                'count': response.json()['count'],
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': response.json()['results'][0]['id'],
                        'title': 'title_lesson_1',
                        'description': 'description_lesson_1',
                        'preview': response.json()['results'][0]['preview'],
                        'video_url': 'http://youtube.com/test_lesson.mp4',
                        'creator': self.user_1.pk,
                        'course': response.json()['results'][0]['course']
                    }
                ]
            }
        )

    def test_detail_lesson(self):
        """ Тестирование вывода урока """

        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )

        response_detail = self.client.get(
            f"/lms/lesson/{response_create.json()['id']}/"
        )

        # Проверяем вывод одной записи
        self.assertEqual(
            response_detail.status_code,
            status.HTTP_200_OK
        )

        # Проверяем содержимое выводимой записи
        self.assertEqual(
            response_detail.json(),
            {
                'id': response_detail.json()['id'],
                'title': 'title_lesson_1',
                'description': 'description_lesson_1',
                'preview': response_detail.json()['preview'],
                'video_url': 'http://youtube.com/test_lesson.mp4',
                'creator': self.user_1.pk,
                'course': response_detail.json()['course']
            }
        )

    def test_update_lesson(self):
        """ Тестирование редактирования урока """

        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )

        response_patch = self.client.patch(
            f"/lms/lesson/update/{response_create.json()['id']}/",
            {
                'title': 'title_lesson_1_patch',
                'description': 'description_lesson_1_patch',
                'video_url': 'http://youtube.com/test_lesson_1_patch.mp4'
            }
        )

        # Проверяем вывод одной записи
        self.assertEqual(
            response_patch.status_code,
            status.HTTP_200_OK
        )

        # Проверяем содержимое редактированной записи
        self.assertEqual(
            response_patch.json(),
            {
                'id': response_patch.json()['id'],
                'title': 'title_lesson_1_patch',
                'description': 'description_lesson_1_patch',
                'preview': response_patch.json()['preview'],
                'video_url': 'http://youtube.com/test_lesson_1_patch.mp4',
                'creator': self.user_1.pk,
                'course': response_patch.json()['course']
            }
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """

        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )

        response_delete = self.client.delete(
            f"/lms/lesson/delete/{response_create.json()['id']}/"
        )

        # Проверяем удаление
        self.assertEqual(
            response_delete.status_code,
            status.HTTP_204_NO_CONTENT
        )
