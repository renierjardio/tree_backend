from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'trees', views.TreeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('qr/<str:qrCode>/', views.getTreeByQr, name='tree-by-qr'),
]