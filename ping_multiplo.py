# importando bibliotecas
import os
import time

with open("hosts.txt") as file:
    dump = file.read()

    # coloca o dump em linhas separadas
    dump = dump.splitlines()
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)