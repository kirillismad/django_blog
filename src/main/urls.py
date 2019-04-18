from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='root'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
]
