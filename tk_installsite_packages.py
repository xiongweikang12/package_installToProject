#TODO 配置虚拟环境时，导入想要的第三方库
import os
import pathlib
import random
import time
import tkinter as tk
import pathlib as plib
from tkinter import messagebox
import re
import shutil



window=tk.Tk()
window.title('导入第三库')
window.geometry('400x400')
entry_install=tk.StringVar
entry_project=tk.StringVar
l_top=tk.Label(window,text='第三方库',height=1,width=20,bg='red')
l_top.place(x=130,y=10)
tk.Label(window,text='第三方库库名 :',height=1,width=15).place(x=60,y=45)
tk.Label(window,text='环境项目名称 :',height=1,width=15).place(x=60,y=75)
e_install=tk.Entry(window)
e_install.place(x=175,y=45)
e_project=tk.Entry(window)
e_project.place(x=175,y=75)



def copied_to_newproject():
    
    p=plib.Path(r'D:\lib\site-packages') #pip 安装的目录
    p_list=list(p.glob('*'))
    p_dirname=[i for i in p_list if i.is_dir()] #通过列表推导式获取p路径下是文件夹的路径
    p_python=plib.Path.cwd().parent.parent #设置环境的目录 D:\python
    p_list_project=list(p_python.glob('*'))
    p_list_project=[str(a) for a in p_list_project if a.is_dir()] #获取环境项目路径，转换成string


    flag_install=len(p_dirname)
    check_install=0
    entry_install=e_install.get()
    for name_ in p_dirname:
        if bool(re.search('%s$'%(entry_install),name_.name)):#通过entry输入内容，遍历搜索库名
            #将该文件夹复制到环境的site_packages
            path_sitepackage_install=name_ #得到库的路径
            print(path_sitepackage_install)
            break
        else:
            check_install+=1
            continue
    if check_install==flag_install:
        messagebox.showerror(title='information',message='no find out the package')
        quit()

    flag_project=len(p_list_project)
    check_project=0
    entry_project = e_project.get()
    for path_project in p_list_project:
        if bool((re.search('%s$' % (entry_project), path_project))):
            path_sitepackage = pathlib.Path(path_project) / pathlib.Path('Lib/site-packages')/pathlib.Path(entry_install)
            print(path_sitepackage)
            break
        else:
            check_project+=1
            continue
    if check_install==flag_project:
        messagebox.showerror(title='information',message='on find out the project')
        quit()
            # os.mkdir(path_sitepackage)
            # break

    #TODO 判断是否输入正常，第三方库是否重复安装
    shutil.copytree(path_sitepackage_install,path_sitepackage)
    messagebox.showinfo(title='information',message='pasckage have installed ')
    time.sleep(random.randint(2,5))
    quit()




    #
    #         print()
    #
    #     else:
    #         continue
    # messagebox.showinfo(title='remind',message='sorry! no finder package please comfirm which wheath install suessfully')







button_ml=tk.Button(window,text='启动',height=1,width=10,command=copied_to_newproject)
button_ml.place(x=200,y=100)
button_quit=tk.Button(window,text='退出',height=1,width=10,command=quit)
button_quit.place(x=200,y=130)

if __name__=='__main__':
    window.mainloop()

