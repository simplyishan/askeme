import flet , requests
import flet as ft
# from flet import  Container, Column,Page , AppBar , TextField , Image , colors ,FilledButton , Text
from flet import *
from getquote import quote
import json


f = open('data.json')
data = json.load(f)
for i in data['logincred']:
    dmail = i["mm"]
    dpass = i['pp']


dmail = i["mm"]
dpass = i['pp']

def main(page: Page):
    page.auto_scroll = True
    page.window_width=300.00
    page.window_height=720.00
    page.appbar=AppBar(title=Text('LOGIN FORM'),bgcolor=colors.BLACK12 , center_title=True)
    # page.add()
    
    img = Image(
        src=f'https://i.postimg.cc/L5z7hZXg/undraw-Login-re-4vu2.png',
    fit='contain'
        
    )
    email = TextField(label='Email',hint_text='Email Address')
    passw = TextField(label='Password', password=True,can_reveal_password=True,hint_text='Enter Password')
    
    # call back for button 
    
    def btn_callback(e):
        if not email.value:
            email.error_text = "Email Not Given"
            page.update()
        else:
            email.error_text = None
            page.update()
            
        if not passw.value:
            passw.error_text = "Pass Not Given"
            page.update()
        else:
            passw.error_text = None
            page.update()

        cmail = email.value
        cpass = passw.value
        def checkpass():
            if (cmail==dmail) and (cpass==dpass):
                print('CORRECT PASSWORD AND MAIL') 
                dlg = ft.AlertDialog(
                title=ft.Text("Sucessfully Logined")
             
                 )

                page.dialog = dlg
                dlg.opacity=50
                
             
                dlg.open = True
                # CHANGING THE PAGE WITHOUT ROUTING
                page.clean()
                page.max_window_width=300.00
                page.max_window_height=720.00
                page.appbar=AppBar(title=Text('HOME SCREEN'),bgcolor=colors.BLACK38 , center_title=True , color=colors.WHITE)
                 # validation 
                def btn_clkback2(e):
                    if len(prompt.value) < 1:
                     prompt.error_text = 'pls write atleast 2 letters '
                     page.update()
                    elif len(prompt.value) > 0:
                        prompt.error_text = None
                        page.update()
                    
                    
                    
                    
                    
                    
                    
                    
                    wait = ft.AlertDialog(
                    title=ft.Text("pls wait a little bit the ai needs time to find out the answer meanwhile don't touch anything..!"))
                    page.dialog = wait
                    dlg.open = True
                    page.update()
                    promp = prompt.value.lower()
                    results = quote(prompt=promp)
                    page.add(ft.Text(results))
                    
                    
                   
                   


                
                
                textt = ft.Text("Welcome To CsQuote/lineExpander/QuesAns | A Simple OpenAi based quote gen/LineExpander/QuesAns..! ")
                prompt = TextField(label='enter keywords',hint_text='what is love?')
                sendbutton = ft.OutlinedButton(text="Get Response",icon='send_icon' , on_click=btn_clkback2)
                
                # 

               
                



                page.add(
                Container(
                
                Column([
                    textt,prompt , sendbutton 
                ], spacing=20)
                    
                )    )
                page.add(ft.Text("EXAMPLES \n\n ques : what is python?\nquote :   write a quote about love.  \n ans/math : Find The Value of X :  x + 8 = 12 "))
                
                    
               
               

                    
               

            
                
                page.update()
                   







            else:  
                dlg = ft.AlertDialog(
                title=ft.Text("WRONG PASSWORD")
                
                )

                page.dialog = dlg
                dlg.opacity=50
                
                dlg.open = True
                page.update()


            
         
                

      
        checkpass()          

    btn = OutlinedButton(text='Login' , width=300 , height=45 , on_click=btn_callback )
    page.add(
         Container(
        Column([
            img,
            email,
            passw,
            btn
        ], spacing=20)
         )
        

        
    )
   







flet.app(target=main)
