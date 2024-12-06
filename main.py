import ClasseDePastas as CP
from ClasseDePastas import *

def CriarPasta(QdeArquivos=5):
    Pasta1 = Pasta()
    Pasta1.CriarPastaVazia()
    for _ in range(QdeArquivos):
        Pasta1.Receber_Arquivo()
    Pasta1.get_chaves_arquivos_pasta()
    return Pasta1 




if __name__=="__main__":
    PastaMat = {}

    # Pasta1 = Pasta() #cria a pasta
    # Pasta1.CriarPastaVazia()
    # Pasta1.get_idPasta()
    # for i in range(3):
    #     Pasta1.Receber_Arquivo()

    # Pasta1.get_chaves_arquivos_pasta()
    # Pasta1.Remover_Arquivo()
    # print("Verificação de remoção")
    # Pasta1.get_chaves_arquivos_pasta
