from api.views import (
    CommentViewSet,
    GroupViewSet,
    PostViewSet,
    api_comment_detail,
)
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'})
    ),
    path('posts/<int:post_id>/comments/<int:comment_id>/', api_comment_detail)
]
