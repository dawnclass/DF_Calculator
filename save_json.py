import json
import shutil
import os
import write_now

with open('save/job_code.json','r', encoding='utf-8') as code:
    job_code_list=json.load(code)
temp_dict={}
last_code=job_code_list[-1]['code']
last_job=job_code_list[-1]['name']
last_file=job_code_list[-1]['file']
if last_job == str(write_now.job_name) or last_file == str(write_now.file_name):
    del job_code_list[-1]
    temp_dict['code']=last_code
else: 
    temp_dict['code']=last_code+1
temp_dict['name']=str(write_now.job_name)
temp_dict['file']=str(write_now.file_name)

job_code_list.append(temp_dict)
with open('save/job_code.json', 'w', encoding='utf-8') as code_save:
    json.dump(job_code_list, code_save, indent="\t",ensure_ascii=False)




show=write_now.info
with open('save/'+str(write_now.file_name)+'.json', 'w', encoding='utf-8') as make_file:
    json.dump(show, make_file, indent="\t",ensure_ascii=False)

shutil.copy('write_now.py', 'save_py/'+str(write_now.file_name)+'.py')
#os.rename( 'savepy/write_now.py','savepy/'+str(write_now.file_name)+'.py')
