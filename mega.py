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

    def __str__(self):
        return "{} {} {}".format(self.concurso,  self._dezenas, self._data)

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
        registro.close()


class Loterica:

    def atualizar_resultados(self):
        url = "https://asloterias.com.br/lista-de-resultados-da-mega-sena"
        busca = requests.get(url)
        if(busca.status_code == 200):
            soup = BeautifulSoup(busca.content, 'html5lib')
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
                print(aposta)
                mega.append((aposta))

                if str(data) == '11/03/1996':
                    gravador = 'mega.txt'
                    arquivo = Arquivos(gravador)
                    arquivo.gravar(mega)
                    break
                else:
                    indice += 38
        else:
            print('Não foi possivel abrir URL')
        busca.close()

loteria = Loterica()
loteria.atualizar_resultados()

