#macbook /Users/anuragnarsingoju/Documents/Manemma soft/CODE/login.jpg
#macmini /Users/bablunarsingoju/Library/Mobile Documents/com~apple~CloudDocs/Documents/Manemma soft/CODE/login.jpg


import flet as ft
from time import sleep
import math
import json
import os
from pathlib import Path
import threading

img=os.path.dirname(os.path.normpath(__file__))
img=img+"/login.jpg"
# login=""
# with open("login.json","r+") as a:
#     login=json.load(a)
# print(login)

#...................................................................................................................................

width1=980
height1=1300
#...................................................................................................................................
a=["anurag"]
def log_checker(e):
    if i1.value in login.keys():
        if(i2.value==login[i1.value]):
            i1.error_text=None
            i1.error_style=None
            i2.error_text=None
            i2.error_style=None
            
        else:
            i1.error_text=None
            i1.error_style=None
            i2.error_text="Incorrect Password"
            ft.page.update
    else:
        i2.error_text=None
        i2.error_style=None
        
        i1.error_text="User Not Found !!"
        

     
#...................................................................................................................................
empty1=ft.Container(
    width=50
)
empty2=ft.Container(
    width=50,
)

a1=ft.Container(
    ft.Image(src=img,fit=ft.ImageFit.SCALE_DOWN,expand=1),
)

a2=ft.Container(
            border_radius=5,
            width=width1-(width1/3),
)

t1=ft.Text("Login",size=70,color="#FFF3B6")

i1= ft.TextField(label="Enter User ID ",icon=ft.icons.PERSON,text_size=20,border_radius=20,width=480,color="#FFF3B6",border_color="#FFF3B6",autofocus=True,on_submit=True)

i2=ft.TextField(label="Enter Password ",icon=ft.icons.LOCK_OUTLINE_ROUNDED,text_size=20,border_radius=20,width=480,color="#FFF3B6",border_color="#FFF3B6",password=True,autofocus=True,on_submit=True)

i3=ft.ElevatedButton(text="Submit",color="#AD5993",bgcolor="#FFF3B6")

a21=ft.Container(
    ft.Column(controls=[empty1,
        ft.Row([
            t1
        ],alignment=ft.MainAxisAlignment.CENTER),empty2,
        ft.Container(
            i1,margin=ft.margin.only(left=50,right=50)),
        ft.Container(
            i2,margin=ft.margin.only(left=50,right=50)),
        ft.Container(
            i3,margin=ft.margin.only(left=92,right=50)),
        ],
              
        alignment=ft.MainAxisAlignment.START,spacing=20),
    width=width1-round(width1/3),height=height1-(height1/4),bgcolor="#AD5993",margin=ft.margin.only(top=round(height1/80),left=round(height1/80)),
)

#...................................................................................................................................

#body part above are inside body parts

val=ft.TextField()
body= ft.Container(
    ft.Stack([a1,a2,a21]),
)

#...................................................................................................................................

"""
flet login_page.py
"""

login_text=ft.Text("Login")
def main(page: ft.Page):
    
    print("active threads : ", threading.enumerate())
    page.padding = 0
    page.window_full_screen=True
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.window_min_width=1360
    page.window_min_height=788
    page.window_max_height=1080
    page.window_max_width=1980
    
    def page_resize(e):
        
        if(page.window_width==0 and page.window_height==0):
            width1=1920
            height1=1080
        else:
            width1=round(page.window_width-(page.window_width/2))
            height1=round(page.window_height-(page.window_height/1.3))
            
        a2.width=width1-round(width1/3)
        a2.height=round(height1*3.35)
        a2.margin=ft.margin.only(left=width1+round(width1*0.217),top=height1-round(height1/2.05))
        a21.width=width1-round(width1/2.68)
        a21.margin=ft.margin.only(left=width1+round(width1*0.235),top=height1-round(height1/2.4))
        a21.height=round(height1*3.2)
        t1.size=width1/13
        empty1.height=round(height1*0.3)
        empty2.height=round(height1*0.3)
        page.update()
        
    page.add(
        body,
        
       
    )
    i3.on_click=log_checker
    page.on_resize = page_resize
    page.update()
    
    
    i=1
    while True:
        i+=1
    
        a2.gradient=ft.SweepGradient(
                center=lambda :ft.alignment.center,
                tile_mode=ft.GradientTileMode.REPEATED,

                colors=[
            
                    
                   "#AD5993",
                    "#AD5993",
                    "red",
                   "#AD5993",
                   "#AD5993",
                   "#AD5993",
                   "#AD5993",
                   "#AD5993",
                    "red",
                    "#AD5993",
                    "#AD5993",
                    "#AD5993",
                 
               
                    

                ],
        
                rotation=i/5,
                
        )
        sleep(0.09)
        page.update()
        
ft.app(main)