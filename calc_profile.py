import tkinter
import requests
import urllib.request
from urllib import parse
from json import loads
import json
from multiprocessing.pool import ThreadPool
import openpyxl
from collections import Counter
import numpy as np
from math import floor
import random

try:
    import calc_api_key
    apikey=calc_api_key.get_api_key()
except:
    try:
        api_txt_file=open("API_key.txt","r")
        apikey = api_txt_file.readline()
        if apikey=="":
            pass
        api_txt_file.close()
    except:
        pass

with open('skillDB/item_code_list.json','r', encoding='utf-8') as item_code_list:
    item_code_list=json.load(item_code_list)
with open('skillDB/opt_one.json','r', encoding='utf-8') as opt_one:
    opt_one=json.load(opt_one)
with open('skillDB/item_name_list.json','r', encoding='utf-8') as item_name_list:
    item_name_list=json.load(item_name_list)
with open('skillDB/opt_job.json','r', encoding='utf-8') as opt_job:
    opt_job=json.load(opt_job)
with open('skillDB/opt_job_ele.json','r', encoding='utf-8') as opt_job_ele:
    opt_job_ele=json.load(opt_job_ele)

with open('skillDB/pltDB.json','r', encoding='utf-8') as plt_json:
    plt_dict=json.load(plt_json)

def load_api2(URL):
    api_load=urllib.request.urlopen(URL)
    api_dic=loads(api_load.read().decode("utf-8"))
    return api_dic
def load_api(URL):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(load_api2, (URL,))
    api_dic = async_result.get()
    return api_dic

