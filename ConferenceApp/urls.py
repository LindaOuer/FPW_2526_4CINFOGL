from django.urls import path
from .views import home, about, profile, conferenceList, ConferenceListView, ConferenceDetailView


urlpatterns = [
    path('', home, name='conference_home'),
    path('about/', about, name='conference_about'), # 127.0.0.1:8000/conference/about/
    path('profile/<str:username>/', profile, name='conference_profile'),
    path('conferences/', conferenceList, name='conference_list'),
    path('conferencesLV/', ConferenceListView.as_view(), name='conference_list_lv'),
    path('conference/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail_lv'),
]