import requests
from bs4 import BeautifulSoup

class Aposta:
    def __init__(self, concurso, data, dezenas):
        self._concurso = concurso
        self._data = data
        self._dezenas = dezenas

    @property
    def concurso(self):
        return self._concurso

    @property
    def data(self):
        return self._data

    @property
    def dezenas(self):
        return self._dezenas


class Arquivos:
    def __init__(self, arquivo_texto):
        self._arquivo = arquivo_texto

    def gravar(self, itens):
        with open (self._arquivo, "w") as registro:
            for item in itens:
                dezenas = ""
                for dezena in item.dezenas:
                    dezenas += dezena + " "
                registro.write(item.data + " " + item.concurso + " " + dezenas.strip() +"\n")
        registro.close


mega = requests.get('https://asloterias.com.br/lista-de-resultados-da-mega-sena')


if(mega.status_code == 200):
    soup = BeautifulSoup(mega.content, 'html5lib')
    resultados = soup.text
    indice = resultados.find('sorteados!')
    mega = []
    while True:
        concurso =(resultados[indice + 10:indice + 15])
        data = resultados[indice +17:indice+27]
        dezenas =[]
        for i in range(0,18,3):
            dezenas.append(resultados[indice+31+i:indice+33+i])
            aposta = Aposta (concurso, data, dezenas)
        mega.append((aposta))

        if str(data) == '11/03/1996':
            break
        else:
            indice += 38
    gravador = 'mega.txt'
    arquivo = Arquivos(gravador)
    arquivo.gravar(mega)
    print(mega[0].data)


else:
    print('Não foi possivel abrir URL')
