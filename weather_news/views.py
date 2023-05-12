from rest_framework import generics
from .models import Weather, News
from .serializers import WeatherSerializer, NewsSerializer

class WeatherListAPIView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the queryset based on query parameters
        city = self.request.query_params.get('city')
        temperature__gte = self.request.query_params.get('temperature__gte')
        if city:
            queryset = queryset.filter(city=city)
        if temperature__gte:
            queryset = queryset.filter(temperature__gte=temperature__gte)
        return queryset

class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter the queryset based on query parameters
        source = self.request.query_params.get('source')
        author = self.request.query_params.get('author')
        if source:
            queryset = queryset.filter(source=source)
        if author:
            queryset = queryset.filter(author=author)
        return queryset
