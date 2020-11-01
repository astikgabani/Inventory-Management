from rest_framework import serializers

from inventory_api import models


class InventoryCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InventoryCategoryModel
        fields = ('url', 'id', 'name',)

    def create(self, validated_data):
        category = models.InventoryCategoryModel.objects.create_category(**validated_data)
        return category


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    category = InventoryCategorySerializer()

    class Meta:
        model = models.InventoryModel
        fields = '__all__'
        extra_kwargs = {
            'is_qa_approved': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        inventory = models.InventoryModel.objects.create_inventory(**validated_data)
        return inventory


class InventoryQASerializer(serializers.HyperlinkedModelSerializer):
    category = InventoryCategorySerializer()

    class Meta:
        model = models.InventoryModel
        fields = '__all__'
