from . import views
from rest_framework import routers
from django.urls import include,re_path,path



router = routers.DefaultRouter()

router.register(r'user',views.UserAppViewSet,basename='UserApp')
router.register(r'offers',views.OfferViewSet, basename = "Offers")


urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('login/',views.loginview.as_view(), name = "login"),
]