from django.urls import path
from .views import home, users, SubscriberDetailView

urlpatterns = [
    path('', home, name='home'),
    path('users/', users, name='users'),
    path('detail/<int:pk>/', SubscriberDetailView.as_view(), name='detail'),
]