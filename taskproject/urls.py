from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('tasks/', include('tasks.urls')),
    path('health', lambda request: HttpResponse('OK')),
]