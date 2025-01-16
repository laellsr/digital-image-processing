import cv2, os, re
import matplotlib.pyplot as plt
import numpy as np

dir = os.getcwd()
endsWith = re.compile(r'.*(\.jpg$|\.png$|\.tif$)')
hsvImages = []

# Executar a atividade anterior (Parte 1) 
# só que convertendo cada imagem para HSV antes de visualizar.

#  1
plt.subplots_adjust(hspace=0.5, wspace=0.5)
index = 241
for file in os.listdir(dir):
    if endsWith.match(file):
        hsvImg = cv2.cvtColor(cv2.imread(os.path.abspath(file)), cv2.COLOR_BGR2HSV)
        # hsvImg = cv2.imread(os.path.abspath(file))
        hsvImages.append(hsvImg)
        plt.subplot(index)
        plt.imshow(hsvImg)
        plt.title(file)
        index += 1
plt.show()

# 2
fig, ax = plt.subplots(8,3)
fig.subplots_adjust(hspace=1, wspace=1)
for row, hsvImg in enumerate(hsvImages):
    h = hsvImg[:,:,0]
    s = hsvImg[:,:,1]
    v = hsvImg[:,:,2]
    ax[row, 0].imshow(h)
    ax[row, 0].set_title('h')
    ax[row, 1].imshow(s)
    ax[row, 1].set_title('s')
    ax[row, 2].imshow(v)
    ax[row, 2].set_title('v')
plt.show()

# 3
hsvNormImages = []
for hsvImg in hsvImages:
    hsvNormImages.append(np.float32(hsvImg)/255.0)
    
# 4
for img in hsvNormImages:
    cv2.namedWindow('Imagem Normalizada', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Imagem Normalizada', img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

for index, img in enumerate(hsvNormImages):
    plt.subplot(2,4,1+index)
    plt.imshow(img)
plt.show()