from django.urls import path
from .views import ConferenceCreateView, home, about, profile, conferenceList, ConferenceListView, ConferenceDetailView, ConferenceDeleteView


urlpatterns = [
    path('', home, name='conference_home'),
    path('about/', about, name='conference_about'), # 127.0.0.1:8000/conference/about/
    path('profile/<str:username>/', profile, name='conference_profile'),
    path('conferences/', conferenceList, name='conference_list'),
    path('conferencesLV/', ConferenceListView.as_view(), name='conference_list_lv'),
    path('conference/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail_lv'),
    path('conference/delete/<int:pk>/', ConferenceDeleteView.as_view(), name='conference_delete_lv'),
    path('create/', ConferenceCreateView.as_view(), name='conference_create_lv'),
]