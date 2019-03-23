from django.urls import path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from rest_framework_jwt.views import refresh_jwt_token
from api import views

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Django blog api",
        default_version='v1',
        contact=openapi.Contact(email="pechkirill@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.SignInView.as_view(), name='sign_in'),
    path('refresh', refresh_jwt_token, name='refresh'),

    path('posts/', views.PostView.as_view(), name='posts'),  # list/create
    path('posts/<int:id>/', views.PostDetailView.as_view(), name='posts_detail'),  # read/update/delete

    path('posts/<int:id>/comments/', views.CommentView.as_view(), name='comments'),  # list/create
    # read/update/delete
    path('posts/<int:id>/comments/<int:comment_id>/', views.CommentDetailView.as_view(), name='comments_detail'),

    path('tags/', views.TagView.as_view(), name='tags'),  # list
    path('tags/<int:id>/posts/', views.TagPostsView.as_view(), name='tags_detail_posts'),  # list

    path('profiles/', views.ProfileView.as_view(), name='profiles'),  # list
    path('profiles/<int:id>/', views.ProfileDetailView.as_view(), name='profile_detail'),  # read
    path('profiles/<int:id>/posts/', views.ProfilePostView.as_view(), name='profile_detail_posts'),  # list
    path('profiles/self/', views.ProfileSelfView.as_view(), name='self'),  # update
]
