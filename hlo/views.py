from django.shortcuts import render
from enquiry.models import Enquiry


def index(request):
    return render(request, 'hlo/index.html', {})