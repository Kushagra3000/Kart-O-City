#Virtual Keyboard to prevent keylogging malware
try:
    import Tkinter
except:
    import tkinter as Tkinter

import pyautogui

keys =[ 
[

 [
  ("Character_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   ('~\n`','!\n1','@\n2','#\n3','$\n4','%\n5','^\n6','&\n7','*\n8','(\n9',')\n0','_\n-','+\n=','|\n\\','backspace'),
   ('tab','q','w','e','r','t','y','u','i','o','p','{\n[','}\n]','   '),
   ('capslock','a','s','d','f','g','h','j','k','l',':\n;',"\"\n'","enter"),
   ("shift",'z','x','c','v','b','n','m','<\n,','>\n.','?\n/',"shift"),
   ("ctrl", "[+]",'alt','\t\tspace\t\t','alt','[+]','[=]','ctrl')
  ]
 ]
],

[

 [
  ("Numeric_Keys"),
  ({'side':'top','expand':'yes','fill':'both'}),
  [
   ("num\nlock","/","*","-"),
   ("7","8","9","+"),
   ("4","5","6"," "),
   ("0","1","2","3"),
   ("0",".","enter")
  ]
 ],

]

]


class Keyboard(Tkinter.Frame):
 def __init__(self, *args, **kwargs):
  Tkinter.Frame.__init__(self, *args, **kwargs)

  
  self.create_frames_and_buttons()


 def create_frames_and_buttons(self):
  
  for key_section in keys:
  
   store_section = Tkinter.Frame(self)
   store_section.pack(side='left',expand='yes',fill='both',padx=10,pady=10,ipadx=10,ipady=10)
   
   for layer_name, layer_properties, layer_keys in key_section:
    store_layer = Tkinter.LabelFrame(store_section)#, text=layer_name)
    
    store_layer.pack(layer_properties)
    for key_bunch in layer_keys:
     store_key_frame = Tkinter.Frame(store_layer)
     store_key_frame.pack(side='top',expand='yes',fill='both')
     for k in key_bunch:
      k=k.capitalize()
      if len(k)<=3:
       store_button = Tkinter.Button(store_key_frame, text=k, width=2, height=2)
      else:
       store_button = Tkinter.Button(store_key_frame, text=k.center(5,' '), height=2)
      if " " in k:
       store_button['state']='disable'
      #flat, groove, raised, ridge, solid, or sunken
      store_button['relief']="raised"
      store_button['bg']="white"
      store_button['command']=lambda q=k: self.button_command(q)
      store_button.pack(side='left',fill='both',expand='yes')
  return

  
 def button_command(self, event):
  print(event)
  return


def main():
 root = Tkinter.Tk(className="Virtual Keyboard")
 Keyboard(root).pack()
 root.mainloop()
 return

if __name__=='__main__':
 main()
