import os

from rest_framework.test import APITestCase
from rest_framework import status
from django.forms.models import model_to_dict

from users.models import User
from lms.models import Course, Lesson, Subscription


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@test.ru')
        self.course = Course.objects.create(
            title="title_course",
            description="description_course",
            preview=os.path.join('lms', 'courses', 'previews', 'shutterstock_571762606.webp'),
            creator=self.user
        )
        self.lesson = Lesson.objects.create(
            title="title_lesson",
            description="description_lesson",
            video_url="http://youtube.com/test_lesson.mp4",
            preview=os.path.join('lms', 'lessons', 'previews', 'shutterstock_571762606.webp'),
            course=self.course,
            creator=self.user
        )
        self.subscription = Subscription.objects.create(
            subscriber=self.user,
            course=self.course
        )

        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """ Тестирование создания курса """

        response = self.client.post(
            '/lms/course/',
            data=model_to_dict(self.course)
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
                'id': 2,
                'lesson_count': 0,
                'lesson': [],
                'subscription': False,
                'title': 'title_course',
                'description': 'description_course',
                'preview': response.json()['preview'],
                'creator': self.user.pk
            }
        )

        # Проверяем наличие записи в базе данных
        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_list_course(self):
        """ Тестирование вывода списка """

        response = self.client.get(
            '/lms/course/'
        )

        # Проверяем вывод списка записей
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем содержимое выводимой записи
        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results':
                 [
                     {
                         'id': response.json()['results'][0]['id'],
                         'lesson_count': response.json()['results'][0]['lesson_count'],
                         'lesson': [
                             {
                                 'id': response.json()['results'][0]['lesson'][0]['id'],
                                 'title': 'title_lesson',
                                 'description': 'description_lesson',
                                 'preview': response.json()['results'][0]['lesson'][0]['preview'],
                                 'video_url': 'http://youtube.com/test_lesson.mp4',
                                 'creator': self.user.pk,
                                 'course': response.json()['results'][0]['lesson'][0]['course']
                             }
                         ],
                         'subscription': True,
                         'title': 'title_course',
                         'description': 'description_course',
                         'preview': response.json()['results'][0]['preview'],
                         'creator': self.user.pk
                     }
                 ]
             }
        )

    def test_detail_course(self):
        """ Тестирование вывода курса """

        response_create = self.client.post(
            '/lms/course/',
            data=model_to_dict(self.course)
        )

        response_detail = self.client.get(
            f"/lms/course/{response_create.json()['id']}/"
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
                'id': response_create.json()['id'],
                'lesson_count': response_detail.json()['lesson_count'],
                'lesson': [],
                'subscription': False,
                'title': 'title_course',
                'description':
                    'description_course',
                'preview': response_detail.json()['preview'],
                'creator': self.user.pk
            }
        )

    def test_update_course(self):
        """ Тестирование редактирования курса """

        response_create = self.client.post(
            '/lms/course/',
            data=model_to_dict(self.course)
        )

        response_patch = self.client.patch(
            f"/lms/course/{response_create.json()['id']}/",
            {
                'title': 'title_course_patch',
                'description': 'description_course_patch',
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
                'lesson_count': response_patch.json()['lesson_count'],
                'lesson': [],
                'subscription': False,
                'title': 'title_course_patch',
                'description': 'description_course_patch',
                'preview': response_patch.json()['preview'],
                'creator': self.user.pk
            }
        )

    def test_delete_course(self):
        """ Тестирование удаления курса """

        response_create = self.client.post(
            '/lms/course/',
            data=model_to_dict(self.course)
        )

        response_delete = self.client.delete(
            f"/lms/course/{response_create.json()['id']}/"
        )


        # Проверяем удаление
        self.assertEqual(
            response_delete.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_subscriber(self):
        """ Тестирование создания/удаления подписки """

        response = self.client.post(
            '/lms/subscription/',
            data={'course_id': self.course.pk}
        )

        # Проверяем создание записи
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем сообщение
        self.assertIn(
            response.json()['message'],
            ['подписка удалена', 'подписка добавлена']
        )
