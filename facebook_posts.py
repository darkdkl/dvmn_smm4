import requests

import os

def send_facebook(message=None, image=None):

    params = {'access_token': os.getenv('FACEBOOK_TOKEN'),
              'caption': message,
              'published': 'True'
              }
    if image and message:
        with open(image, 'rb') as img:
            image = {'file':img}
            requests.post(f'https://graph.facebook.com/v3.3/{os.getenv("FACEBOOK_GROUP_ID")}/photos', params=params, files=image)

    elif message:
        params_only_message = {'access_token': os.getenv('FACEBOOK_TOKEN'),
                               'message': message
                               }
        requests.post(f'https://graph.facebook.com/{os.getenv("FACEBOOK_GROUP_ID")}/feed', params=params_only_message)
    elif image:
        params_only_image = {'access_token': os.getenv('FACEBOOK_TOKEN') }

        with open(image, 'rb') as img:
            image = {'file':img}
            requests.post(f'https://graph.facebook.com/v3.3/{os.getenv("FACEBOOK_GROUP_ID")}/photos', params=params, files=image)

    else:
        print('No data found.')

if __name__ == "__main__":
    send_facebook(None,None)
