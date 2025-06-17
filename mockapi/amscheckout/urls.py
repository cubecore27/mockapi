from django.urls import path
from .views import CheckoutListView, CheckoutResolveView, CheckoutCreateView
urlpatterns = [
    path('api/ams/checkout-tickets', CheckoutListView.as_view(), name='checkout-list'),
    path('api/ams/checkout-resolve/<str:ticket_id>', CheckoutResolveView.as_view(), name='checkout-resolve'),
    path('api/ams/checkout-create', CheckoutCreateView.as_view(), name='checkout-create'),
]
