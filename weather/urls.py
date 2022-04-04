from django.urls import path
from weather.views import LoginUserView, SignUpView, LogoutUserView, ProfileView, UpdateUserView, HistoryView

app_name = 'weather'
urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/', UpdateUserView.as_view(), name='edit'),
    path('profile/history/<int:pk>/', HistoryView.as_view(), name='history')
]