from . import views
from django.urls import path

app_name='departmentapp'

urlpatterns = [
    path('alldepartment/',views.alldepartment,name='alldepartment'),
    path('<slug:d_slug>/',views.alldepartment,name='doctors_by_department'),
    path('<slug:d_slug>/<slug:doctor_slug>/', views.docDetail, name='docdepartmentdetail'),
]
