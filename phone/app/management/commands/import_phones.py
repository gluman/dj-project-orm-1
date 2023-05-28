from django.core.management.base import BaseCommand
import csv
from app.models import Phone

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('phones.csv') as f:
            line_count = 0
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    text_list = row[1].lower().split(' ')
                    slug = '-'.join(text_list)
                    phone = Phone(
                        name=row[1],
                        image=row[2],
                        price=row[3],
                        release_date=row[4],
                        lte_exists=row[5],
                        slug=slug,
                    )
                    phone.save()
                    line_count += 1
        return print('done')
