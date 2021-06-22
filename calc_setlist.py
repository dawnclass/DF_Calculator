#-*- coding: utf-8 -*-
## 코드를 무단으로 복제하여 개조 및 배포하지 말 것##
## Copyright ⓒ 2020 Dawnclass(새벽반) dawnclass16@naver.com

import itertools



def make_list(list0,list1,list2,list3):
    all_list=[]
    all_list1=[]
    all_list2=[]
    all_list3=[]


    if list0 !=[]:
        all_list=list(itertools.product(*list0))
    
    if list1 !=[]:
        if len(list1[0]) != 0:
            all_list1=list(itertools.product(*list1))

    if list2 !=[]:
        if len(list2[5]) != 0:
            all_list2=list(itertools.product(*list2))


    if list3 !=[]:
        if len(list3[10]) != 0:
            all_list3=list(itertools.product(*list3))
        
        
    all_list_god=all_list1+all_list2+all_list3
    all_list_num=len(all_list_god)+len(all_list)
    return [all_list,all_list_god,all_list_num]

know_list = ['11390850','11390860','11390870',
             '12390950','12390960','12390970',
             '13390150','13390160','13390170',
             '13391050','13391060','13391070',
             '14391150','14391160','14391170',
             '15391250','15391260','15391270',
             '21391340','21391350','21391360','21391370',
             '21390340','21390350','21390360','21390370',
             '22390240','22390250','22390260','22390270',
             '22391440','22391450','22391460','22391470',
             '23391540','23391550','23391560','23391570',
             '23390450','23390460','23390470',
             '31390540','31390550','31390560','31390570',
             '31391640','31391650','31391660','31391670',
             '32390650','32390660','32390670',
             '32391740','32391750','32391760','32391770',
             '33390750','33390760','33390770',
             '33391840','33391850','33391860','33391870',
             ]
