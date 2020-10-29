from rest_framework import serializers

from employees_api import models


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmployeeModel
        fields = ('url', 'email', 'name', 'password', 'type')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password',
                }
            }
        }

    def create(self, validated_data):
        employee = models.EmployeeModel.objects.create_user(**validated_data)
        return employee
