from django.urls import path
from .views import homePage, EventListView, EventDetailView, event, registration, RegistrationUpdateView, RegistrationDeleteView

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('dashboard/', event, name='event'),
    path('dashboard/event/register/', registration, name='register'),
    path('dashboard/event/registeredevent/', EventListView.as_view(), name='registered-events'),
    path('dashboard/event/<int:pk>/', EventDetailView.as_view(), name='event-details'),
    path('dashboard/event/<int:pk>/update/', RegistrationUpdateView.as_view(), name='registration-update'),
    path('dashboard/event/<int:pk>/delete/', RegistrationDeleteView.as_view(), name='registration-delete'),    
]