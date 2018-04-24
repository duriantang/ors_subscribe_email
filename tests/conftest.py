import os
import sys

import django

PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ors_subscribe_email')
sys.path.insert(0, PATH)


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ors_subscribe_email.settings')
    import ors_subscribe_email.settings
    ors_subscribe_email.settings.DATABASES['default'] = {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
    django.setup()

    from django.core.management import call_command
    call_command('migrate')
