from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('<endpoint>', TemplateView.as_view(template_name='index.html')),
]
