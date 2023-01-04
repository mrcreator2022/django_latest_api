from django.urls import path

from . import views

urlpatterns = [
    path('employeeapi/',views.employeeapi, name="employeeapi"),
    path('employeeapi/<int:id>',views.employeeapi, name="employeeapi"),
]
