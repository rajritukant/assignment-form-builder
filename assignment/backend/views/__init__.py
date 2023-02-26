from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test_func(request):
    print("******" * 5)
    print("testing backend")
    print("******" * 5)
    return HttpResponse("backend testing success!!")


