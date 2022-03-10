from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from customer.views import CustomerViewSet
from staff.views import StaffViewSet
from contract.views import ContractViewSet
from event.views import EventViewSet


router_customer = routers.SimpleRouter()
router_customer.register(r'customer/?', CustomerViewSet, basename='customer')

router_staff = routers.SimpleRouter()
router_staff.register(r'staff/?', StaffViewSet, basename='staff')

router_contract = routers.SimpleRouter()
router_contract.register(r'contract/?', ContractViewSet, basename='contract')

router_event = routers.SimpleRouter()
router_event.register(r'event/?', EventViewSet, basename='event')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('', include(router_customer.urls)),
    path('', include(router_staff.urls)),
    path('', include(router_contract.urls)),
    path('', include(router_event.urls)),
]
