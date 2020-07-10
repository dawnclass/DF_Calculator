#-*- coding: utf-8 -*-
## 코드를 무단으로 복제하여 개조 및 배포하지 말 것##
## Copyright ⓒ 2020 Dawnclass(새벽반) dawnclass16@naver.com

from math import floor
from collections import Counter

not_set_list=['136','137','138','144','145','146','147','148','149']
set_code_list=[]
for i in range(101,150):
    set_code_list.append(str(i))
    
def make_all_equ_list(select_item,select_perfect):
    
    list11=[];list12=[];list13=[];list14=[];list15=[]
    list21=[];list22=[];list23=[];list31=[];list32=[];list33=[]
    list11_0=[];list11_1=[];list21_0=[];list21_1=[];list33_0=[];list33_1=[]
    list_setnum=[];list_setnum1=[];list_setnum2=[];list_num=[]
    ##에픽
    for i in range(101,199):
        try:
            if eval('select_item["tg1{}0"]'.format(i)) == 1:
                list11.append('1'+str(i)+'0')
                list11_0.append('1'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    
    for i in range(201,299):
        try:
            if eval('select_item["tg1{}0"]'.format(i)) == 1:
                list12.append('1'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(301,399):
        try:
            if eval('select_item["tg1{}0"]'.format(i)) == 1:
                list13.append('1'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(401,499):
        try:
            if eval('select_item["tg1{}0"]'.format(i)) == 1:
                list14.append('1'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(501,599):
        try:
            if eval('select_item["tg1{}0"]'.format(i)) == 1:
                list15.append('1'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(101,199):
        try:
            if eval('select_item["tg2{}0"]'.format(i)) == 1:
                list21.append('2'+str(i)+'0')
                list21_0.append('2'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(201,299):
        try:
            if eval('select_item["tg2{}0"]'.format(i)) == 1:
                list22.append('2'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(301,399):
        try:
            if eval('select_item["tg2{}0"]'.format(i)) == 1:
                list23.append('2'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(101,199):
        try:
            if eval('select_item["tg3{}0"]'.format(i)) == 1:
                list31.append('3'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(201,299):
        try:
            if eval('select_item["tg3{}0"]'.format(i)) == 1:
                list32.append('3'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(301,399):
        try:
            if eval('select_item["tg3{}0"]'.format(i)) == 1:
                list33.append('3'+str(i)+'0')
                list33_0.append('3'+str(i)+'0')
                list_num.append(str(i)[1:]+'0')
                list_setnum.append('1'+str(i)[1:3])
                list_setnum1.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
  
    algo_list=['11','12','13','14','15','21','22','23','31','32','33']
    if select_perfect[0:4] == '단품제외':
        for i in list_num:
            if list_num.count(i)==1:
                if i[-1]!='1':
                    for ca in algo_list:
                        try:
                            eval("list{}.remove('{}{}')".format(ca,ca,i))
                            eval("list{}_0.remove('{}{}')".format(ca,ca,i))
                        except:
                            c=1

    ##신화                        
    for i in range(101,199):
        try:
            if eval('select_item["tg1{}1"]'.format(i)) == 1:
                list11.append('1'+str(i)+'1')
                list11_1.append('1'+str(i)+'1')
                if list11.count('1'+str(i)+'0')==0:
                    list_setnum.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(101,199):
        try:
            if eval('select_item["tg2{}1"]'.format(i)) == 1:
                list21.append('2'+str(i)+'1')
                list21_1.append('2'+str(i)+'1')
                if list21.count('2'+str(i)+'0')==0:
                    list_setnum.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    for i in range(301,399):
        try:
            if eval('select_item["tg3{}1"]'.format(i)) == 1:
                list33.append('3'+str(i)+'1')
                list33_1.append('3'+str(i)+'1')
                if list33.count('3'+str(i)+'0')==0:
                    list_setnum.append('1'+str(i)[1:3])
                list_setnum2.append('1'+str(i)[1:3])
        except KeyError as error:
            c=1
    set_num_dict=Counter(list_setnum) ##전부
    set_num_dict1=Counter(list_setnum1) ##에픽만
    set_num_dict2=Counter(list_setnum2) ##신화만
    
    result_all_list=[list11,list11_0,list11_1,list12,list13,list14,list15,list21,list21_0,list21_1,list22,list23,list31,list32,list33,list33_0,list33_1]
    result_setnum=[set_num_dict,set_num_dict1,set_num_dict2]
    return [result_all_list,result_setnum]

##공통
def make_setopt_num(equ_list,god_tg):
    set_list=["1"+str(equ_list[x][2:4]) for x in range(0,11)]
    set_val=Counter(set_list)
    for i in not_set_list:
        del set_val[i]
    setopt_num=sum([floor(x*0.7) for x in set_val.values()])+god_tg
    return [set_list,setopt_num]

def make_set_list(equ_list,set_list): 
    set_on=list(equ_list)
    setcount=set_list.count
    onecount=equ_list.count
    setapp=set_on.append
    for i in set_code_list:
        now_set=setcount(i)
        if now_set>1:
            setapp(i+str(floor(now_set*0.7)))
    if onecount('32390650')==1:
        if onecount('21390340')==1 or onecount('31390540')==1: setapp('1401')
    return tuple(set_on)

##딜러용
def hard_coding_dealer(base_array,betterang,for_calc,coolper,skiper):
    hard_coding=for_calc.count
    if hard_coding('1201')==1 and hard_coding('32200')==1:
        base_array[3]=base_array[3]-5
    if hard_coding('33200')==1 and hard_coding('31200')==0:
        base_array[8]=base_array[8]-10
    if hard_coding('33230')==1 or hard_coding('33231')==1:
        if hard_coding('31230')==0:
            base_array[4]=base_array[4]-10
        if hard_coding('32230')==0:
            base_array[9]=base_array[9]-40
    if hard_coding('15340')==1 or hard_coding('23340')==1 or hard_coding('33340')==1 or hard_coding('33341')==1:
        if hard_coding('1341')==0 and hard_coding('1342') ==0:
            if hard_coding('15340')==1:
                base_array[9]=base_array[9]-20
            elif hard_coding('23340')==1:
                base_array[2]=base_array[2]-10
            elif hard_coding('33340')==1:
                base_array[6]=base_array[6]-5
            else:
                base_array[9]=base_array[9]-4
                base_array[2]=base_array[2]-2
                base_array[6]=base_array[6]-1
                base_array[8]=base_array[8]-1.93
    if hard_coding('11111')==1:
        if hard_coding('1112')==1 or hard_coding('1113')==1:
            coolper=(1-(100-coolper)/100*(100-11)/100)*100
    if hard_coding('11301')==1:
        if hard_coding('22300')!=1:
            base_array[4]=base_array[4]-10
            base_array[7]=base_array[7]+10
        if hard_coding('31300')!=1:
            base_array[4]=base_array[4]-10
            base_array[7]=base_array[7]+10
    if hard_coding('11061')==1:
        if betterang ==34:
            if hard_coding('12060')==1:
                base_array[3]=base_array[3]+1
            if hard_coding('13060')==1:
                skiper=skiper/1.34*1.35
            if hard_coding('14060')==1:
                base_array[9]=base_array[9]+4
            if hard_coding('15060')==1:
                base_array[8]=base_array[8]+1
            if hard_coding('1063')==1:
                base_array[4]=base_array[4]+1
    if hard_coding('1441') ==1:
        if hard_coding('11440')!=1: ##3셋 공3% 모공5% 감소
            base_array[7]=base_array[7]-3
            base_array[6]=base_array[6]-5
    return [base_array,coolper,skiper]

def inv_auto_dealer(base_array,only_bon,inv2_on_tg,inv_type_list):
    inv1_val=10
    inv2_val=5
    qqq=0
    inv_opt_list=[base_array[2],base_array[3],base_array[4],base_array[6],base_array[7],base_array[8]]
    for i in [2,3,4,6,7,8]:
        if min(inv_opt_list)==base_array[i]:
            base_array[i]=base_array[i]+10
            inv1_opt=inv_type_list[qqq]
            if i==4: only_bon=only_bon+10
            break
        qqq=qqq+1
    if inv2_on_tg==1:
        qqq2=0
        inv_opt_list=[base_array[2],base_array[3],base_array[4],base_array[6],base_array[7],base_array[8]]
        for i in [2,3,4,6,7,8]:
            if min(inv_opt_list)==base_array[i]:
                base_array[i]=base_array[i]+5
                inv2_opt=inv_type_list[qqq2]
                if i==4: only_bon=only_bon+5
                break
            qqq2=qqq2+1
    else:
        inv2_opt="미충족";inv2_val=" X "
    return [base_array,only_bon,inv1_opt,inv2_opt,inv1_val,inv2_val]
