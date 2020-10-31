from rest_framework import serializers

from inventory_api import models


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InventoryModel
        fields = ('url', 'title', 'description', 'stock', 'category', 'is_qa_approved')
        extra_kwargs = {
            'is_qa_approved': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        inventory = models.InventoryModel.objects.create_inventory(**validated_data)
        return inventory


class InventoryQASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InventoryModel
        fields = ('url', 'title', 'description', 'stock', 'category', 'is_qa_approved')


class InventoryCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InventoryCategoryModel
        fields = ('url', 'id', 'name',)

    def create(self, validated_data):
        category = models.InventoryCategoryModel.objects.create_category(**validated_data)
        return category
