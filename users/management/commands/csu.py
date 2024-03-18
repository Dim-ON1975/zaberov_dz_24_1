from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='zaberov.dv@yandex.ru',
            first_name='Дмитрий',
            last_name='Заберов',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('123qwe456asd')
        user.save()
