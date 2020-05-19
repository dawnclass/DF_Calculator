
def making_cases(case_list,god,mode):
    ##모드
    ##1: 표준533
    ##2: 표준3332
    ##3: 상의변형2333
    ##4: 하의변형3233
    ##5: 신발변형3323
    ##6: 32/33

    #신화
    #0:없음
    #1:상의
    #2:팔찌
    #3:귀걸이
    result_list=[]
    
    if mode==1: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) <116:
                        set_type_list=['11','12','13','14','15']
                    elif int(j) <120:
                        set_type_list=['21','22','23']
                    elif int(j) <124:
                        set_type_list=['31','32','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) <116:
                        set_type_list=['12','13','14','15']
                        temp_make.append('11'+str(j)[1:3]+'1')
                    elif int(j) <120:
                        set_type_list=['21','22','23']
                    elif int(j) <124:
                        set_type_list=['31','32','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) <116:
                        set_type_list=['11','12','13','14','15']
                    elif int(j) <120:
                        set_type_list=['22','23']
                        temp_make.append('21'+str(j)[1:3]+'1')
                    elif int(j) <124:
                        set_type_list=['31','32','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) <116:
                        set_type_list=['11','12','13','14','15']
                    elif int(j) <120:
                        set_type_list=['21','22','23']
                    elif int(j) <124:
                        set_type_list=['31','32']
                        temp_make.append('33'+str(j)[1:3]+'1')
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)


    elif mode==2: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                        temp_make.append('11'+str(j)[1:3]+'1')
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14']
                    elif int(j) <128:
                        set_type_list=['12','32']
                        temp_make.append('21'+str(j)[1:3]+'1')
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23']
                        temp_make.append('33'+str(j)[1:3]+'1')
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)


    elif mode==3: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['11','13','14']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14']
                        temp_make.append('11'+str(j)[1:3]+'1')
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['11','13','14']
                    elif int(j) <128:
                        set_type_list=['12','32']
                        temp_make.append('21'+str(j)[1:3]+'1')
                    elif int(j) <132:
                        set_type_list=['22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['11','13','14']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                    elif int(j) <136:
                        set_type_list=['15','23']
                        temp_make.append('33'+str(j)[1:3]+'1')
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)


    elif mode==4: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['12','13','14']
                    elif int(j) <128:
                        set_type_list=['21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['12','13','14']
                    elif int(j) <128:
                        set_type_list=['21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                        temp_make.append('11'+str(j)[1:3]+'1')
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['12','13','14']
                    elif int(j) <128:
                        set_type_list=['32']
                        temp_make.append('21'+str(j)[1:3]+'1')
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['12','13','14']
                    elif int(j) <128:
                        set_type_list=['21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['15','23']
                        temp_make.append('33'+str(j)[1:3]+'1')
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)


    elif mode==5: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14','15']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14','15']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['22','31']
                        temp_make.append('11'+str(j)[1:3]+'1')
                    elif int(j) <136:
                        set_type_list=['23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14','15']
                    elif int(j) <128:
                        set_type_list=['12','32']
                        temp_make.append('21'+str(j)[1:3]+'1')
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['23','33']
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if int(j) < 116:
                        set_type_list=['13','14','15']
                    elif int(j) <128:
                        set_type_list=['12','21','32']
                    elif int(j) <132:
                        set_type_list=['11','22','31']
                    elif int(j) <136:
                        set_type_list=['23']
                        temp_make.append('33'+str(j)[1:3]+'1')
                    for k in set_type_list:
                        temp_make.append(k+str(j)[1:3]+'0')
                result_list.append(temp_make)



    if mode==6: ################################################################################
        if god==0:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if len(j)==3:
                        if int(j) <116:
                            pass
                        elif int(j) <120:
                            set_type_list=['21','22','23']
                        elif int(j) <124:
                            set_type_list=['31','32','33']
                        for k in set_type_list:
                            temp_make.append(k+str(j)[1:3]+'0')
                    elif len(j)==15: ## X11 X22 X33 X44 X55 
                        temp_make.append('11'+j[1:3]+'0')
                        temp_make.append('12'+j[4:6]+'0')
                        temp_make.append('13'+j[7:9]+'0')
                        temp_make.append('14'+j[10:12]+'0')
                        temp_make.append('15'+j[13:]+'0')
                result_list.append(temp_make)
        if god==1:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if len(j)==3:
                        if int(j) <116:
                            pass
                        elif int(j) <120:
                            set_type_list=['21','22','23']
                        elif int(j) <124:
                            set_type_list=['31','32','33']
                        for k in set_type_list:
                            temp_make.append(k+str(j)[1:3]+'0')
                    elif len(j)==15: ## X11 X22 X33 X44 X55 
                        temp_make.append('11'+j[1:3]+'1')
                        temp_make.append('12'+j[4:6]+'0')
                        temp_make.append('13'+j[7:9]+'0')
                        temp_make.append('14'+j[10:12]+'0')
                        temp_make.append('15'+j[13:]+'0')
                result_list.append(temp_make)
        if god==2:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if len(j)==3:
                        if int(j) <116:
                            pass
                        elif int(j) <120:
                            set_type_list=['22','23']
                            temp_make.append('21'+str(j)[1:3]+'1')
                        elif int(j) <124:
                            set_type_list=['31','32','33']
                        for k in set_type_list:
                            temp_make.append(k+str(j)[1:3]+'0')
                    elif len(j)==15: ## X11 X22 X33 X44 X55 
                        temp_make.append('11'+j[1:3]+'0')
                        temp_make.append('12'+j[4:6]+'0')
                        temp_make.append('13'+j[7:9]+'0')
                        temp_make.append('14'+j[10:12]+'0')
                        temp_make.append('15'+j[13:]+'0')
                result_list.append(temp_make)
        if god==3:
            for i in case_list:
                temp_make=[]
                for j in i:
                    if len(j)==3:
                        if int(j) <116:
                            pass
                        elif int(j) <120:
                            set_type_list=['21','22','23']
                        elif int(j) <124:
                            set_type_list=['31','32']
                            temp_make.append('33'+str(j)[1:3]+'1')
                        for k in set_type_list:
                            temp_make.append(k+str(j)[1:3]+'0')
                    elif len(j)==15: ## X11 X22 X33 X44 X55 
                        temp_make.append('11'+j[1:3]+'0')
                        temp_make.append('12'+j[4:6]+'0')
                        temp_make.append('13'+j[7:9]+'0')
                        temp_make.append('14'+j[10:12]+'0')
                        temp_make.append('15'+j[13:]+'0')
                result_list.append(temp_make)



    return result_list


def meta_ful(set_num_dict,evert_list,bang_on_dict,list40_0):
    all_of_cases=[]
    ec=evert_list.count
    for i in range(101,136):
        if set_num_dict.get(str(i))==None:
            set_num_dict[str(i)]=0

    for case in [[4,3,3],[5,3,2],[5,2,3]]:
        for i in range(101,116):
            if set_num_dict.get(str(i))==case[0]:
                for j in range(116,120):
                    if set_num_dict.get(str(j))==case[1]:
                        for k in range(120,124):
                            if set_num_dict.get(str(k))==case[2]:
                                for sin in range(0,4):
                                    all_of_cases=all_of_cases+making_cases([(str(i),str(j),str(k))],sin,1)
    for mode in range(2,6):
        if mode==2:
            case_list=[[2,3,3,2],[3,2,3,2],[3,3,2,2],[3,3,3,1]]
        if mode==3:
            case_list=[[2,2,3,3],[3,1,3,3],[3,2,2,3],[3,2,3,2]]
        if mode==4:
            case_list=[[1,3,3,3],[2,2,3,3],[2,3,2,3],[2,3,3,2]]
        if mode==5:
            case_list=[[2,3,2,3],[3,2,2,3],[3,3,1,3],[3,3,2,2]]
        for case in case_list:
            for i in range(124,128):
                    
                for j in range(128,132):
                    for k in range(132,136):
                        for l in range(101,116):
                            if set_num_dict.get(str(i))==case[0]:
                                if set_num_dict.get(str(j))==case[1]:
                                    if set_num_dict.get(str(k))==case[2]:
                                        if set_num_dict.get(str(l))>=case[3]:
                                            for sin in range(0,4):
                                                all_of_cases=all_of_cases+making_cases([(str(i),str(j),str(k),str(l))],sin,mode)
                            if set_num_dict.get(str(i))==3:
                                if set_num_dict.get(str(j))==3:
                                    if set_num_dict.get(str(k))==3:
                                        if bang_on_dict[str(l)][2]+bang_on_dict[str(l)][3]==2:
                                            for sin in range(0,4):
                                                all_of_cases=all_of_cases+making_cases([(str(i),str(j),str(k),str(l))],sin,mode)


    for case in [[4,3,3],[5,2,3],[5,3,2]]:                
        for i in range(101,116):
            stri=str(i)
            for j in range(101,116):
                if i!=j:
                    strj=str(j)
                    for cases in [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]:
                        not_cases=[0,1,2,3,4]
                        not_cases.remove(cases[0]);not_cases.remove(cases[1])
                        aa=bang_on_dict.get(stri)[cases[0]]+bang_on_dict.get(stri)[cases[1]]
                        bb=bang_on_dict.get(strj)[not_cases[0]]+bang_on_dict.get(strj)[not_cases[1]]+bang_on_dict.get(strj)[not_cases[2]]
                        temp=[0,0,0,0,0]
                        if case[0]==4:
                            if aa==1 and bb==3:
                                for x in cases:
                                    temp[x]=stri
                                for y in not_cases:
                                    temp[y]=strj
                            if aa==2 and bb==2:
                                for x in cases:
                                    temp[x]=stri
                                for y in not_cases:
                                    temp[y]=strj
                        elif case[0]==5:
                            if aa==2 and bb==3:
                                for x in cases:
                                    temp[x]=stri
                                for y in not_cases:
                                    temp[y]=strj
                        if temp!=[0,0,0,0,0]:
                            ssgg=''.join(temp)
                            for k in range(116,120):
                                if set_num_dict.get(str(k))==case[1]:
                                    for l in range(120,124):
                                        if set_num_dict.get(str(l))==case[2]:
                                            for sin in range(0,4):
                                                all_of_cases=all_of_cases+making_cases([(ssgg,str(k),str(l))],sin,6)
    temp_list=[]
    temp_list_god=[]
    
    for now_list in all_of_cases:
        tem=0
        god=0
        for now_item in now_list:
            if ec(now_item)==0:
                if now_item[-1]=='1' or now_item[2:4]=='15' or now_item[2:4]=='19' or now_item[2:4]=='23':
                    break
            if ec(now_item)==1:
                tem=tem+1
                if now_item[-1]=='1':
                    god=1
        if tem==10:
            if god==0:
                temp_list.append(now_list)
            elif god==1:
                temp_list_god.append(now_list)
    all_list=[]
    all_list_god=[]
    for i in list40_0:
        for j in temp_list:
           tempx=list(j)
           tempx.append(i)
           all_list.append(tuple(tempx))
        for j in temp_list_god:
           tempx=list(j)
           tempx.append(i)
           all_list_god.append(tuple(tempx))
        
    all_list_num=len(all_list)+len(all_list_god)
    return [all_list,all_list_god,all_list_num]


