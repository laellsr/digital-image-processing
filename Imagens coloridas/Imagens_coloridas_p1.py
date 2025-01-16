import cv2, os, re
import matplotlib.pyplot as plt
import numpy as np

dir = os.getcwd()
endsWith = re.compile(r'.*(\.jpg$|\.png$|\.tif$)')
rgbImages = []

#  1. Carregar e mostrar cada uma das imagens (8 imagens)
plt.subplots_adjust(hspace=0.5, wspace=0.5)
index = 241
for file in os.listdir(dir):
    if endsWith.match(file):
        rgbImg = cv2.cvtColor(cv2.imread(os.path.abspath(file)), cv2.COLOR_BGR2RGB)
        # rgbImg = cv2.imread(os.path.abspath(file))
        rgbImages.append(rgbImg)
        plt.subplot(index)
        plt.imshow(rgbImg)
        plt.title(file)
        index += 1
plt.show()

# 2. Apresentar cada canal de cor (R, G e B) separadamente para cada imagem
fig, ax = plt.subplots(8,3)
fig.subplots_adjust(hspace=1, wspace=1)
for row, rgbImg in enumerate(rgbImages):
    r = rgbImg[:,:,0]
    g = rgbImg[:,:,1]
    b = rgbImg[:,:,2]
    ax[row, 0].imshow(r)
    ax[row, 0].set_title('r')
    ax[row, 1].imshow(g)
    ax[row, 1].set_title('g')
    ax[row, 2].imshow(b)
    ax[row, 2].set_title('b')
plt.show()

# 3. Normalizar cada imagem convertendo para ponto flutuante e dividindo por 255.0
rgbNormImages = []
for rgbImg in rgbImages:
    rgbNormImages.append(np.float32(rgbImg)/255.0)
    
# 4. Apresentar as imagens (do tipo float) usando cv2.namedWindow e matplotlib.
# Qual a diferença entre as estratégias de visualização?

# O método cv2.namedWindow cria uma janela onde o título da janela (trackbar) 
# é uma função de callback para o método cv2.imshow.
# Essa janela exibi e imagem em tempo real.
# Também prioriza a visualização em BGR (inversão do RGB).

# O método do matplotlib exibe a figura na interface da própria biblioteca e
# prioriza a ordem RGB na exibição da imagem. 
# É uma janela separada para visualização e análise de dados.

for img in rgbNormImages:
    cv2.namedWindow('Imagem Normalizada', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Imagem Normalizada', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
cv2.destroyAllWindows()

for index, img in enumerate(rgbNormImages):
    plt.subplot(2,4,1+index)
    plt.imshow(img)
plt.show()