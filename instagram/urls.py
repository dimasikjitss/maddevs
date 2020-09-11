from django.urls import path

from . import views


urlpatterns = [
    path('user/list/', views.InstagramUserListAPIView.as_view(), name='instagramuser-list'),
    path('user/<int:pk>/', views.InstagramUserRetrieveAPIView.as_view(), name='instagramuser-detail'),

    path('post/list/', views.PostInfoListAPIView.as_view(), name='postinfo-list'),
    path('post/<int:pk>/', views.PostInfoRetrieveAPIView.as_view(), name='postinfo-detail'),

    path('post/get/', views.get_posts, name='h')

]
