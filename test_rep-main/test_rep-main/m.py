import flet as ft 
import time
import threading
from runmodel import predicto
import warnings

warnings.filterwarnings("ignore")

def main(page:ft.Page):
    page.title="Anti virus app"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.window_min_width=600
    page.window_min_height=600
    page.window_center=True
    
############################################## Thread class ################################################################### 
    class thread(threading.Thread):
        ############################################## Thread 1 ################################################################### 
        def theread1():
            scan_bg.padding=195
            while True:
                scan_bg.rotate.angle += 1
                page.update()
                time.sleep(0.07)
        ########################################### Thread 2 ##################################################################         
        def thread2():
            for i in range(5):
                num=ft.Text(i,size=30,weight=ft.FontWeight.W_900)
                scan_button.content= ft.Container(
                    ft.Stack(controls=[
                            ft.Container(
                                ft.Container(
                                    width=200,height=200,
                                    gradient=ft.LinearGradient(
                                                    begin=ft.alignment.top_center,
                                                    end=ft.alignment.bottom_center,
                                                    colors=[ft.colors.BLUE, ft.colors.YELLOW],
                                    ),shape=ft.BoxShape.CIRCLE,border_radius=180
                                            
                                            ),alignment=ft.alignment.center
                            ),
                            ft.Container(ft.Row(controls=[ft.Text(" ",size=5),num,ft.Text("%",size=30,weight=ft.FontWeight.W_900)],alignment=ft.MainAxisAlignment.CENTER),alignment=ft.alignment.bottom_center,padding=ft.padding.only(bottom=93)),
                        
                    ]),
                alignment=ft.alignment.bottom_left
                )
                page.update()
                time.sleep(1)
            page.update()
            animate_popup_1()
            return page.add(
                scan
            )
        
        
        
