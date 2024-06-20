from django.urls import path
from .views import RegisterUserView, CreateUserProfileView, EditUserProfileView, RetrieveUserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterUserView.as_view(), name='register-user'),
    path('auth/profile/register/', CreateUserProfileView.as_view(), name='create-user-profile'),
    path('auth/profile/edit/', EditUserProfileView.as_view(), name='edit-user-profile'),
    path('auth/profile/', RetrieveUserProfileView.as_view(), name='retrieve-user-profile'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login-user-view'),
]