from django.db import models


class InstagramUser(models.Model):
    username = models.CharField(max_length=255, verbose_name='Username')

    def __str__(self):
        return self.username


class PostInfo(models.Model):
    instagram_user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE, related_name='posts')
    media_id = models.CharField(max_length=255)
    image_url = models.URLField()
    comment_count = models.BigIntegerField()
    like_count = models.BigIntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.instagram_user)
