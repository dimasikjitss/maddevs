import json
import codecs
import os.path

try:
    from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version
    )
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError,
        __version__ as client_version
    )


def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json, indent=4)
        print('SAVED: {0!s}'.format(new_settings_file))


class Bot:
    a = 2
    def __init__(self, login=None, password=None, proxy=None):
        self.login = login
        self.password = password
        self.device_id = None

        try:
            settings_file = f'accounts/{self.login}.json'

            if not os.path.isfile(settings_file):

                self.api = Client(
                    self.login, self.password,
                    on_login=lambda x: onlogin_callback(x, f'accounts/{self.login}.json'),
                    proxy=proxy
                )
            else:
                with open(settings_file) as file_data:
                    cached_settings = json.load(file_data, object_hook=from_json)

                self.device_id = cached_settings.get('device_id')

                self.api = Client(
                    self.login, self.password,
                    settings=cached_settings,
                    proxy=proxy
                )
        except ClientCookieExpiredError as e:
            print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))

            # Login expired
            # Do relogin but use default ua, keys and such
            self.api = Client(
                self.login, self.password,
                device_id=self.device_id,
                on_login=lambda x: onlogin_callback(x, settings_file),
                proxy=proxy
            )

    def get_posts(self, username):
        user = self.api.search_users(
            username
        )

        pk = user['users'][0]['pk']

        for i in user['users']:
            if username == i['username']:
                pk = i['pk']
                break

        posts = self.api.user_feed(pk)
        posts_info = []

        for i in posts['items']:
            if i.get('video_versions'):
                for media in i['video_versions']:
                    if media['width'] > 1000:
                        posts_info.append(
                            [

                            ]
                        )
                        posts_info[-1].append(i['id'])
                        posts_info[-1].append(media['url'])
                        posts_info[-1].append(i['comment_count'])
                        posts_info[-1].append(i['like_count'])
                        if i.get('caption'):
                            posts_info[-1].append(i['caption']['text'])
                        else:
                            posts_info[-1].append('none')

            elif i.get('carousel_media'):
                for media in i['carousel_media']:
                    if media.get('video_versions'):
                        for video in media['video_versions']:
                            posts_info.append(
                                [

                                ]
                            )
                            posts_info[-1].append(i['id'])
                            posts_info[-1].append(video['url'])
                            posts_info[-1].append(i['comment_count'])
                            posts_info[-1].append(i['like_count'])
                            if i.get('caption'):
                                posts_info[-1].append(i['caption']['text'])
                            else:
                                posts_info[-1].append('none')
                    else:
                        for video in media['image_versions2']['candidates']:
                            posts_info.append(
                                [

                                ]
                            )
                            posts_info[-1].append(i['id'])
                            posts_info[-1].append(video['url'])
                            posts_info[-1].append(i['comment_count'])
                            posts_info[-1].append(i['like_count'])
                            if i.get('caption'):
                                posts_info[-1].append(i['caption']['text'])
                            else:
                                posts_info[-1].append('none')

            else:
                for media in i['image_versions2']['candidates']:
                    if media['width'] > 1000:
                        posts_info.append(
                            [

                            ]
                        )
                        posts_info[-1].append(i['id'])
                        posts_info[-1].append(media['url'])
                        posts_info[-1].append(i['comment_count'])
                        posts_info[-1].append(i['like_count'])
                        if i.get('caption'):
                            posts_info[-1].append(i['caption']['text'])
                        else:
                            posts_info[-1].append('none')



        return posts_info

