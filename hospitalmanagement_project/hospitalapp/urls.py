from . import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('patient/', views.patient, name='patient'),
    path('addappointment/',views.addappointment,name='addappointment'),
    path('response/', views.response, name='response'),
    path('doctor/<int:doctor_id>/', views.detail, name='detail'),


]
