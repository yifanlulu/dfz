#encoding: utf-8
from django.shortcuts import render


def course_list(request):
    return render(request,'course/course_index.html')

def course_detail(request,course_id):
    return render(request,'course/course_detail.html')