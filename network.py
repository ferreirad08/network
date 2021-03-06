from os import system, remove
import platform


class Network:

    __version__ = '1.0.0'

    def __init__(self, remote_host: str) -> None:
        self.remote_host: str = remote_host
        self.OS = platform.system()

    def ping(self, count: int=1) -> int:
        '''
        Mede a latência da conexão
        '''
        if self.OS == 'Linux':
            return system(f'ping -c {count} {self.remote_host}')

    def is_connected(self) -> bool:
        '''
        Verifica se o dispositivo está corretamente conectado à internet
        '''
        return self.ping() == 0

    def get_port(self, min: int=1, max: int=100) -> str:
        '''
        Obtém a porta em que a conexão foi aberta
        '''
        if self.OS != 'Linux':
            return

        fname: str = 'tempfile.txt'
        system(f'nmap -oN {fname} -p {min}-{max} {self.remote_host}')

        with open(fname, 'r') as f:
            lines: list = f.readlines()
            port, *_ = lines[-3].split('/')

        remove(fname)
        return port
