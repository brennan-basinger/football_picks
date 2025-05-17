# picks/context_processors.py
from django.conf import settings
from django.utils import timezone

def contest_timing(request):
    return {
        'CONTEST_START': settings.CONTEST_START,
        'now': timezone.now(),
    }
