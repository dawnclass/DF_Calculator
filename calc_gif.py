import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance

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

def make_skill_tag(fillname):
    img = Image.open('skillDB/skill_img/'+str(fillname))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 253 and item[1] > 253 and item[2] > 253:
            newData.append((item[0], item[1], item[2], 0))
        else:
            newData.append(item)
    img.putdata(newData)
    print(type(img))
    img.save('skillDB/skill_img/'+str(fillname))

def auto_run():
    path = "skillDB/skill_img"
    file_list = os.listdir(path)

    print (file_list)
    for now in file_list:
        make_skill_tag(now)


if __name__ == "__main__":
    #make_skill_tag('블러드 앤 체인')
    auto_run()
