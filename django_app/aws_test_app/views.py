from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader


# Create your views here.
def index(request):
    # template = loader.get_template('aws_test_app/index.html')
    # return HttpResponse(template.render(request))
    return render(request, 'aws_test_app/index.html')
