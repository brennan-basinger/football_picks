# picks/management/commands/bulk_create_users.py
from django.core.management.base import BaseCommand, CommandError
import csv
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = (
        "Bulk-create users from a CSV file."
        "\nExpected columns: email, first_name, last_name, phone_number[, password]"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to the CSV file containing user data'
        )

    def handle(self, *args, **options):
        path = options['csv_file']
        User = get_user_model()

        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                created = 0
                for row in reader:
                    email = row.get('email', '').strip()
                    first = row.get('first_name', '').strip()
                    last = row.get('last_name', '').strip()
                    phone = row.get('phone_number', '').strip()
                    pwd = row.get('password') or User.objects.make_random_password()

                    if not email:
                        self.stderr.write(self.style.ERROR("Missing email on row: %s" % row))
                        continue

                    if User.objects.filter(email=email).exists():
                        self.stdout.write(self.style.WARNING(f"Skipped {email}: already exists."))
                        continue

                    user = User.objects.create_user(
                        email=email,
                        password=pwd,
                        first_name=first,
                        last_name=last,
                        phone_number=phone
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"Created user {email} with password '{pwd}'"
                    ))
                    created += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully processed. {created} users created."))

        except FileNotFoundError:
            raise CommandError(f"File '{path}' does not exist.")
        except csv.Error as e:
            raise CommandError(f"CSV error: {e}")