def make_profile(name,server):
    dark_knight_pas2=0
    server_dict={'안톤':'anton','바칼':'bakal','카인':'cain','카시야스':'casillas',
                '디레지에':'diregie','힐더':'hilder','프레이':'prey','시로코':'siroco'}
    try:
        sever_code=server_dict[server]
        cha_id_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters?characterName='+parse.quote(name)+'&apikey=' + apikey)
        cha_id=cha_id_dic['rows'][0]['characterId']
        down_url='https://img-api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'?zoom=1?apikey='+apikey
        urllib.request.urlretrieve(down_url,'my_cha.png')
    except:
        return {'error':'Not found'}
    else:
        stat_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/status?apikey=' + apikey)
        #print('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/equipment?apikey='+ apikey)
        equipment_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/equipment?apikey='+ apikey)
        avatar_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/avatar?apikey='+ apikey)
        pet_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/creature?apikey='+ apikey)
        gem_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/flag?apikey='+ apikey)
        talisman_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/equip/talisman?apikey='+ apikey)
        swiequ_dic=load_api('https://api.neople.co.kr/df/servers/'+sever_code+'/characters/'+cha_id+'/skill/buff/equip/equipment?apikey='+ apikey)

        adventure_name=swiequ_dic['adventureName']
        class_name=swiequ_dic['jobName']
        job_name=swiequ_dic['jobGrowName']
        if job_name=='세라핌' or  job_name=='헤카테':
            return {'error':'buffer'}
        job_id=swiequ_dic['jobId']
        job_calc_name=job_detail[class_name][job_name][6]
        if job_name[0]=='眞': job_calc_name=job_calc_name+'(진각)'
        else: job_calc_name=job_calc_name+'(2각)'
        now_ele=int(stat_dic["status"][27]["value"])
        no_enchant_ele=200
        try:
            swi_skillname=swiequ_dic['skill']['buff']['skillInfo']['name']
            swi_skilllvl=swiequ_dic['skill']['buff']['skillInfo']['option']['level']
            swiper_list=swiequ_dic['skill']['buff']['skillInfo']['option']['values']
        except TypeError as error:
            swi_skillname='채택안됨'
            swi_skilllvl='0'
            swiper_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        swiper_value=job_detail[class_name][job_name][0]-1
        max_swiper=job_detail[class_name][job_name][1]
        if class_name=='프리스트(남)' and job_name=='眞 크루세이더':
            if len(swiper_list)!=18:
                return {'error':'buffer'}
        ##1번 스위칭박스
        if job_name=='眞 베가본드':
            now_swiper=5*float(swiper_list[swiper_value])
            max_swiper=5*float(max_swiper)
            swi_score=(100+now_swiper)/(100+max_swiper)
            show_swi=str(round(now_swiper,1))+'% / '
        elif class_name=='격투가(남)' and job_name=='眞 넨마스터':
            now_swiele=int(swiper_list[1])
            max_ele_eff=((now_ele+86)*0.0045+1.05)/(now_ele*0.0045+1.05)
            now_ele_eff=((now_ele+now_swiele)*0.0045+1.05)/(now_ele*0.0045+1.05)
            now_swiper=float(swiper_list[swiper_value])
            swi_score=(100+now_swiper)/(100+max_swiper)*now_ele_eff/max_ele_eff
            show_swi=str(round(now_swiper,1))+'% / +'+str(int(now_swiele))+' / '
        elif class_name=='격투가(여)' and job_name=='眞 넨마스터':
            now_swiele=int(swiper_list[3])
            max_ele_eff=((now_ele+86)*0.0045+1.05)/(now_ele*0.0045+1.05)
            now_ele_eff=((now_ele+now_swiele)*0.0045+1.05)/(now_ele*0.0045+1.05)
            now_swiper=float(swiper_list[swiper_value])
            swi_score=(100+now_swiper)/(100+max_swiper)*now_ele_eff/max_ele_eff
            show_swi=str(round(now_swiper,1))+'% / +'+str(int(now_swiele))+' / '
        elif class_name=='격투가(여)' and job_name=='眞 스트리트 파이터':
            now_swiper=50+5.882352941176470588235294117647*float(swiper_list[swiper_value])/100
            swi_score=now_swiper/100
            show_swi=str(round(float(swiper_list[swiper_value]),1))+'% / '
        elif class_name=='프리스트(남)' and job_name=='眞 인파이터':
            max_swiper=max_swiper*1.5
            now_swiper=float(swiper_list[swiper_value])*1.5
            swi_score=(100+now_swiper)/(100+max_swiper)
            show_swi=str(round(now_swiper/1.5,1))+'% / '
        else:
            now_swiper=float(swiper_list[swiper_value])
            swi_score=(100+now_swiper)/(100+max_swiper)
            show_swi=str(round(now_swiper,1))+'% / '
        
            
        
        ##2번 스탯
        ear_score=0.99;patt_enchant=0;matt_enchant=0;iatt_enchant=0
        for now_equ in equipment_dic["equipment"]:
            if now_equ.get("slotName")=="무기":
                wep_name=now_equ.get("itemName")
                wep_type=now_equ.get("itemTypeDetail").replace(" ", "")
                wep_rein=str(now_equ.get("reinforce"))
                if wep_rein==None:
                    wep_rein='0'
                wep_refi=str(now_equ.get("refine"))
                if wep_refi==None:
                    wep_refi='0'
                if job_detail[class_name][job_name][2]==0:
                    if now_equ.get("remodelInfo")!=None:
                        wep_score=float(reinforce_eff['산물'][wep_rein])
                        wep_show=wep_rein+'개조'
                    else:
                        wep_score=float(reinforce_eff['무기'][wep_rein])
                        wep_show=wep_rein+'강'
                elif job_detail[class_name][job_name][2]==1:
                    if now_equ.get("remodelInfo")!=None:
                        wep_score=float(refine_eff['산물'][wep_rein])
                        wep_show=wep_rein+'개조'
                    else:
                        wep_score=float(refine_eff['무기'][wep_refi])
                        wep_show=wep_refi+'재련'
                if wep_name[0:5]=='검은 성전' or wep_name[0:6]=='흑천의 주인' or wep_name[5:11]=='흑천의 주인':
                    wep_score=wep_score-70/4800
            elif now_equ.get("slotName")=="귀걸이":
                ear_rein=str(now_equ.get("reinforce"))
                if ear_rein==None:
                    ear_rein='0'
                ear_score=float(reinforce_eff['귀걸이'][ear_rein])
        final_rein_score=(float(wep_score)-1)+(float(ear_score)-1)+1

        api_stat=0
        god_parts=['상의','팔찌','귀걸이']
        for now_equ in equipment_dic["equipment"]:
            if god_parts.count(now_equ.get("slotName"))!=0:
                if now_equ.get("mythologyInfo")!=None:
                    god_option=now_equ.get("mythologyInfo").get("options")
                    for now_opt in god_option:
                        if now_opt["explain"][0:5]=="힘, 지능" and list(now_opt["explain"]).count('%')==0:
                            god_stat=now_opt["explain"][6:];god_stat=god_stat[:-3]
                            api_stat=api_stat-int(god_stat)
        api_stat=api_stat+max([stat_dic["status"][2]["value"],stat_dic["status"][3]["value"]])
        max_stat=job_detail[class_name][job_name][3]
        stat_dif=api_stat-max_stat
        stat_score=1+stat_dif/100*0.0078
        if stat_dif > 0: stat_show=str(api_stat)+' (+'+str(stat_dif)+')'
        else: stat_show=str(api_stat)+' ('+str(stat_dif)+')'
        
    
        ##3번 속강
        fire_enchant=0;ice_enchant=0;light_enchant=0;dark_enchant=0;all_enchant=0;enchant_show='';
        ele_enchant_parts=['무기','칭호','목걸이','팔찌','반지','마법석']
        att_enchant_parts=['무기','상의','하의','보조장비']
        for now_equ in equipment_dic["equipment"]:
            if ele_enchant_parts.count(now_equ.get("slotName"))!=0:
                if now_equ.get("enchant")!=None:
                    try:
                        for i in range(len(now_equ.get("enchant").get("status"))):
                            if now_equ.get("enchant")['status'][i]["name"]=='화속성강화':
                                fire_enchant=fire_enchant+int(now_equ.get("enchant")['status'][i]["value"])
                            if now_equ.get("enchant")['status'][i]["name"]=='수속성강화':
                                ice_enchant=ice_enchant+int(now_equ.get("enchant")['status'][i]["value"])
                            if now_equ.get("enchant")['status'][i]["name"]=='명속성강화':
                                light_enchant=light_enchant+int(now_equ.get("enchant")['status'][i]["value"])
                            if now_equ.get("enchant")['status'][i]["name"]=='암속성강화':
                                dark_enchant=dark_enchant+int(now_equ.get("enchant")['status'][i]["value"])
                            if now_equ.get("enchant")['status'][i]["name"]=='모든 속성 강화':
                                all_enchant=all_enchant+int(now_equ.get("enchant")['status'][i]["value"])
                    except: pass
            if att_enchant_parts.count(now_equ.get("slotName"))!=0:
                if now_equ.get("enchant")!=None:
                    try:
                        for i in range(len(now_equ.get("enchant").get("status"))):
                            enchant_name=now_equ.get("enchant")['status'][i]["name"]
                            enchant_value=now_equ.get("enchant")['status'][i]["value"]
                            if enchant_name=='물리 공격력': patt_enchant=patt_enchant+enchant_value
                            if enchant_name=='마법 공격력': matt_enchant=matt_enchant+enchant_value
                            if enchant_name=='독립 공격력': iatt_enchant=iatt_enchant+enchant_value
                    except: pass
                                
        
        flag_slot=gem_dic.get("flag")
        if flag_slot!=None:
            gem_slot=flag_slot.get("gems")
            for now_gem in gem_slot:
                try:
                    if now_gem.get("itemName")=="희미하게 빛나는 젬[화속성강화]": fire_enchant=fire_enchant+1
                    if now_gem.get("itemName")=="희미하게 빛나는 젬[수속성강화]": ice_enchant=ice_enchant+1
                    if now_gem.get("itemName")=="희미하게 빛나는 젬[명속성강화]": light_enchant=light_enchant+1
                    if now_gem.get("itemName")=="희미하게 빛나는 젬[암속성강화]": dark_enchant=dark_enchant+1
                    if now_gem.get("itemName")=="은은하게 빛나는 젬[화속성강화]": fire_enchant=fire_enchant+3
                    if now_gem.get("itemName")=="은은하게 빛나는 젬[수속성강화]": ice_enchant=ice_enchant+3
                    if now_gem.get("itemName")=="은은하게 빛나는 젬[명속성강화]": light_enchant=light_enchant+3
                    if now_gem.get("itemName")=="은은하게 빛나는 젬[암속성강화]": dark_enchant=dark_enchant+3
                    if now_gem.get("itemName")=="눈부시게 빛나는 젬[화속성강화]": fire_enchant=fire_enchant+5
                    if now_gem.get("itemName")=="눈부시게 빛나는 젬[수속성강화]": ice_enchant=ice_enchant+5
                    if now_gem.get("itemName")=="눈부시게 빛나는 젬[명속성강화]": light_enchant=light_enchant+5
                    if now_gem.get("itemName")=="눈부시게 빛나는 젬[암속성강화]": dark_enchant=dark_enchant+5
                    if now_gem.get("itemName")=="영롱하게 빛나는 젬[화속성강화]": fire_enchant=fire_enchant+7
                    if now_gem.get("itemName")=="영롱하게 빛나는 젬[수속성강화]": ice_enchant=ice_enchant+7
                    if now_gem.get("itemName")=="영롱하게 빛나는 젬[명속성강화]": light_enchant=light_enchant+7
                    if now_gem.get("itemName")=="영롱하게 빛나는 젬[암속성강화]": dark_enchant=dark_enchant+7
                except: pass

        avatar_list=avatar_dic.get("avatar")
        for i in range(len(avatar_list)):
            if avatar_list[i].get("slotId")=="AURORA":
                aura_name=avatar_list[i].get("itemName")
                aura_ID=avatar_list[i].get("itemId")
                aura_opt_list=load_api('https://api.neople.co.kr/df/items/'+aura_ID+'?apikey=' + apikey).get("itemStatus")
                for now_opt in aura_opt_list:
                    if now_opt["name"]=='화속성강화': fire_enchant=fire_enchant+int(now_opt["value"]/1.2)
                    if now_opt["name"]=='수속성강화': ice_enchant=ice_enchant+int(now_opt["value"]/1.2)
                    if now_opt["name"]=='명속성강화': light_enchant=light_enchant+int(now_opt["value"]/1.2)
                    if now_opt["name"]=='암속성강화': dark_enchant=dark_enchant+int(now_opt["value"]/1.2)
                    if now_opt["name"]=='모든 속성 강화': all_enchant=all_enchant+int(now_opt["value"]/1.2)
                    if now_opt["name"]=='물리 공격력': patt_enchant=patt_enchant+int(now_opt["value"]/1.11)
                    if now_opt["name"]=='마법 공격력': matt_enchant=matt_enchant+int(now_opt["value"]/1.11)
                    if now_opt["name"]=='독립 공격력': iatt_enchant=iatt_enchant+int(now_opt["value"]/1.11)
                    
        
        fire_enchant=fire_enchant+all_enchant
        ice_enchant=ice_enchant+all_enchant
        light_enchant=light_enchant+all_enchant
        dark_enchant=dark_enchant+all_enchant
        final_enchant=max(fire_enchant,ice_enchant,light_enchant,dark_enchant)
        if final_enchant==fire_enchant: enchant_show=enchant_show+'화';main_ele='화'
        if final_enchant==ice_enchant: enchant_show=enchant_show+'수';main_ele='수'
        if final_enchant==light_enchant: enchant_show=enchant_show+'명';main_ele='명'
        if final_enchant==dark_enchant: enchant_show=enchant_show+'암';main_ele='암'
        if final_enchant==all_enchant: enchant_show='모';main_ele='모'
        enchant_show=enchant_show+'속작'
        enchant_score=((no_enchant_ele+final_enchant)*0.0045+1.05)/((no_enchant_ele+158)*0.0045+1.05) ##no_enchant_ele=200

        if final_enchant==158: enchant_rank='S' # 15 30 30 30 20 6 / 20 7
        elif final_enchant>=158-23: enchant_rank='A' # 12 25 25 25 15 6 / 20 7
        elif final_enchant>=158-32: enchant_rank='B' # 12 23 23 23 15 3 / 20 7
        elif final_enchant>=158-48: enchant_rank='C' # 10 20 20 20 12 3 / 20 5
        else: enchant_rank='D'


        ##4번 패시브 레벨링작/스킬칭호 분석
        eff_list=[]
        plt_now=plt_dict[job_calc_name[:-4]]
        plt_now_dict={}
        plt_for_title=[]
        for i in range(len(plt_now)):
            temp_eff=1/(1+2*float(plt_now[i]["up_value"]))
            if plt_now[i]["tier"]=='1': plt_for_title.append(plt_now[i]["name"])
            eff_list.append(temp_eff)
            plt_now_dict[plt_now[i]["name"]]=[float(plt_now[i]["up_value"]),plt_now[i]["tier"],plt_now[i]["reqlvl"]]
        plt_score=min(eff_list)
        if job_calc_name[:-4]=='패황': plt_for_title.append('화염의 각')
        if job_calc_name[:-4]=='마제스티':
            if wep_type=='소검':
                plt_score=1/(1+2*0.018996786042240643);del plt_now_dict['견고의 대검 마스터리'],plt_now_dict['파쇄의 둔기 마스터리'],plt_now_dict['쾌속의 도 마스터리']
            elif wep_type=='둔기':
                plt_score=1/(1+2*0.01908396946564883);del plt_now_dict['견고의 대검 마스터리'],plt_now_dict['쾌속의 도 마스터리'],plt_now_dict['속성의 소검 마스터리']
            elif wep_type=='도':
                plt_score=1/(1+2*0.01911288457089988);del plt_now_dict['견고의 대검 마스터리'],plt_now_dict['파쇄의 둔기 마스터리'],plt_now_dict['속성의 소검 마스터리']
            elif wep_type=='대검':
                del plt_now_dict['쾌속의 도 마스터리'],plt_now_dict['파쇄의 둔기 마스터리'],plt_now_dict['속성의 소검 마스터리']
        elif job_calc_name[:-4]=='알키오네':
            if wep_type=='쌍검':
                del plt_now_dict['단검 마스터리']
            elif wep_type=='단검':
                plt_score=1/(1+2*0.02208466696783562);del plt_now_dict['쌍검 마스터리']
        elif job_calc_name[:-4]=='다크나이트':
            if wep_type=='소검':
                plt_score=1/(1+2*0.00929235167977116)
                del plt_now_dict['어둠의 대검 마스터리'],plt_now_dict['어둠의 광검 마스터리'],plt_now_dict['어둠의 둔기 마스터리'],plt_now_dict['어둠의 도 마스터리']
            elif wep_type=='둔기':
                plt_score=1/(1+2*0.008746355685131268)
                del plt_now_dict['어둠의 대검 마스터리'],plt_now_dict['어둠의 광검 마스터리'],plt_now_dict['어둠의 소검 마스터리'],plt_now_dict['어둠의 도 마스터리']
            elif wep_type=='도':
                plt_score=1/(1+2*0.008746355685131268)
                del plt_now_dict['어둠의 대검 마스터리'],plt_now_dict['어둠의 광검 마스터리'],plt_now_dict['어둠의 둔기 마스터리'],plt_now_dict['어둠의 소검 마스터리']
            elif wep_type=='대검':
                plt_score=1/(1+2*0.008746355685131268)
                del plt_now_dict['어둠의 소검 마스터리'],plt_now_dict['어둠의 광검 마스터리'],plt_now_dict['어둠의 둔기 마스터리'],plt_now_dict['어둠의 도 마스터리']
            elif wep_type=='광검':
                plt_score=1/(1+2*0.009845288326300938)
                del plt_now_dict['어둠의 대검 마스터리'],plt_now_dict['어둠의 소검 마스터리'],plt_now_dict['어둠의 둔기 마스터리'],plt_now_dict['어둠의 도 마스터리']
        plt_list=list(plt_now_dict.keys())

        
        title_up=0;plt_name_list=['없음','없음'];tgtg=0
        passive_list=job_detail[class_name][job_name][4]
        passive_up=job_detail[class_name][job_name][5]
        plt_score_up=0;enchant_bonus=1
        for now_equ in equipment_dic["equipment"]:
            if now_equ.get("slotName")=="칭호":
                if now_equ.get("enchant")!=None:
                    if now_equ.get("enchant").get("reinforceSkill")!=None:
                        skill_name=now_equ["enchant"]["reinforceSkill"][0]["skills"][0]["name"]
                        skill_up=now_equ["enchant"]["reinforceSkill"][0]["skills"][0]["value"]
                        if plt_for_title.count(skill_name)!=0 and skill_up==2:
                            title_in="스킬칭호"
                            title_up=passive_up
                            enchant_bonus=1.0102505694760821 ## 속강 6 보정해주는거임
                            enchant_score=enchant_score*enchant_bonus
                            
        avatar_list=avatar_dic.get("avatar")
        plt_rank_list=['D','D']
        for i in range(len(avatar_list)):
            if avatar_list[i].get("slotId")=="JACKET" or avatar_list[i].get("slotId")=="PANTS":
                try:
                    for now_emb in avatar_list[i].get("emblems"):
                        if now_emb.get("slotColor")=="플래티넘" and now_emb.get("itemRarity")=="레전더리":
                            plt_name_list[tgtg]=now_emb.get("itemName")[9:-1]
                            if plt_list.count(plt_name_list[tgtg])==1:
                                plt_score_up=plt_score_up+plt_now_dict[plt_name_list[tgtg]][0]
                                if plt_now_dict[plt_name_list[tgtg]][1]=='1':
                                    plt_rank_list[tgtg]='S'
                                elif plt_now_dict[plt_name_list[tgtg]][1]=='2':
                                    plt_rank_list[tgtg]='A'
                                else:
                                    plt_rank_list[tgtg]='B'
                            else:
                                plt_score_up=plt_score_up+0.005
                                plt_rank_list[tgtg]='B'
                        elif now_emb.get("slotColor")=="플래티넘" and now_emb.get("itemRarity")=="언커먼":
                            plt_name_list[tgtg]='언커먼'
                            plt_rank_list[tgtg]='C'
                except: pass
                if job_calc_name[:-4]=='다크나이트':
                    if avatar_list[i].get("optionAbility")=="차원일치 스킬Lv +1":
                        dark_knight_pas2+=1
                tgtg+=1
                
        plt_score=plt_score*(1+plt_score_up)
        plt_rank_str=''.join(plt_rank_list)
        if plt_rank_str=='SS': plt_rank='S'
        elif plt_rank_str=='SA' or plt_rank_str=='AS' or plt_rank_str=='AA': plt_rank='A'
        elif plt_rank_str=='BA' or plt_rank_str=='AB' or plt_rank_str=='BB': plt_rank='B'
        elif plt_rank_str=='BC' or plt_rank_str=='CB' or plt_rank_str=='CC': plt_rank='C'
        else: plt_rank='D'
        
        ##5번 룬/탈리스만
        cha_tal=['없음','없음'];ttgg=0
        tal_score=1/1.03/1.03;rune_score=1/1.003/1.003/1.003/1.003/1.003/1.003
        tal_rarity=['C','C'];rune_rarity=['C','C','C','C','C','C'];ttgg2=0
        talisman_list=talisman_dic.get("talismans")
        if talisman_list!=None:
            for now_tal in talisman_list:
                try:
                    cha_tal[ttgg]=now_tal.get("talisman").get("itemName")
                    if cha_tal[ttgg][0:3]=='갈라진':
                        tal_rarity[ttgg]='B'
                    elif cha_tal[ttgg][0:3]=='온전한':
                        tal_score=tal_score*1.02
                        tal_rarity[ttgg]='A'
                    else:
                        tal_score=tal_score*1.03
                        tal_rarity[ttgg]='S'
                    for k in range(0,3):
                        try:
                            if now_tal.get("runes")[k].get("itemName")[0:3]=='선명한': rune_score=rune_score*1.003;rune_rarity[ttgg2]='S'
                            if now_tal.get("runes")[k].get("itemName")[0:3]=='빛바랜': rune_score=rune_score*1.002;rune_rarity[ttgg2]='A'
                            if now_tal.get("runes")[k].get("itemName")[0:3]=='갈라진': rune_score=rune_score*1.001;rune_rarity[ttgg2]='B'
                        except:pass
                        ttgg2=ttgg2+1
                    ttgg=ttgg+1
                except: pass
        if rune_rarity.count('S')>=4: rune_score=1
        tal_score=tal_score*rune_score
        if tal_score==1: tal_rank='S'
        elif tal_score>=1/1.003/1.003/1.003/1.003/1.003/1.003: tal_rank='A'
        elif tal_score>=1/1.003/1.003/1.003/1.003/1.003/1.003/1.03/1.03*1.02*1.02: tal_rank='B'
        elif tal_score>=1/1.003/1.003/1.003/1.003/1.003/1.003/1.03/1.03*1.02: tal_rank='C'
        else: tal_rank='D'
                
        att_enchant=max([patt_enchant,matt_enchant,iatt_enchant])
        att_score=(4800+att_enchant-245)/4800
        final_stat_score=stat_score*((final_rein_score-1)+(att_score-1)+1)

        
        ##계산 영역
        cha_equ=[];siroco_equ=['4']
        extra_dam=0;extra_cri=0;extra_bon=0;extra_all=0;extra_att=0;extra_sta=0;extra_pas2=0;extra_final=0
        fixed_dam=0;fixed_cri=0
        
        ele_skill=0
        ele_in=158+10+13
        betterang=34
        cool_eff=0.5
        job_lv1=opt_job[job_calc_name][11]
        job_lv2=opt_job[job_calc_name][12]
        job_lv3=opt_job[job_calc_name][13]
        job_lv4=opt_job[job_calc_name][14]
        job_lv5=opt_job[job_calc_name][15]
        job_lv6=opt_job[job_calc_name][16]
        job_pas0=opt_job[job_calc_name][0]
        job_pas1=opt_job[job_calc_name][1]
        job_pas2=opt_job[job_calc_name][2]
        job_pas3=opt_job[job_calc_name][3]

        job_ult1=opt_job[job_calc_name][17]
        job_ult2=opt_job[job_calc_name][18]
        job_ult3=opt_job[job_calc_name][19]

        if job_calc_name[-4:] == "(진각)":
            silmari=0
            active_eff_one=15
            active_eff_set=15
        else:
            silmari=1
            active_eff_one=21
            active_eff_set=24

        ##템 리스트 만들기
        siroco_parts=['하의','반지','보조장비']
        wep_type='공통'
        for now_equ in equipment_dic["equipment"]:
            if now_equ.get("slotName")=='보조무기':
                continue
            now_code=item_code_list.get(now_equ.get("itemName"))
            if now_code==None: pass
            else: cha_equ.append(now_code)
            if now_equ.get("itemName")[0:5]=='원초의 꿈': cha_equ.append('111076')
            if siroco_parts.count(now_equ.get("slotName"))!=0:
                if now_equ.get("sirocoInfo")!=None:
                    now_siroco=item_code_list.get(now_equ.get("upgradeInfo").get("itemName"))
                    siroco_equ.append(now_siroco[3])
                else: siroco_equ.append('0')
        for now_equ in equipment_dic["equipment"]:
            if now_equ.get("slotName")=='무기':
                
                if now_equ.get("sirocoInfo")!=None:
                    smell1=now_equ["sirocoInfo"]["options"][0]["explain"]
                    smell2=now_equ["sirocoInfo"]["options"][1]["explain"]
                    
                    if smell1.split('%')[0][-1]=='0':
                        smell1_value=int(smell1.split('%')[0][-2]+smell1.split('%')[0][-1])
                    else: smell1_value=int(smell1.split('%')[0][-1])
                    smell2_value=int(smell2.split('%')[0][-1])
                    for i in range(len(smell1)):
                        if smell1[i:i+6]=='추가 데미지': smell1_opt='추뎀';extra_bon=extra_bon+smell1_value
                        elif smell1[i:i+7]=='크리티컬 공격': smell1_opt='크증';extra_cri=extra_cri+smell1_value
                        elif smell1[i:i+6]=='모든 공격력': smell1_opt='모공';extra_all=extra_all+smell1_value
                        elif smell1[i:i+5]=='힘, 지능': smell1_opt='스탯';extra_sta=extra_sta+smell1_value
                        elif smell1[i:i+6]=='물리, 마법': smell1_opt='공퍼';extra_att=extra_att+smell1_value
                        elif smell1[i:i+7]=='공격 시 데미': smell1_opt='증뎀';extra_dam=extra_dam+smell1_value
                    if siroco_equ.count('0')==0: smell2_tg=1
                    else: smell2_tg=0
                    for i in range(len(smell2)):
                        if smell2[i:i+6]=='추가 데미지': smell2_opt='추뎀';extra_bon=extra_bon+smell2_value*smell2_tg
                        elif smell2[i:i+7]=='크리티컬 공격': smell2_opt='크증';extra_cri=extra_cri+smell2_value*smell2_tg
                        elif smell2[i:i+6]=='모든 공격력': smell2_opt='모공';extra_all=extra_all+smell2_value*smell2_tg
                        elif smell2[i:i+5]=='힘, 지능': smell2_opt='스탯';extra_sta=extra_sta+smell2_value*smell2_tg
                        elif smell2[i:i+6]=='물리, 마법': smell2_opt='공퍼';extra_att=extra_att+smell2_value*smell2_tg
                        elif smell2[i:i+7]=='공격 시 데미': smell2_opt='증뎀';extra_dam=extra_dam+smell2_value*smell2_tg
        eleup_type=['화속성강화','수속성강화','명속성강화','암속성강화','모든 속성 강화']
        for now_equ in equipment_dic["equipment"]:
            if now_equ.get("slotName")=='칭호':
                title_id=now_equ.get("itemId")
                title_api=load_api('https://api.neople.co.kr/df/items/'+title_id+'?apikey=' + apikey)
                title_opt=title_api.get("itemExplain")
                if title_opt[0:15]=='공격 시 데미지 10% 증가': fixed_dam=10
                elif title_opt[0:15]=='공격 시 데미지 15% 증가': fixed_dam=15
                elif title_opt[0:20]=='크리티컬 공격 시 데미지 10% 증가': fixed_cri=10
                elif title_opt[0:14]=='공격 시 10% 추가데미지': extra_bon=extra_bon+10
                title_opt2=title_api.get("itemStatus")
                if len(title_opt2)!=0:
                    for now_opt in title_opt2:
                        if eleup_type.count(now_opt.get("name"))!=0:
                            ele_in=ele_in+now_opt.get("value")
                            if now_opt.get("value")==27:
                                ele_in=ele_in+5
                            break
        pet_info=pet_dic.get("creature")
        try:
            per_name=pet_info["itemName"]
            if per_name=='서퍼 웰시코기': extra_all=extra_all+15
            elif per_name=='강인한 이그니스': extra_final=extra_final+10.7
            elif per_name=='명석한 아쿠아젤로': extra_final=extra_final+10.7
            elif per_name=='명석한 루메누스': extra_final=extra_final+10.7
            elif per_name=='강인한 테네브리스': extra_final=extra_final+10.7
            elif per_name=='초열의 주술사 미호': extra_final=extra_final+10.7
            elif per_name=='빙설의 마법사 루나': extra_final=extra_final+10.7
            elif per_name=='고대의 용사 리처드': extra_final=extra_final+10.7
            elif per_name=='SD 팩': extra_final=extra_final+10.7
            elif per_name=='쁘띠 바스테트': extra_final=extra_final+10.7
            elif per_name=='쁘띠 샴': extra_final=extra_final+10.7
            elif per_name=='SD 프레이-이시스': extra_att=extra_att+18;extra_pas2=extra_pas2+1
            elif per_name=='SD 이시스-프레이': extra_att=extra_att+18;extra_pas2=extra_pas2+1
            elif per_name=='뇌광의 사수 빅토리아': extra_att=extra_att+18;extra_pas2=extra_pas2+1
            elif per_name=='폭풍을 부르는 성녀 글로리아': extra_att=extra_att+18;extra_pas2=extra_pas2+1
            elif per_name[-5:]=='[노련한]': fixed_cri=18;extra_pas2=extra_pas2+1
            elif per_name[-5:]=='[강인한]': extra_all=extra_all+15
        except: pass
        
        equ_exist=[];wep_exist=0
        for i in cha_equ:
            if len(i)!=6:
                equ_exist.append(i[0:2])
            elif len(i)==6:
                wep_exist=1
        if cha_equ.count('11410130')==1:
            for code in ['12','13','14','15']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'410');equ_exist.append(code)
        if cha_equ.count('21420130')==1:
            for code in ['22','23']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'420');equ_exist.append(code)
        if cha_equ.count('33430130')==1:
            for code in ['31','32']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'430');equ_exist.append(code)
        if cha_equ.count('11440')==1:
            for code in ['12','13','14','15']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'440');equ_exist.append(code)
        if cha_equ.count('21450')==1:
            for code in ['22','23']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'450');equ_exist.append(code)
        if cha_equ.count('33460')==1:
            for code in ['31','32']:
                if equ_exist.count(code)==0:
                    cha_equ.append(code+'460');equ_exist.append(code)

        for code in ['11','12','13','14','15']:
            if equ_exist.count(code)==0: cha_equ.append(code+'360')
        for code in ['21','22','23']:
            if equ_exist.count(code)==0: cha_equ.append(code+'370')
        for code in ['31','32','33']:
            if equ_exist.count(code)==0: cha_equ.append(code+'380')
        if wep_exist==0:
            wep_name='검은 성전/흑천'
            cha_equ.append('111001')
        if len(siroco_equ)!=4:
            siroco_equ=['4','0','0','0']
        cha_equ.append(''.join(siroco_equ))
        #### 계산 시작#####        
        getone=opt_one.get
        set_list=[]
        for item in cha_equ:
            if len(item)!=6 and len(item)!=4: set_list.append('1'+item[2:4])
        set_val=Counter(set_list)
        del set_val['136'],set_val['137'],set_val['138'],set_val['144'],set_val['145'],set_val['146'],set_val['147'],set_val['148'],set_val['149']
        setopt_num=sum([floor(x*0.7) for x in set_val.values()])
        set_on=[];setapp=set_on.append
        setcount=set_list.count
        set_oncount=set_on.count
        onecount=cha_equ.count
        for i in range(101,136):
            if setcount(str(i))==2:
                setapp(str(i)+"1")
            if 4>=setcount(str(i))>=3:
                setapp(str(i)+"2")
            if setcount(str(i))==5:
                setapp(str(i)+"3")
        for i in range(141,144):
            if setcount(str(i))==2:
                setapp(str(i)+"1")
            if 4>=setcount(str(i))>=3:
                setapp(str(i)+"2")
            if setcount(str(i))==5:
                setapp(str(i)+"3")
        for i in range(136,139):
            if setcount(str(i))==2:
                setapp(str(i)+"0")
            if 4>=setcount(str(i))>=3:
                setapp(str(i)+"1")
            if setcount(str(i))==5:
                setapp(str(i)+"2")
        for i in range(144,150):
            if setcount(str(i))==2:
                setapp(str(i)+"0")
            if 4>=setcount(str(i))>=3:
                setapp(str(i)+"1")
            if setcount(str(i))==5:
                setapp(str(i)+"2")
        base_array=np.array([0,0,extra_dam,extra_cri,extra_bon,0,extra_all,extra_att,extra_sta,ele_in,0,1,0,0,0,0,0,0,extra_pas2,0,0,0,0,0,0,0,0,0])
        ult_1=0;ult_2=0;ult_3=0;ult_skiper=0
        skiper=0
        coolper=0
        for_calc=set_on+cha_equ
        oneone=len(for_calc)
        oneonelist=[]
        max_damper=fixed_dam
        max_criper=fixed_cri
        for i in range(oneone):
            no_cut=getone(for_calc[i])               ## 11번 스증
            cut=np.array(no_cut[0:20]+no_cut[22:23]+no_cut[34:35]+no_cut[38:44])
            skiper=(skiper/100+1)*(cut[11]/100+1)*100-100
            coolper=(1-(100-coolper)/100*(100-cut[20])/100)*100
            max_damper=max([no_cut[44],max_damper])
            max_criper=max([no_cut[45],max_criper])
            ult_1=(no_cut[46]/100+1)*(ult_1/100+1)*100-100
            ult_2=(no_cut[47]/100+1)*(ult_2/100+1)*100-100
            ult_3=(no_cut[48]/100+1)*(ult_3/100+1)*100-100
            oneonelist.append(cut)
        for i in range(oneone):
            base_array=base_array+oneonelist[i]
        if set_oncount('1201')==1 and onecount('32200')==1:
            base_array[3]=base_array[3]-5
        if onecount('33200')==1 and onecount('31200')==0:
            base_array[8]=base_array[8]-10
        if onecount('33230')==1 or onecount('33231')==1:
            if onecount('31230')==0:
                base_array[4]=base_array[4]-10
            if onecount('32230')==0:
                base_array[9]=base_array[9]-40
        if onecount('15340')==1 or onecount('23340')==1 or onecount('33340')==1 or onecount('33341')==1:
            if set_oncount('1341')==0 and set_oncount('1342') ==0:
                if onecount('15340')==1:
                    base_array[9]=base_array[9]-20
                elif onecount('23340')==1:
                    base_array[2]=base_array[2]-10
                elif onecount('33340')==1:
                    base_array[6]=base_array[6]-5
                else:
                    base_array[9]=base_array[9]-4
                    base_array[2]=base_array[2]-2
                    base_array[6]=base_array[6]-1
                    base_array[8]=base_array[8]-1.93
        if onecount('11111')==1:
            if set_oncount('1112')==1 or set_oncount('1113')==1:
                coolper=(1-(100-coolper)/100*(100-11)/100)*100
        if onecount('11301')==1:
            if onecount('22300')!=1:
                base_array[4]=base_array[4]-10
                base_array[7]=base_array[7]+10
            if onecount('31300')!=1:
                base_array[4]=base_array[4]-10
                base_array[7]=base_array[7]+10
        if onecount('11061')==1:
            if betterang ==34:
                if onecount('12060')==1:
                    base_array[3]=base_array[3]+1
                if onecount('13060')==1:
                    skiper=skiper/1.34*1.35
                if onecount('14060')==1:
                    base_array[9]=base_array[9]+4
                if onecount('15060')==1:
                    base_array[8]=base_array[8]+1
                if set_oncount('1063')==1:
                    base_array[4]=base_array[4]+1
        if set_oncount('1441') ==1:
            if onecount('11440')!=1: ##3셋 공3% 모공5% 감소
                base_array[7]=base_array[7]-3
                base_array[6]=base_array[6]-5
        if onecount('13150')==1:  ## 대자연 속강 감지
            if main_ele!='화':base_array[9]=base_array[9]-24
        if onecount('12150')==1:
            if main_ele=='암':base_array[9]=base_array[9]+24
        if onecount('14150')==1:
            if main_ele=='수':base_array[9]=base_array[9]+24
        if onecount('15150')==1:
            if main_ele=='명':base_array[9]=base_array[9]+24
        if main_ele=='모':
            for nature in ['13150','12150','14150','15150']:
                if onecount('13150')!=1:
                    if onecount(nature)==1:
                        base_array[9]=base_array[9]+24
                        break
        if onecount('32390650')==1:
            if onecount('21390340')==1:
                base_array[5]=base_array[5]+7
            elif onecount('31390540')==1:
                base_array[5]=base_array[5]+7
        
        base_array[11]=skiper
        base_array[2]=max_damper+base_array[2]
        base_array[3]=max_criper+base_array[3]
        only_bon=base_array[4]
        base_array[4]=base_array[4]+base_array[5]*(base_array[9]*0.0045+1.05)
        actlvl=((base_array[active_eff_one]+base_array[22]*job_lv1+base_array[23]*job_lv2+base_array[24]*job_lv3+
                base_array[25]*job_lv4+base_array[26]*job_lv5+base_array[27]*job_lv6)/100+1)
        paslvl=((100+base_array[16]*job_pas0)/100)*((100+base_array[17]*job_pas1)/100)*((100+base_array[18]*job_pas2)/100)*((100+base_array[19]*job_pas3)/100)*(title_up/100+1)
        
        if ult_2 !=0:
            ult1_per=job_ult1*(1+base_array[23]*0.0653)/actlvl*(ult_1/100)
            ult2_per=job_ult2*(1+(base_array[25]*0.1203+0.04348*base_array[27]*silmari))/actlvl*(ult_2/100)
            ult3_per=job_ult3*(1+base_array[27]*0.1883)/actlvl*(ult_3/100)
            ult_skiper=(ult1_per+ult2_per+ult3_per)*100
        real_bon_not_ele=only_bon+base_array[5]*((base_array[9]-int(ele_skill))*0.0045+1.05)  
        damage=((base_array[2]/100+1)*(base_array[3]/100+1)*(base_array[4]/100+1)*(base_array[6]/100+1)*(base_array[7]/100+1)*
                (base_array[8]/100+1)*(base_array[9]*0.0045+1.05)*(base_array[10]/100+1)*(skiper/100+1)*
                paslvl*((54500+3.31*base_array[0])/54500)*((4800+base_array[1])/4800)/(1.05+0.0045*int(ele_skill)))*(1+extra_final/100)
        final_damage=damage*((base_array[12]+(actlvl-1)*100+ult_skiper)/100+1)
        final_damage_cool=final_damage*((100/(100-coolper)-1)*cool_eff+1)

        if job_calc_name[:-4]=='다크나이트': ## 닼나 특수식
            base_array[18]=base_array[18]+dark_knight_pas2
            for pas2_in_dungeon in ['15320','23170','23330','1102','1103','1212','1282','1282']:
                if onecount(pas2_in_dungeon)==1 or set_oncount(pas2_in_dungeon)==1:
                    base_array[18]=base_array[18]-1
                   
            api_stat=int(api_stat/(1.22+0.02*base_array[18]))
            stat_dif=api_stat-max_stat
            stat_score=1+stat_dif/100*0.0078
            if stat_dif > 0: stat_show=str(api_stat)+' (+'+str(stat_dif)+')'
            else: stat_show=str(api_stat)+' ('+str(stat_dif)+')'
            final_stat_score=stat_score*final_rein_score*att_score
            
        final_score=swi_score*final_stat_score*enchant_score*plt_score*tal_score
        str_result=(name+' / '+class_name+' / '+job_name+'\n'
                    '스위칭 점수= '+swi_skillname+' ('+show_swi+str(swi_skilllvl)+'렙)'+' ['+str(round(swi_score*100,2))+' %]\n'
                    '스탯 점수= '+wep_show+' (마부-'+str(int(245-att_enchant))+') / '+stat_show+' ['+str(round(final_stat_score*100,2))+'%]\n'
                    '속강 점수= '+enchant_show+'+'+str(final_enchant)+' ['+str(round(enchant_score*100,2))+'%]\n'
                    '플티= '+plt_name_list[0]+' / '+plt_name_list[1]+' ['+str(round(plt_score*100,2))+'%]\n'
                    '탈리스만= '+cha_tal[0]+' / '+cha_tal[1]+' ['+str(round(tal_score*100,2))+'%]\n'
                    '총합 점수='+str(round(final_score*100,2))+'%')
        if swi_score>=1: swi_rank='S'
        elif swi_score>=0.986: swi_rank='A'
        elif swi_score>=0.971: swi_rank='B'
        elif swi_score>=0.95: swi_rank='C'
        else: swi_rank='D'

        
        
        if final_stat_score>=1: stat_rank='S'
        elif final_stat_score>=0.97: stat_rank='A'
        elif final_stat_score>=0.94: stat_rank='B'
        elif final_stat_score>=0.91: stat_rank='C'
        else: stat_rank='D'
        #print(cha_equ)
        result_dict={'캐릭명':name,
                     '모험단':adventure_name,
                     '직업군':class_name,
                     '직업명':job_name,
                     '무기명':wep_name,
                     '무기강화':wep_show,
                     '스위칭':str(round(float(swi_score*100),1))+'%',
                     '스위칭랭크':swi_rank,
                     '스위칭상세':str(round(float(now_swiper),1))+'%',
                     '스위칭최대':str(round(float(max_swiper),1))+'%',
                     '스탯':str(round(float(final_stat_score*100),1))+'%',
                     '스탯상세':str(int(api_stat)),
                     '스탯랭크':stat_rank,
                     '속강':str(round(float(enchant_score*100),1))+'%',
                     '속강종류':main_ele,
                     '속강상세':str(int(final_enchant)),
                     '속강랭크':enchant_rank,
                     '플티명':plt_name_list,
                     '플티':str(round(float(plt_score*100),1))+'%',
                     '플티랭크':plt_rank,
                     '플티상세':plt_rank_list,
                     '탈리명':cha_tal,
                     '탈리':str(round(float(tal_score*100),1))+'%',
                     '탈리랭크':tal_rank,
                     '탈리상세':tal_rarity,
                     '룬상세':rune_rarity,
                     '종합점수':str(round(float(final_score*100),2))+'%',
                     '장비':cha_equ,
                     '장비딜':str(int(final_damage_cool*100))+'%',
                     '쿨감':str(round(float(coolper),1))+'%',}
        """
        for i in range(len(result_dict.keys())):
            print(list(result_dict.keys())[i]+' : '+str(result_dict[list(result_dict.keys())[i]]))
        """
        return [str_result,result_dict]

