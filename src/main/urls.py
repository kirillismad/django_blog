from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='root'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.SignInView.as_view(), name='sign_in'),
    path('sign_out/', views.SingOut.as_view(), name='sign_out'),
    path('profiles/', views.ProfileView.as_view(), name='profiles'),
    path('tags/', views.TagsView.as_view(), name='tags'),
    # path('tags/<int:id>/', views.TagsDetailView.as_view(), name='tags_detail'),
]
