import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

diretorio_atual = os.path.dirname(__file__)
caminho_da_pasta = os.path.join(diretorio_atual, 'imagens')

def open_folder():
    conteudos_da_pasta = os.listdir(caminho_da_pasta)
    return conteudos_da_pasta
 
def convert_path(name):
    return os.path.join(caminho_da_pasta, name)

def plot_results(before, after):
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(wspace=0.02)
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title("Antes", fontsize=20)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("Depois", fontsize=20)
    plt.axis('off')

    plt.show()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def high_boost_filter(imagem, kernel, peso):
    imagem = imagem.astype(np.float32)
    # borra a imagem
    imagem_borrada = cv2.GaussianBlur(imagem, kernel, 2)
    # a mascara é definida pela diferença entra a imagemm borrada e a original
    mask = np.subtract(imagem, imagem_borrada)
    # o resultado é a soma da máscara com a imagem borrada multiplicada pelo peso
    resultado = np.add(imagem, np.multiply(mask, peso))
    plot_results(np.clip(imagem, 0, 255).astype(np.uint8), np.clip(resultado, 0, 255).astype(np.uint8))


if __name__ == "__main__":
    op = 0
    lista = open_folder()
    while op != 3:
        print("\n[1] Listar imagens")
        print("[2] Filtragem High Boost")
        print("[3] Encerrar programa")
        op = int(input("\nSelecione uma opção: "))
        if op == 1:
            for imagem in lista:
                print(imagem)
        elif op == 2:
            name = str(input("Digite o nome da imagem: "))
            if name in lista:
                a = float(input("Digite um valor para o peso: "))
                imagem = cv2.imread(convert_path(name))
                high_boost_filter(imagem, (7,7) , a)
            else:
                print("Imagem inválida!")
                continue
        elif op == 3:
            print("Encerrando")
            continue
        else: 
            print("Opção inválida!")