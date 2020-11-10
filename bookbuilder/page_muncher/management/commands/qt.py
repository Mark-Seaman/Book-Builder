from django.core.management.base import BaseCommand

from page_muncher.quick_test import test_quick


class Command(BaseCommand):
    help = 'Django quick test'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Running quick test ...')
            test_quick()

            self.stdout.write(self.style.SUCCESS('Successfully done'))

        except:
            self.stdout.write('*** Quick test died ***')

