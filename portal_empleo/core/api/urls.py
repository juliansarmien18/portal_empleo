from . import views
from rest_framework import routers
from django.urls import include,re_path



router = routers.DefaultRouter()

router.register(r'user',views.UserAppViewSet,basename='UserApp')


urlpatterns = [
    re_path(r'^', include(router.urls)),
]