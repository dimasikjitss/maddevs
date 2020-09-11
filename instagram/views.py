from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import InstagramUser, PostInfo
from .instagram_bot import Bot
from . import serializers


@api_view(['GET'])
def get_posts(request):
    bot = Bot('python_test11', 'DimaNovikov15061998')
    for user in InstagramUser.objects.all():
        posts = bot.get_posts(user.username)
        for post in posts:
            try:
                PostInfo.objects.get(media_id=post[0])
            except PostInfo.DoesNotExist:
                PostInfo.objects.create(
                    instagram_user=user,
                    media_id=post[0],
                    image_url=post[1],
                    comment_count=post[2],
                    like_count=post[3],
                    description=post[4]
                )
    return Response('hello')


class InstagramUserListAPIView(ListCreateAPIView):
    lookup_field = 'pk'
    queryset = InstagramUser.objects.all()
    serializer_class = serializers.InstagramUserListSerializer


class InstagramUserRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = InstagramUser.objects.all()
    serializer_class = serializers.InstagramDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.get_serializer(object)
        return Response(serializer.data)


class PostInfoListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = PostInfo.objects.all()
    serializer_class = serializers.PostInfoListSerializer


class PostInfoRetrieveAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = PostInfo.objects.all()
    serializer_class = serializers.PostInfoDetailSerializer
