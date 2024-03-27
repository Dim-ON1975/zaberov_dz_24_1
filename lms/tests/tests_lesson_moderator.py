from django.contrib.auth.models import Group

import os

from rest_framework.test import APITestCase
from rest_framework import status
from django.forms.models import model_to_dict

from users.models import User
from lms.models import Course, Lesson


class CourseModeratorTestCase(APITestCase):

    def setUp(self):
        self.user_moder = User.objects.create(email='moderator@test.ru')
        group_moder = Group.objects.get_or_create(name='moderator')[0]
        self.user_moder.groups.add(group_moder)

        self.user_3 = User.objects.create(email='not_moderator@test.ru')

        self.course_1 = Course.objects.create(
            title="title_course",
            description="description_course",
            preview=os.path.join('lms', 'courses', 'previews', 'shutterstock_571762606.webp'),
            creator=self.user_moder
        )
        self.lesson_1 = Lesson.objects.create(
            title="title_lesson",
            description="description_lesson",
            video_url="http://youtube.com/test_lesson.mp4",
            preview=os.path.join('lms', 'lessons', 'previews', 'shutterstock.webp'),
            course=self.course_1,
            creator=self.user_moder
        )

        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user_moder)

    def test_create_lesson_moderator(self):
        """ Тестирование создания урока модератором: запрещено """

        response = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )

        # Проверяем создание записи
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(
            response.json(),
            {'detail': 'У вас недостаточно прав для выполнения данного действия.'}
        )

    def test_list_lesson_moderator(self):
        """ Тестирование вывода списка модератором: разрешено """

        response = self.client.get(
            '/lms/lesson/'
        )

        # Проверяем вывод списка записей
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_lesson_moderator(self):
        """ Тестирование вывода урока модератором: разрешено"""

        self.client.force_authenticate(user=self.user_3)
        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )
        self.client.logout()

        self.client.force_authenticate(user=self.user_moder)
        response_detail = self.client.get(
            f"/lms/lesson/{response_create.json()['id']}/"
        )

        # Проверяем вывод одной записи
        self.assertEqual(
            response_detail.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson_moderator(self):
        """ Тестирование редактирования урока модератором: разрешено """

        self.client.force_authenticate(user=self.user_3)
        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )
        self.client.logout()

        self.client.force_authenticate(user=self.user_moder)
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

    def test_delete_lesson_moderator(self):
        """ Тестирование удаления урока модератором: запрещено """

        self.client.force_authenticate(user=self.user_3)
        response_create = self.client.post(
            '/lms/lesson/create/',
            data=model_to_dict(self.lesson_1)
        )
        self.client.logout()

        self.client.force_authenticate(user=self.user_moder)
        response_delete = self.client.delete(
            f"/lms/lesson/delete/{response_create.json()['id']}/"
        )

        # Проверяем удаление
        self.assertEqual(
            response_delete.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertEqual(
            response_delete.json(),
            {'detail': 'У вас недостаточно прав для выполнения данного действия.'}
        )
