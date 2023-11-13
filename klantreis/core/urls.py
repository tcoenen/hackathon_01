from django.urls import path

from core.views import ProcessView


urlpatterns = [
    path('process_view/<int:pk>/', ProcessView.as_view()),
]