"""
0,1번: 스위칭박스
주의: 리스트상으론 전부 -1번씩 shift 해줘야함
2번: 0:강화,1:재련
3번: 노증 최고 마을스탯
4번:딜칭호 리스트, 5번:딜칭호 상승율
6번:계산기 상 직업명(2각명)
7번:선호딜플티 8번:패시브딜플티 9번 선호증가치
"""
job_detail={
    '귀검사(남)':{
        '眞 웨펀마스터':[2,82,0,4192,[''],6.66,'검신',[''],[''],3.57],
        '眞 버서커':[2,116,1,4067,[''],5.28,'블러드이블',[''],[''],2.73],
        '眞 소울브링어':[3,69,0,4144,[''],4.86,'다크로드',[''],[''],1.6],
        '眞 아수라':[6,58,1,4201,[''],4.38,'인다라천',[''],[''],3.01],
        '眞 검귀':[2,100,0,4056,[''],6.37,'악귀나찰',[''],[''],3.28]
        },
    '귀검사(여)':{
        '眞 소드마스터':[2,71,0,4189,[''],5.76,'마제스티',[''],[''],3.92],
        '眞 데몬슬레이어':[1,100,0,4013,[''],5.45,'디어사이드',[''],3.77],
        '眞 다크템플러':[1,65,0,4071,[''],5.08,'네메시스',[''],[''],3.51],
        '眞 베가본드':[3,25,0,4003,[''],9.09,'검제',[''],[''],6.45]  #5중첩
        },
    '격투가(남)':{
        '眞 스트라이커':[3,104,0,4163,['화염의 각'],6.77,'패황',[''],[''],2.5],
        '眞 스트리트파이터':[7,79,0,4002,[''],4.58,'명왕',[''],[''],3.15],
        '眞 그래플러':[2,108,0,4186,[''],6.31,'그랜드마스터',[''],[''],3.28],
        '眞 넨마스터':[3,43,0,4201,[''],5.15,'염황광풍제월',[''],[''],3.53] #2번 속강(86)도 있음
        },
    '격투가(여)':{
        '眞 넨마스터':[3,57,0,4126,[''],5.15,'염제폐월수화',[''],[''],3.51], #4번 속강(86)도 있음
        '眞 스트라이커':[4,113,0,4188,[''],6.44,'카이저',[''],[''],3.54],
        '眞 스트리트 파이터':[5,850,0,4127,[''],2.36,'용독문주',[''],[''],1.6], #독 바르기 공격력 변화율 (증가율이 아님,독비중 50% 기준 평균산출 필요)
        '眞 그래플러':[2,107,1,4095,[''],6.93,'얼티밋디바',[''],[''],3.57]
        },
    '거너(남)':{
        '眞 스핏파이어':[1,84,0,3926,[''],6.05,'커맨더',[''],[''],3.57],
        '眞 메카닉':[4,85,0,4084,[''],4.58,'프라임',[''],[''],3.15],
        '眞 런처':[3,95,0,4203,[''],7.54,'디스트로이어',[''],[''],5.14],
        '眞 레인저':[2,125,0,4144,[''],6.93,'레이븐',[''],[''],3.57]
        },
    '거너(여)':{
        '크림슨 로제':[2,125,0,3994,[''],6.93,'크림슨로제',[''],[''],3.57],
        '스톰 트루퍼':[3,95,0,4078,[''],7.54,'스톰트루퍼',[''],[''],5.14],
        '프레이야':[1,84,1,3941,[''],6.05,'프레이야',[''],[''],3.57],
        '옵티머스':[4,85,0,4084,[''],4.15,'옵티머스',[''],[''],2.73]
        },
    '마법사(남)':{
        '어센션':[2,85,1,4200,[''],5.84,'어센션',[''],[''],3.42],
        '아이올로스':[1,111,0,3977,[''],4.76,'아이올로스',[''],[''],3.3],
        '뱀파이어 로드':[2,97,0,4018,[''],7.21,'뱀파이어로드',[''],[''],3.64],
        '이터널':[2,80,0,4105,[''],5.73,'이터널',[''],[''],3.57],
        '오블리비언':[1,107,0,4100,[''],5.18,'오블리비언',[''],[''],3.33]
        },
    '마법사(여)':{
        '지니위즈':[2,92,1,4056,[''],6.11,'지니위즈',[''],[''],3.57],
        '아슈타르테':[2,79,0,4283,[''],6.77,'아슈타르테',[''],[''],3.33],
        '오버마인드':[5,85,0,4193,[''],4.46,'오버마인드',[''],[''],3.07],
        '이클립스':[2,79,0,4076,[''],6.23,'이클립스',[''],[''],3.42],
        '헤카테':[0,0,1,4060,[''],0,'(버프)헤카테',[''],[''],0] # 조회 불가 직업
        },
    '프리스트(남)':{
        '眞 퇴마사':[2,76,0,4079,[''],3.43,'태을선인',[''],[''],2.35],
        '眞 어벤저':[1,90,0,4048,[''],6.47,'이모탈',[''],[''],4.51],
        '眞 인파이터':[2,66,0,4073,[''],6.14,'저스티스',[''],[''],3.24], #api의 1.5배가 실적용 수치
        '眞 크루세이더':[2,97,1,3906,[''],5.06,'세인트',[''],[''],3.42] # 배크만 조회가능, 리스트 갯수 18번까지 있음
        },
    '프리스트(여)':{
        '세라핌':[0,0,1,4093,[''],0,'(버프)세라핌',[''],[''],0], # 조회 불가 직업
        '인페르노':[3,93,0,4064,[''],7.76,'인페르노',[''],[''],4.14],
        '천선낭랑':[1,108,0,4167,[''],6.61,'천선낭랑',[''],[''],3.33],
        '리디머':[12,87.5,0,4098,[''],6.95,'리디머',[''],[''],3.57] # 시너지 (투기에 가득찬 분노)
        },
    '도적':{
        '그림리퍼':[3,103,0,4302,[''],6.77,'그림리퍼',[''],[''],3.77],
        '시라누이':[2,104,0,4133,[''],5.66,'시라누이',[''],[''],3.92],
        '타나토스':[1,114,0,4047,[''],2.91,'타나토스',[''],[''],2.57],
        '알키오네':[2,77,0,4235,[''],7.39,'알키오네',[''],[''],4.88]
        },
    '나이트':{
        '세이비어':[2,89,0,4147,[''],6.95,'세이비어',[''],[''],3.57],
        '드레드노트':[2,85,1,4142,[''],5.17,'드레드노트',[''],[''],3.57],
        '가이아':[2,102,0,3956,[''],4.41,'가이아',[''],[''],3.08],
        '마신':[3,100,1,4001,[''],6.39,'마신',[''],[''],3.57]
        },
    '다크나이트':{
        '자각2':[2,54,0,4019,[''],2.74,'다크나이트',[''],[''],1.86]
        },
    '크리에이터':{
        '자각2':[1,66,1,4089,[''],6.89,'크리에이터',[''],[''],3.77]
        },
    '마창사':{
        '제노사이더':[2,85,0,4071,[''],6.52,'제노사이더',[''],[''],3.15],
        '에레보스':[2,93,0,4187,[''],5.32,'에레보스',[''],[''],3.28],
        '듀란달':[1,100,0,4055,[''],4.96,'듀란달',[''],[''],3.42],
        '워로드':[2,80,0,4183,[''],6.01,'워로드',[''],[''],4.16]
        },
    '총검사':{
        '언터처블':[2,100,0,3988,[''],5.66,'언터처블',[''],[''],3.92],
        '갓파더':[2,85,0,4056,[''],4.58,'갓파더',[''],[''],3.15],
        '패스파인더':[2,100,0,4182,[''],6.35,'패스파인더',[''],[''],3.2],
        '레퀴엠':[2,100,0,4123,[''],6.57,'레퀴엠',[''],[''],3.42]
        }
    }
