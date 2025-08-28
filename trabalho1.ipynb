#TRABALHO PRATICO JOÃO VITOR REIS E GABRIEL FERNANDES ZAMORA

import cv2  # usando opencv pra fazer a imagem virar matriz
import numpy as np  # usando as propriedades de matriz do numpy
from google.colab.patches import cv2_imshow 

def MatrizExpandida(matriz):
    linha_original, coluna_original = matriz.shape[:2] #conta o numero de linhas e colunas da imagem
    linha_nova = 2 * linha_original - 1
    coluna_nova = 2 * coluna_original - 1
    matriz_expandida = np.zeros((linha_nova, coluna_nova), dtype=matriz.dtype) #inicializa a matriz com 0

    for i in range(linha_original): #coloca os elementos da matriz original na matriz expandida
        for j in range(coluna_original):
            matriz_expandida[2*i, 2*j] = matriz[i, j]
    return matriz_expandida


def AmpliacaoVizinhoProx(matriz):
    matriz_expandida = MatrizExpandida(matriz)
    linha_nova, coluna_nova = matriz_expandida.shape[:2]

    for i in range(linha_nova):
        for j in range(coluna_nova):
            if i % 2 == 1:
                if j % 2 == 0:
                    matriz_expandida[i, j] = matriz_expandida[i-1, j] #se o numero da linha for impar e da coluna par pegar o valor do pixel de cima
                else:
                    matriz_expandida[i, j] = matriz_expandida[i-1, j-1] #se o numero da linha for impar e da coluna impar pegar o valor do pixel do canto superior esquerdo
            elif i % 2 == 0 and j % 2 == 1:
                matriz_expandida[i, j] = matriz_expandida[i, j-1] #se o numero da linha for par e da coluna impar pegar o valor do pixel da esquerda

    return matriz_expandida


def AmpliacaoInterpolacaoBilinear(matriz):
    matriz_expandida = MatrizExpandida(matriz)
    linha_nova, coluna_nova = matriz_expandida.shape[:2]

    for i in range(linha_nova):
        for j in range(coluna_nova):
            if i % 2 == 0 and j % 2 == 1:
                matriz_expandida[i, j] = (matriz_expandida[i, j-1] + matriz_expandida[i, j+1]) // 2 #faz a media entre os pixeis do lado esquerdo e direito
            elif i % 2 == 1 and j % 2 == 0:
                matriz_expandida[i, j] = (matriz_expandida[i-1, j] + matriz_expandida[i+1, j]) // 2 #faz a media entre os pixeis de baixo e de cima
            elif i % 2 == 1 and j % 2 == 1:
                matriz_expandida[i, j] = (
                    matriz_expandida[i-1, j-1] + matriz_expandida[i-1, j+1] + #faz a media entre os pixeis dos 4 cantos
                    matriz_expandida[i+1, j-1] + matriz_expandida[i+1, j+1]
                ) // 4

    return matriz_expandida

def ReducaoInterpolacaoBilinear(matriz):
        linha_original, coluna_original = matriz.shape[:2]
        linha_nova = linha_original // 2
        coluna_nova = coluna_original // 2

        matriz_reduzida = np.zeros((linha_nova, coluna_nova), dtype= matriz.dtype)

        for i in range (0, linha_original, 2): #linha e coluna são puladas de 2 em 2
            for j in range (0, coluna_original, 2):

                p1 = int(matriz[i, j])
                p2 = int(matriz[i, j + 1]) #pega os 4 pixels ao redor e faz a média deles
                p3 = int(matriz[i + 1, j])
                p4 = int(matriz[i + 1, j + 1])


                media = (p1 + p2 + p3 + p4) / 4 
                matriz_reduzida[i // 2 , j // 2] = media

        return matriz_reduzida
                
def ReducaoVizinhoMaisProximo(matriz):
        linha_original, coluna_original = matriz.shape[:2]
        linha_nova = linha_original // 2
        coluna_nova = coluna_original // 2

        matriz_reduzida = np.zeros((linha_nova, coluna_nova), dtype= matriz.dtype)

        for i in range (0, linha_original, 2):
            for j in range (0, coluna_original, 2):

                p1 = int(matriz[i, j]) #pega só o primeiro pixel dos 4

                matriz_reduzida[i // 2 , j // 2] = p1

        return matriz_reduzida



# Testando
img = cv2.imread("/content/imagem.png", cv2.IMREAD_GRAYSCALE) #tira a cor da imagem

vizinho = AmpliacaoVizinhoProx(img)
bilinear = AmpliacaoInterpolacaoBilinear(img)
bilinearReduz = ReducaoInterpolacaoBilinear(img)
vizinhoReduz = ReducaoVizinhoMaisProximo(img)

# Vendo
print("IMAGEM ORIGINAL")
cv2_imshow(img)

print("IMAGEM AUMENTADA COM VIZINHO MAIS PROXIMO")
cv2_imshow(vizinho)

print("IMAGEM AUMENTADA COM INTERPOLAÇAO BILINEAR")
cv2_imshow(bilinear)

print("IMAGEM REDUZIDA COM INTERPOLAÇAO")
cv2_imshow(bilinearReduz)

print("IMAGEM REDUZIDA COM VIZINHO MAIS PROXIMO")
cv2_imshow(vizinhoReduz)
