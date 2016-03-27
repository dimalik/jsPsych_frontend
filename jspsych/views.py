import json

from django.views.generic import TemplateView
from django.http import HttpResponse

from experiments.models import JSPsychText

class HomeView(TemplateView):
    template_name = "index.html"


def ajax(request):
    data = json.dumps([x.to_json() for x in JSPsychText.objects.all()])
    return HttpResponse(data, content_type='application/json')
