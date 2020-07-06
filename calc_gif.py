import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
import time

def img_gif(item_code,value):
    imgtk=[]
    if value==0: ## 신화
        len_gif=12
    elif value==1: ## 시로코
        len_gif=22
    for i in range(0,len_gif):
        effect = cv2.imread('image_effect/'+str(value)+str(i)+'.PNG')

        if value==1:
            effect=effect[1:27,1:27]

        item = cv2.imread('image/'+str(item_code)+'n.PNG')
        item_cut=item[1:27,1:27]

        temp_img = cv2.addWeighted(effect, 40/100, item_cut, 60/100, 0)
        item[1:27,1:27]=temp_img
        item = cv2.cvtColor(item, cv2.COLOR_BGR2RGB)
        temp_img2 = Image.fromarray(item)
        enhancer=ImageEnhance.Brightness(temp_img2).enhance(1.5)
        imgtk.append(ImageTk.PhotoImage(image=enhancer))

    return imgtk
