from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, URLField

from .models import InstagramUser, PostInfo


class InstagramUserListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = InstagramUser
        fields = '__all__'


class InstagramDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = InstagramUser
        fields = ['username', 'posts']


class PostInfoListSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PostInfo
        fields = '__all__'


class PostInfoDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PostInfo
        fields = '__all__'