"""
for i in list(job_detail.keys()):
    for j in list(job_detail[i].keys()):
        print(j)
        print('최선플티')
        print(job_detail[i][j][7])
        print('차선플티')
        print(job_detail[i][j][8])
        print('')
"""
reinforce_eff={
    '무기':{
        '0':'0.823333333333333',
        '1':'0.828958333333333',
        '2':'0.834583333333333',
        '3':'0.840416666666667',
        '4':'0.845625',
        '5':'0.85125',
        '6':'0.857083333333333',
        '7':'0.862708333333333',
        '8':'0.87625',
        '9':'0.893333333333333',
        '10':'0.913333333333333',
        '11':'0.953125',
        '12':'1',
        '13':'1.03020833333333',
        '14':'1.06041666666667',
        '15':'1.09041666666667',
        '16':'1.12041666666667',
        '17':'1.15',
        '18':'1.179375',
        '19':'1.20854166666667',
        '20':'1.2375'
        },
    '귀걸이':{
        '0':'0.99',
        '1':'0.990625',
        '2':'0.99125',
        '3':'0.991875',
        '4':'0.992291666666667',
        '5':'0.992916666666667',
        '6':'0.99375',
        '7':'0.994375',
        '8':'0.995833333333333',
        '9':'0.997708333333333',
        '10':'1',
        '11':'1.004375',
        '12':'1.00958333333333',
        '13':'1.01291666666667',
        '14':'1.01625',
        '15':'1.01958333333333',
        '16':'1.02291666666667',
        '17':'1.02625',
        '18':'1.029375',
        '19':'1.03270833333333',
        '20':'1.03583333333333'
        },
    '산물':{
        '0':'0.802083333333333',
        '1':'0.841422833333333',
        '2':'0.88088425',
        '3':'0.920467583333333',
        '4':'0.960172833333333',
        '5':'1.0',
        '6':'1.03994908333333‬',
        '7':'1.08002008333333‬',
        '8':'1.120213'
        }
    }
refine_eff={
    '무기':{
        '0':'0.8925',
        '1':'0.901041666666667',
        '2':'0.905208333333333',
        '3':'0.909583333333333',
        '4':'0.918333333333333',
        '5':'0.926875',
        '6':'0.948333333333333',
        '7':'0.97',
        '8':'1'
        },
    '산물':{
        '0':'0.880208333333333',
        '1':'0.904019083333333‬',
        '2':'0.927903625',
        '3':'0.9518619583333',
        '4':'0.9758940833333‬',
        '5':'1.0',
        '6':'1.024179708',
        '7':'1.048433208‬',
        '8':'1.0727605'
        }
    }
