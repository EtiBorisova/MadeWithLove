from django.urls import path

from MadeWithLove.ads import views

urlpatterns = (
    path('create/', views.CreateAdsView.as_view(), name='create ad'),
    path('details <int:pk>',views.DetailsAdView.as_view(), name='ad details'),
)