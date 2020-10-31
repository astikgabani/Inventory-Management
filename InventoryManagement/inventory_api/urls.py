from rest_framework.routers import DefaultRouter, SimpleRouter

from django.urls import path, include

from inventory_api import views


router = DefaultRouter()
router.register('items', views.InventoryModelView)
router.register('category', views.InventoryCategoryModelView)


urlpatterns = [
    path('', include(router.urls)),
]
