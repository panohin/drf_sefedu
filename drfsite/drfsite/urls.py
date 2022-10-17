from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from women import views


# router = routers.SimpleRouter()
# router2 = routers.DefaultRouter()
# # router.register('women', WomenViewSet)
# router2.register('women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>', views.WomenAPIUpdate.as_view()),
    path('api/v1/women/delete/<int:pk>', views.WomenAPIDestroy.as_view()),
    # path('api/v1/womenlist', WomenViewSet.as_view({'get':'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put':'update', 'get':'retrieve'}), name='update_url'),
]

