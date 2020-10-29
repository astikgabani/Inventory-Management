from rest_framework.routers import DefaultRouter

from django.urls import path, include

from employees_api import views


router = DefaultRouter()
router.register('employees', views.EmployeeModelView)


urlpatterns = [
    path('', include(router.urls)),
]
