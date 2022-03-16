from . import views
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'user',views.UserAppViewSet,basename='UserApp')