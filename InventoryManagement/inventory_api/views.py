from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions

from inventory_api import serializers, models

from employees_api.models import EmployeeType


class InventoryModelView(viewsets.ModelViewSet):
    queryset = models.InventoryModel.objects.all()

    permission_classes = (permissions.IsAuthenticated, )

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('description', 'title', 'category',)

    def get_serializer_class(self):
        if self.request.user.type in {EmployeeType.QUALITY_CHECK_PERSON.value, EmployeeType.IT_ADMIN.value}:
            return serializers.InventoryQASerializer
        return serializers.InventorySerializer


class InventoryCategoryModelView(viewsets.ModelViewSet):
    serializer_class = serializers.InventoryCategorySerializer
    queryset = models.InventoryCategoryModel.objects.all()

    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
