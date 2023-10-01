from django.urls import path
from . import views

urlpatterns = [
    path('<path:url>', views.generate_page, name='index'),
]