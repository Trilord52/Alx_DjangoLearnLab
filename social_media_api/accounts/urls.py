from django.urls import include, path
from .views import RegisterView, LoginView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('api/accounts/', include('accounts.urls')),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
