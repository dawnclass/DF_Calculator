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
