from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_proposal_view, name='upload_proposal'),
]
