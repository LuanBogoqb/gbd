from json import dumps, loads, JSONDecodeError
from os import cpu_count, remove, path, mkdir, getcwd

class ConfigManager():

    #Inicia e carrega as configs.
    def __init__(self) -> None:
        self.api: str = ''
        self.userid: str = ''
        self.apikey: str = ''
        self.dwpath: str = ''
        self.multithreaded: bool = True

        try:
            with open('config.json', 'r') as file:
                config = loads(file.read())
                self.api = config['gelbooru']['endpoint']
                self.userid = config['credentials']['userid']
                self.apikey = config['credentials']['apikey']
                self.dwpath = config['downloads']['path']
                self.multithreaded = bool(config['system']['multithreaded'])
                del config

            #AVISO: Multithreading OFF, VAI deixar os Downloads mais lentos.
            if not self.multithreaded:
                print(f'''WARNING: Multi-threaded downloads are OFF. it CAN make the time to download\nLonger since it will download one-by-one.''')

            else:
                print(f"NOTE: Multi-threading is ON. Network Band-width can spike.")

            if not path.exists(self.dwpath):
                mkdir(self.dwpath)

            dwpath = path.join(getcwd(), self.dwpath)
        # Caso não seja bem sucedido o parsing ou seja em formato incorreto, cria o arquivo denovo.
        # Caso esteja sem permissão ou sei la oque só da erro e sai do programa antes que faz mais cagada.
        except FileNotFoundError:
            print('config.json not found')
            self._saveconfig()
            print('config.json saved, please relaunch.')
            exit()

        except JSONDecodeError:
            print('config.json could not be decoded')
            remove('config.json')
            self._saveconfig()
            print('config.json saved, please configure and re-launch.')
            exit()

        except Exception as e:
            print('error parsing config.json. EXCEPTION:', e)
            exit()

    #Salva as configs template pra config.json.
    def _saveconfig(self) -> None:
        with open('config.json', 'w') as file:
            temp = {
                'gelbooru': {
                    'endpoint': 'https://gelbooru.com/index.php',
                },
                'credentials': {
                    'userid': '<YOUR USER ID>',
                    'apikey': '<YOUR API KEY>'
                },
                'downloads': {
                    'path': '<YOUR DOWNLOAD PATH>'
                },
                'system':{
                    'multithreaded': True
                }
            }
            file.write(dumps(temp, indent=4))
        return


