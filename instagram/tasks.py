from django.conf import settings
# from django.utils import timezone
from mad_devs.celery import app

from .instagram_bot import Bot

from .models import InstagramUser, PostInfo


@app.task(name='get_posts')
def get_posts():
    bot = Bot('python_test11', 'DimaNovikov15061998')
    for user in InstagramUser.objects.all():
        posts = bot.get_posts(user.username)
        for post in posts:
            if PostInfo.objects.get(media_id=post[0]):
                continue

            PostInfo.objects.create(
                instagram_user=user,
                media_id=post[0],
                image_url=post[1],
                comment_count=post[2],
                like_count=post[3],
                description=post[4]
            )

    return

# get_posts()