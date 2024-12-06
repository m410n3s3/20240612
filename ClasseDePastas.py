
import time as t #Obter momento unix em float
import datetime as dt #Obter momento unix com data
import random
class Pasta(object):
    def __init__(self):
        self.id = ''
        self.conteudo = ''
        self.estado = 0 #0 pasta vazia, 1 com documento
        self.documento = {}

    def CriarPastaVazia(self):
        self.id = input("Indetificação da pasta: ")
        self.id = str(int(t.time())) #nos da o momento unix. comentar dps
        self.conteudo = input("Entre com o conteúdo da pasta: ")
        self.estado = 0

    def Receber_Arquivo(self):
        #nome = input("Entre com o nome do arquivo: ")
        # end = input("Entre com o endereço do arquivo: ")
        NomesArquivos = ("Alfredo","Rogério","Astoufo","Carlão","Jorjão")
        nome = NomesArquivos[random.randint(0,len(NomesArquivos)-1)]
        end = dt.datetime.now
        #Arquivo será referenciado por um dicionário
        if self.documento.get(nome) == None:
            self.documento[nome] = end
            self.estado =  1
        else:
            print("Documento contido na pasta")

    def Remover_Arquivo(self):
        arq = input("Entre com o nome do arquivo a remover: ")
        DocumentoRemovido = None
        if self.documento.get(arq) != None:
            DocumentoRemovido = self.documento.pop(arq)
        else:
            print(f"Documento {arq} nao encontrado")
        return DocumentoRemovido
        

    def get_idPasta(self):
        print ("id = ",self.id)
        print ("Conteúdo = ",self.conteudo)

    def get_chaves_arquivos_pasta(self):
        if self.estado == 1:
            print("Relação com os arquivos na pasta: ",self.id)
            for chave, valor in self.documento.items():
                print("\t chave = ",chave, "valor =", valor)
        else:
            print("Pasta está vazia")


if __name__=="__main__":
    Pasta1 = Pasta() #cria a pasta
    Pasta1.CriarPastaVazia()
    Pasta1.get_idPasta()
    Pasta1.Receber_Arquivo()
    Pasta1.get_chaves_arquivos_pasta()
    Pasta1.Remover_Arquivo()