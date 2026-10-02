#Importar Bibilhotecas
from libs import cfglib as Config
from libs.gbulib import downloadpost, getposts
from time import sleep
from threading import Thread, enumerate

#Define o controlador de configs.
cfg = None

#Define as tags que o usuario quer e o tanto de paginas que o usuario quer carregar.
def main(cfg):
    tags = str(input('Please enter tags separated by spaces: ')).lower()

    while True:
        # Trata erros de input.
        try:
            pages = int(input('Please enter pages you would like to download (10 posts per page): '))
            # Verifica se o ser humano tem mente o suficiente e não mete um -1.
            if pages <= 0:
                print(' Please enter a valid amount of pages.')
                continue
            break
        except ValueError:
           print('please enter a valid integer.')

    #Tenta puxar a lista de posts.
    try:
        posts = getposts(tags, pages, cfg.api, cfg.apikey, cfg.userid)
    except ConnectionError:
        print('Connection error, please try again later.')
        exit()

    print('Download has started and will shortly start, the script is not stuck. please be patient.')

    #Inicia downloads.
    for post in posts:
        url = post
        name = post.split('/')[-1]
        if cfg.multithreaded:
            if not len(enumerate()) > 10:
                Thread(target=downloadpost, args=(url, name, cfg.dwpath), daemon=True).start()
            else:
                sleep(0.1)
        else:
            downloadpost(url, name, cfg.dwpath)
    while not len(enumerate()) == 1:
        sleep(0.5)
    exit()

if __name__ == '__main__':
    cfg = Config.ConfigManager()
    try:
        main(cfg=cfg)
    except KeyboardInterrupt:
        exit()