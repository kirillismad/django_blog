from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission, SAFE_METHODS

DELETE = 'DELETE'


class PostDetailPermission(BasePermission):
    message = _('You must be author of post')

    def has_object_permission(self, request, view, post):
        if request.method not in SAFE_METHODS:
            return post.author_id == request.user.pk
        return True


# class CommentDetailPermission(BasePermission):
#     def has_object_permission(self, request, view, comment):
#         if request.method not in SAFE_METHODS:
#             user = request.user
#             if request.method == DELETE:
#                 return comment.author_id == user.pk or comment.post.author_id == user.pk
#             # PUT / PATCH
#             return comment.author_id == user.pk
#         return True


class CommentUpdatePermission(BasePermission):
    message = _('You must be author of comment')

    def has_object_permission(self, request, view, comment):
        if request.method in {'PUT', 'PATCH'}:
            return comment.author_id == request.user.pk
        return True


class CommentDeletePermission(BasePermission):
    message = _('You must be author of comment or author of post')

    def has_object_permission(self, request, view, comment):
        if request.method == DELETE:
            return comment.author_id == request.user.pk or comment.post.author_id == request.user.pk
        return True


CommentDetailPermission = CommentUpdatePermission & CommentDeletePermission
