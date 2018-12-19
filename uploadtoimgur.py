from imgurpython import ImgurClient
from local import client_id, client_secret, album_id, access_token, refresh_token

# if __name__ == "__main__":
def upload2imgur(id):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    path = "./event(%s).jpg"%id
    config = {
        'album': album_id,
        'name': id,
        'title': id,
        'description': 'test-description'
    }
    print("Uploading image... ")
    image = client.upload_from_path(path, config=config, anon=False)
    print("Done")
    return image.get('link')