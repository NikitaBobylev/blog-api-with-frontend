from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("tags/<slug:tag_slug>/", TagDetailView.as_view(), name='tag'),
    re_path(r'tags/?$', TagListView.as_view(), name='all_tags'),
    path('aside/<slug:post_slug>', LastFiveArticlesView.as_view(), name='lastfiveposts'),
    path('feedback/', FeedBackView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('profile/', CureentUserView.as_view()),
    path('comments/<slug:post_slug>/', PostCommentsView.as_view()),
    path('comments/', PostCommentsView.as_view()),
]

urlpatterns += router.urls
