from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from women.views import WomenAPIView, WomenAPIUpdate, WomenAPIList, WomenAPIDetailView, WomenViewSet


router = routers.SimpleRouter()
router.register('women', WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist', WomenViewSet.as_view({'get':'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put':'update', 'get':'retrieve'}), name='update_url'),
]

