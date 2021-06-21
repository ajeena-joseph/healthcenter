from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from .models import Doctor, Department


# Create your views here.

def alldepartment(request, d_slug=None):
    d_page = None
    doctors_list = None
    if d_slug != None:
        d_page = get_object_or_404(Department, slug=d_slug)
        doctors_list = Doctor.objects.all().filter(department=d_page)
    else:
        doctors_list = Doctor.objects.all()
    paginator = Paginator(doctors_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        doctors = paginator.page(page)
    except(EmptyPage, InvalidPage):
        doctors = paginator.page(paginator.num_pages)

    return render(request, "doctor.html", {'department': d_page, 'doctors': doctors_list})


def docDetail(request, d_slug, doctor_slug):
    try:
        doctor = Doctor.objects.get(department__slug=d_slug, slug=doctor_slug)
    except Exception as e:
        raise e
    return render(request, "doctorsdetails.html", {'doctor': doctor})

