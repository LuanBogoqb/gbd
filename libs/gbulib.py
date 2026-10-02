from requests import get
from time import sleep
from os.path import join, exists

#Manda Baixar os dados pelo getdata e salva em disco com o savefile
def downloadpost(url:str, name:str, downloadpath:str):
    try:
        if not exists(join(downloadpath, name)):
            savefile(getdata(url), name, downloadpath)
        else:
            print(f'Post is already downloaded! skipping: {name}')
    except OSError:
        print('Could not save file. stoping...')
        exit()
#Baixa os dados em byte do arquivo no GelBooru
def getdata(url: str):
    data = get(url)
    return bytes(data.content)

#Salva arquivo em disco com os dados do getdata
def savefile(data: bytes, name: str, downloadpath:str):
    try:
        with open(join(downloadpath, name), "wb") as file:
            file.write(data)
            print(f'Wrote Succesfully: {name}')
        return True
    except (OSError or IOError or PermissionError) as error:
        raise OSError(error)


#Lista os posts com as tags definidas e o numero de paginas que o usuario escolheu.
def getposts(tags: str, pages: int, api: str, apikey:str, userid:str) -> list:
    posts = []
    i = 1
    while len(posts) < pages:
        params = {
            'page': 'dapi',
            's': 'post',
            'q': 'index',
            'json': '1',
            'limit': '10',
            'pid': str(i),
            'tags': tags.lower(),
            'api_key': apikey,
            'user_id': userid
        }
        try:
            query = get(api, params=params)
        except TimeoutError:
            raise ConnectionError('Connection timed out')
        if query.status_code != 200:
            raise ConnectionError('connection error')
        batch = query.json()
        for post in batch['post']:
            posts.append(post['file_url'])
        sleep(1)
        i += 1
    del i
    return posts


