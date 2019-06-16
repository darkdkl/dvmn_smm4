import vk_api

import os

def send_vk(message=None, image=None):
    album_id = int(os.getenv('ALBUM_ID')),
    group_id = int(os.getenv('GROUP_ID'))
    attachments = None
    vk_session = vk_api.VkApi(login=os.getenv('VK_LOGIN'), token=os.getenv('VK_TOKEN'))

    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    if message and image:
        photo = upload.photo(
            image,
            album_id=album_id,
            group_id=group_id
        )
        attachments = f"photo-{group_id}_{photo[0]['id']}"
        vk.wall.post(owner_id=-group_id, message=message +
                 '\n', attachments=attachments)
    elif image:
        photo = upload.photo(
            image,
            album_id=album_id,
            group_id=group_id
        )
        attachments = f"photo-{group_id}_{photo[0]['id']}"
        vk.wall.post(owner_id=-group_id, attachments=attachments)

    elif message:
        vk.wall.post(owner_id=-group_id, message=message)
    else:
        print('No data found.')

if __name__ == '__main__':
    send_vk(None,None)
