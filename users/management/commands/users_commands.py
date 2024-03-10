import os

from django.core.management import BaseCommand, call_command

from users.models import User, Payment
from core.settings import BASE_DIR
from django.db.utils import ProgrammingError, IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем данные из таблиц БД
        User.objects.all().delete()
        Payment.objects.all().delete()

        # Путь к фикстурам
        path_fixture = os.path.join(BASE_DIR, 'fixtures', 'users_data.json')

        # Вызов команды loaddata - загрузка данных в БД из фикстур
        try:
            call_command('loaddata', path_fixture)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Ошибка фикстур: {e}', self.style.NOTICE)
        else:
            self.stdout.write('OK', self.style.SUCCESS)
