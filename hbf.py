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

def high_boost_filter(imagem, kernel, peso):
    # borra a imagem
    imagem_borrada = cv2.GaussianBlur(imagem.astype(np.float32), kernel, 1)
    print(imagem_borrada)
    
    # a mascara é definida pela diferença entra a imagemm borrada e a original
    mask = np.subtract(imagem, imagem_borrada)

    # o resultado é a soma da máscara com a imagem borrada
    resultado = np.add(imagem, np.multiply(mask, peso))
    plot_results(imagem, resultado.astype(np.uint16))


if __name__ == "__main__":
    # imagem= cv2.imread("imagens/lena_gray_512.tif")
    # imagem= cv2.imread("imagens/pirate.tif")
    imagem= cv2.imread("imagens/woman_darkhair.tif")
    # imagem= cv2.imread("house.tif")s
    high_boost_filter(imagem, (7,7), 1)