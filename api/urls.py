from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from . import views
from .views import NusonViewSet


router = DefaultRouter()
router.register(r'nuson', NusonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('nuson/add', NusonViewSet.add, name='add'),
    path('nuson/vm', NusonViewSet.lookAI, name='Ai'),
    path('api/nuson/<int:pk>/', NusonViewSet.as_view({'delete': 'delete_data'}), name='delete-data'),

    # path('hapus/:{id}', NusonViewSet.add, name='hapus'),
]

