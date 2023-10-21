import cv2
import matplotlib.pyplot as plt
import numpy as np

def plot_results(before, after):
    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(wspace=0.02)
    
    plt.subplot(1, 2, 1)
    plt.imshow(before)
    plt.title("Antes", fontsize=20)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("Depois", fontsize=20)
    plt.axis('off')

    plt.show()

def high_boost_filter(imagem, matrix):
    # borra a imagem
    imagem_borrada = cv2.GaussianBlur(imagem, matrix, 0)
    
    # a mascara é definida pela diferença entra a imagemm borrada e a original
    mask = np.subtract(imagem, imagem_borrada)

    # o resultado é a soma da máscara com a imagem borrada
    resultado = np.add(imagem, mask)
    plot_results(imagem, resultado)


if __name__ == "__main__":
    # imagem= cv2.imread("lena_gray_512.tif")
    imagem= cv2.imread("imagens/pirate.tif")
    # imagem= cv2.imread("house.tif")s
    high_boost_filter(imagem, (7,7))