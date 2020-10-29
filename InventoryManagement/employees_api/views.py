from rest_framework import viewsets
from rest_framework import filters

from employees_api import serializers, models
from employees_api import permissions


class EmployeeModelView(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.EmployeeModel.objects.all()

    permission_classes = (permissions.IsOwnerOrAdmin, permissions.permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'email',)