################################################ File Picker ################################################################### 
    
    
    def animate_popup_1():
        time.sleep(2)
        inside_scan.height=0
        popup_continer_1.content=ft.Text("CONGRAGULATIONS, We didn't Found any virus in this File")
        popup_continer_1.height=260
        page.update()
        time.sleep(5)
        popup_continer_1.height=0
        inside_scan.height=230
        page.update()
        scan_animation_button.content=ft.Stack(controls=[scan_button])
        page.update()
        
        # global pop_message
        # if(0):
        #     popup_continer_1.bgcolor="green"
        #     popup_continer_1.height=90
        #     popup_continer_1.content=ft.Text("CONGRAGULATIONS, We didn't Found any virus in this File")
            
        # else:
        #     popup_continer_1.bgcolor="red"
        #     popup_continer_1.height=90
        #     popup_continer_1.content=ft.Text("We have detected virus in your computer")
        # page.update()
    
    def animate_popup_2(pridict):
        global pop_message
        if(pridict[0][0]==0):
            popup_continer_2.bgcolor="green"
            popup_continer_2.height=70
            popup_continer_2.content=ft.Text("CONGRAGULATIONS, We didn't Found any virus in this File")
        
        else:
            popup_continer_2.bgcolor="red"
            popup_continer_2.height=70
            popup_continer_2.content=ft.Text("We have detected virus in your computer")
        page.update()
        
    
    global file_loactions
    file_loactions=[]
    def send_file_location(e):
        global file_loactions
        pridict=predicto(file_loactions[0])
        
        upload_button.disabled=True
        upload_button.bgcolor="#dddddd"
        upload_button.content.color="black"
        animate_popup_2(pridict)
        
        file_select_button.disabled=True
        file_select_button.bgcolor="#dddddd"
        file_select_button.content.color="black"
        
        page.update()
        time.sleep(5)
        file_loactions.clear()
        pridict.clear()
        popup_continer_2.height=0
        
        file_select_button.bgcolor="#232F34"
        file_select_button.content.color="white"
        file_select_button.disabled=False
        
        page.update()
        
        
    def dialog_picker(e:ft.FilePickerResultEvent):
        global file_loactions
        if e.files is None:
            upload_button.disabled=True 
            page.update()
        else :
            upload_button.disabled=False
            upload_button.bgcolor="#232F34"
            upload_button.content.color="white"
            page.update()
        for i in e.files:
            file_loactions.append(i.path)
        page.update()
    
    pop_message=ft.Text()
   
    popup_continer_1=ft.Container(content=pop_message,width=230,height=0,animate=ft.animation.Animation(1000,"bounceOut"),alignment=ft.alignment.center,blur=5,bgcolor="green",padding=12)
   
    popup_continer_2=ft.Container(content=pop_message,width=400,height=0,animate=ft.animation.Animation(1000,"bounceOut"),alignment=ft.alignment.center,blur=5,bgcolor="green",padding=12)    
    file_picker = ft.FilePicker(on_result=dialog_picker)
    
    page.overlay.append(file_picker) #it will pop up the file selection window without distrubing page layout
    page.update()
    
    file_select_button=ft.Container(content=ft.Text("Select a File",text_align=ft.alignment.center),on_click=lambda _: file_picker.pick_files(allow_multiple=True),height=40,width=180,bgcolor="#232F34",alignment=ft.alignment.center,border_radius=15)
    upload_button=ft.Container(content=ft.Text("Upload",text_align=ft.alignment.center,color="black"),on_click=send_file_location,height=40,width=180,disabled=True,bgcolor="#dddddd",alignment=ft.alignment.center,border_radius=15)
    
    file_picker_content=ft.Container(
        ft.Column(controls=[popup_continer_2,
            ft.Container(    
                ft.Container(
                    ft.Column(controls=[
                        file_select_button,
                        upload_button
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ),
                width=400,
                height=600,
                expand=True,
                alignment=ft.alignment.center,
                bgcolor="#4A6572"
            )]),
        expand=True,
        padding=ft.padding.only(top=100,bottom=100),
        alignment=ft.alignment.center
        
    )           
    
   
    t1=threading.Thread(target=theread1)
    t2=threading.Thread(target=thread2)
    page.update()
 #######################################################################################################################   
    def animate(e):
       #scan_animation_button=ft.Container(content=[ft.Stack(controls=[scan_button])])
        scan_animation_button.content=ft.Stack(controls=[scan_bg,scan_button])
        page.update()
        t1.start()
        t2.start()
    
    #/////////////////////////
        
    scan_1=ft.Container(ft.Stack(
        controls=[ #on strat page scan 1st scan button
        ft.Container(
            ft.Container(           #scan inside color
                width=200,height=200,
                gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[ft.colors.BLUE, ft.colors.YELLOW],
                ),shape=ft.BoxShape.CIRCLE,border_radius=180
                         
                         ),alignment=ft.alignment.center),
        ft.Container(
            ft.Text("SCAN",size=30,weight=ft.FontWeight.W_500),alignment=ft.alignment.center,padding=70)
        ]),alignment=ft.alignment.center
    )
    
    #/////////////////////////
    
    scan_button=ft.Container(
                scan_1,on_click=animate,alignment=ft.alignment.center
                )
   
    #/////////////////////////
    scan_bg=ft.Container(
            gradient=ft.SweepGradient(
            center=ft.alignment.center,
                colors=[
                    "red",
                    "0xFF4285F4",
                    "red"
                
                ]),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_IN_OUT),
        shape=ft.BoxShape.CIRCLE,
        )
     #/////////////////////////
     
    scan_animation_button=ft.Container(ft.Stack(controls=[scan_button]))

    #/////////////////////////
    inside_scan=ft.Container(scan_animation_button,width=230,height=230,animate=ft.animation.Animation(1000,"bounceOut"))
    scan=ft.Container(ft.Column(controls=[popup_continer_1,inside_scan],alignment=ft.MainAxisAlignment.CENTER),width=1980,height=1080,expand=True,alignment=ft.alignment.center)
    
    
############################################## Title bar ########################################################################
   
    page.appbar=ft.AppBar(
    center_title=False,
    toolbar_height=60,
    bgcolor="white",
    title=ft.Text("Anurag",color="red"),  
    )
    
############################################## Change Navigation ###############################################################    
    
    def change_nav(e):
        if e.control.selected_index==0:
            page.clean()
            page.add(
                scan
            )
        elif e.control.selected_index==1:
            page.clean()
            page.add(
                file_picker_content
            )
            
        elif e.control.selected_index==2:
            page.clean()
            page.add(
                ft.Container(
                    bgcolor="blue",
                    expand=True
                )
            )
        elif e.control.selected_index==3:
            page.clean()
            page.add(
                ft.Container(
                    bgcolor="yellow",
                    expand=True
                )
            )
########################################### page navigation #############################################################    
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.SHIELD_OUTLINED,
                selected_icon=ft.icons.SHIELD,
                label="Scan",
                ),
            ft.NavigationDestination(
                icon=ft.icons.SCREEN_SEARCH_DESKTOP_OUTLINED,
                selected_icon=ft.icons.SCREEN_SEARCH_DESKTOP_ROUNDED,
                label="Scan from computer",
            ),
            ft.NavigationDestination(
                icon=ft.icons.MONITOR_HEART_OUTLINED,
                selected_icon=ft.icons.MONITOR_HEART_ROUNDED,
                label="Activity",   
            ),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label="Settings",   
            )
        ],
        
        on_change=lambda e: change_nav(e),  
        
    ) 
    
########################################### page #######################################################################ˀ
    page.window_full_screen=True
    page.add(
        scan
    )
    page.bgcolor="#344955"

    page.update()
    
ft.app(main)
