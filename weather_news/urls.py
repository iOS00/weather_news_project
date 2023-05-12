from django.urls import path
from .views import WeatherListAPIView, NewsListAPIView

app_name = 'weather_news'

urlpatterns = [
    path('', WeatherListAPIView.as_view(), name='weather-list'),
    path('api/weather/', WeatherListAPIView.as_view(), name='weather-list'),
    path('api/news/', NewsListAPIView.as_view(), name='news-list'),
]
