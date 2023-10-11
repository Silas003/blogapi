from django.urls import path
from .views import CustomUserCreate,BlacklistView

app_name='users'
urlpatterns=[
    path('register',CustomUserCreate.as_view(),name='create_user'),
    path('blackist',BlacklistView.as_view())
]