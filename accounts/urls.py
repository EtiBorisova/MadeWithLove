from django.urls import path, include
from MadeWithLove.accounts import views


urlpatterns = (
    path('register/',views.UserRegistration.as_view(), name='register'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(),name='profile details'),
        path('edit/', views.EditProfileView.as_view(), name='profile edit'),
        path('delete/', views.ProfileDeleteView.as_view(),name='profile delete'),
    ])),
)
