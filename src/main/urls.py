from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='root'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.SignInView.as_view(), name='sign_in'),
    path('sign_out/', views.SingOut.as_view(), name='sign_out'),
    path('profiles/', views.ProfileView.as_view(), name='profiles'),
    path('profiles/<int:id>/', views.ProfileDetailView.as_view(), name='profiles_detail'),
    path('profiles/<int:id>/update/', views.ProfileUpdateView.as_view(), name='profiles_update'),
    path('tags/', views.TagsView.as_view(), name='tags'),
    path('posts/create/', views.PostCreateView.as_view(), name='posts_create'),
    path('posts/<int:id>/', views.PostDetailView.as_view(), name='posts_detail'),
    path('posts/<int:id>/comments/', views.CommentView.as_view(), name='posts_detail_comment'),
    path('self/', views.ProfileSelfView.as_view(), name='self')
]
