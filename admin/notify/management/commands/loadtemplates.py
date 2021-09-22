import json

from django.core.management.base import BaseCommand
from notify.models import MessageTemplate


class Command(BaseCommand):
    help = 'Load templates for notifications.'

    def add_arguments(self, parser):
        parser.add_argument('file-name', nargs='+', type=str, action='store',
                            default='templates.json', help='template file name')

    def handle(self, *args, **options):
        files = options['file-name']

        for file in files:
            with open(file, 'r') as templates_file:
                templates = json.load(templates_file)
                print(templates)
                for template in templates:

                    template_obj = MessageTemplate.objects.filter(
                        type=template["type"]
                    )

                    if not template_obj:
                        new_template = MessageTemplate(**template)
                        new_template.save()
                    else:
                        template_obj.update(**template)