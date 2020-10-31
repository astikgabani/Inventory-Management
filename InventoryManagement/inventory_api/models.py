from django.db import models

from django.core.exceptions import ValidationError


def stockValidation(value):
    if value < 0:
        raise ValidationError(f"Stock value is {value}, which should be non-negative.")


class InventoryManager(models.Manager):

    def create_inventory(self, *args, **kwargs):
        inventory = InventoryModel(*args, **kwargs)
        inventory.save(using=self._db)
        return inventory


class InventoryCategoryManager(models.Manager):

    def create_category(self, *args, **kwargs):
        category = InventoryCategoryModel(*args, **kwargs)
        category.save(using=self._db)
        return category


class InventoryCategoryModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = InventoryCategoryManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<InventoryCategoryModel {self.name}>"


class InventoryModel(models.Model):
    """
    Inventory model created for managing the company's assets
    """
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    stock = models.IntegerField(validators=[stockValidation])
    category = models.ForeignKey('InventoryCategoryModel', on_delete=models.CASCADE)

    is_qa_approved = models.BooleanField(default=False)

    objects = InventoryManager()

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<InventoryModel {self.title}>"
