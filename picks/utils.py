# picks/utils.py
from django.utils import timezone
from django.conf import settings

def contest_started():
    return timezone.now() >= settings.CONTEST_START
