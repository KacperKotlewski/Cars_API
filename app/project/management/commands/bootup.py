from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "migrate and collect statics"

    def handle(self, *args, **options):
        call_command("migrate", interactive=False)
        call_command("collectstatic", interactive=False)
