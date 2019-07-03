# Importação das bibliotecas
import cv2 # biblioteca de visão computacional
import numpy as np # biblioteca para manipulação de arrays e matrizes

#leitura da imagem de entrada
img = cv2.imread('ponte.png')
#exibição da imagem original
cv2.imshow('Original', img)
#separação dos canais
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

#juntar os canais
resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow("RGB", resultado)

#transformações em espaço de cores
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycrcb", ycrcb)

#exibir os canais nas cores originais
img2 = cv2.imread('ponte.png')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img2)
zeros = np.zeros(img2.shape[:2], dtype = "uint8")

cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow("Original", img)

(b, g, r) = img2[0, 0] #veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

#navegando na imagem em linhas e colunas
imagemm = cv2.imread('ponte.png')
for y in range(0, imagemm.shape[0]):
    for x in range(0, imagemm.shape[1]):
        imagemm[y, x] = (255,0,0)
        cv2.imshow("Imagem modificada", imagemm)

cv2.waitKey(0) #espera pressionar qualquer tecla
