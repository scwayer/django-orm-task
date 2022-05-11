from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import is_visit_long
from .models import get_duration


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits_serialized = []
    for visit in Visit.objects.filter(passcard__passcode=passcode):
        this_passcard_visits_serialized.append({
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit) 
        })

    context = {
        'passcard': this_passcard,
        'this_passcard_visits': this_passcard_visits_serialized
    }
    return render(request, 'passcard_info.html', context)
