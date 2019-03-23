from rest_framework.permissions import BasePermission, SAFE_METHODS

DELETE = 'DELETE'


class PostDetailPermission(BasePermission):
    def has_object_permission(self, request, view, post):
        if request.method not in SAFE_METHODS:
            return post.author_id == request.user.pk
        return True


class CommentDetailPermission(BasePermission):
    def has_object_permission(self, request, view, comment):
        if request.method not in SAFE_METHODS:
            user = request.user
            if request.method == DELETE:
                return comment.author_id == user.pk or comment.post.author_id == user.pk
            # PUT / PATCH
            return comment.author_id == user.pk
        return True
