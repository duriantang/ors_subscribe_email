from django.urls import path
from . import apis

urlpatterns = [
    path('save_email/', apis.save_email, name='save_email'),
]
