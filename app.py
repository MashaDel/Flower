from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry, Calendar
import main as m
from tkinter import messagebox  as mb
from datetime import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.lang='en'
        self.schema=m.get_lang(self.lang)
        self.title(self.schema['l_name_app'])
        self.style =ttk.Style()
        self.style.configure('TFrame',background='green')
        self.style.configure('Error.TLabel',foreground='red', padding=(10, 10, 60, 10))
        self.style.configure('Smp.TLabel', padding=(10, 10, 60, 10)) #default style(10,10,60,10):(left:above:right:from below:)
        self.style.configure('Bldlb.TLabel',font=("Helvetica",13,'bold'),padding=(0,10,0,10)) #Separate style for Frame_2
        self.put_frames()
        self.put_menu()
        self.popup=Popup(self)

    def put_menu(self):
        self.config(menu=MainMenu(self))

    def put_frames(self):
        self.add_form_frame = Frame_1(self).grid(row=0, column=0, sticky='nswe')
        self.state_frame = Frame_2(self).grid(row=0, column=1, sticky='nesw')
        self.table_frame = Frame_3(self).grid(row=1, column=0, columnspan=2, sticky='snwe')

    def refresh(self):
         all_frames = [f for f in self.children]
         for f_name in all_frames:
             self.nametowidget(f_name).destroy()
         self.put_frames()
         self.put_menu()
         self.popup = Popup(self)

    def switch_lang(self,language):
        self.lang= language
        self.schema=m.get_lang(language)
        self.refresh()


class Popup:
    def __init__(self,master):
        self.master=master

    def show(self,window_type): #Calling frame of a specific type
        getattr(self,window_type)()

    def quit(self):
        answer=mb.askquestion("Quit","Are you sure")
        if answer=="yes":
            master.destroy()

    def faq(self):
        mb.showinfo("FAQ","Text not ready")


# Class for creating the main menu of the application___________________________________________________________________________________
class MainMenu(Menu):
    def __init__(self,mainwindow):
        super().__init__(mainwindow)

        file_menu=Menu(self)
        options_menu=Menu(self)
        help_menu=Menu(self)

        file_menu.add_command(label='Refresh',command=mainwindow.refresh)
        file_menu.add_separator()
        file_menu.add_command(label='Quit',command=lambda:mainwindow.popup.show('quit'))

        lang_menu=Menu(options_menu)
        self.s_var=StringVar()
        self.s_var.set(self.master.lang)
        lang_menu.add_radiobutton(label='Русский',variable=self.s_var,value='ru',
                                  command=lambda:mainwindow.switch_lang(self.s_var.get()))
        lang_menu.add_radiobutton(label='English',variable=self.s_var,value='en',
                                  command=lambda:mainwindow.switch_lang(self.s_var.get()))
        options_menu.add_cascade(label='Switch language',menu=lang_menu)
        options_menu.add_separator()
        options_menu.add_command(label='Switch theme')

        help_menu.add_command(label='About us')
        help_menu.add_separator()
        help_menu.add_command(label='FAQ',command=lambda:mainwindow.popup.show('faq'))

        self.add_cascade(label='File',menu=file_menu)
        self.add_cascade(label='Options',menu=options_menu)
        self.add_cascade(label='Help',menu=help_menu)


# FIRST FRAME______________________________________________________________________________________________________________
class Frame_1(ttk.Frame): #It is obligatory to specify "ttk.Frame" as styles go to widgets only from "ttk" module.
    def __init__(self, parent):
        super().__init__(parent)
        self.comb = m.get_flower_copy_name(self.master.lang)
        self.put_widgets()

    def put_widgets(self):
         self.images=[]
         self.l_flower_text = ttk.Label(self, text=self.master.schema['l_flower_text'],width=10,style='Smp.TLabel')
         self.l_flower_value = ttk.Combobox(self, text=' ', values=self.comb,width=10)
         self.l_date_last = ttk.Label(self, text=self.master.schema['l_date_last'],width=15)
         self.f_date_last = DateEntry(self, foreground='black', normalforeground='black', selectforeground='red',
                                      background='white', date_pattern='dd-mm-YYYY',width=10
                                      )
         #print(self.f_date_last.winfo_class()) --------Command to find out which style class this element uses.
         self.f_date_last.delete(0, "end")

         self.logo = Image.open('im/s.png')  # add foto of flower
         self.logo = self.logo.resize((80, 80), Image.Resampling.LANCZOS)
         self.image = ImageTk.PhotoImage(self.logo)
         self.images.append(self.image)
         self.flower_set = ttk.Label(self, image=self.image)
         self.images.append(self.image)
         self.btn_submit = ttk.Button(self, text=self.master.schema['btn_submit'], command=self.form_submit)


         self.l_flower_text.grid(row=0, column=0, sticky='w')
         self.l_flower_value.grid(row=0, column=1, sticky='e')
         self.flower_set.grid(row=1, column=0, columnspan=2, sticky='')
         self.l_date_last.grid(row=2, column=0, sticky='w')
         self.f_date_last.grid(row=2, column=1, sticky='e')
         self.btn_submit.grid(row=3, column=0, columnspan=2, sticky='')
         self.f_date_last._top_cal.overrideredirect(False)


    def show_error(self):
        mb.showerror('Error','Please,choose a flower')

    def form_submit(self):
        flag=True
        name = self.l_flower_value.get()
        date = self.f_date_last.get()
        if name in self.comb:
            flag=True
            self.l_flower_text['style'] = 'Smp.TLabel'
        else:
            if name!='':
                pass
            else:
                flag=False
                self.l_flower_text['style']='Error.TLabel'
                self.bell()
                self.show_error()
        if flag:
            if m.insert_info(name, date):
                self.master.refresh()

# SECOND FRAME_____________________________________________________________________________________________________________
class Frame_2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.put_widgets()

    def put_widgets(self):
        l_light_text = ttk.Label(self, text=self.master.schema['l_light_text'],style='Smp.TLabel')
        f_light_value = ttk.Label(self, text=m.get_flower_light_copy(),style='Bldlb.TLabel' )
        l_date_next = ttk.Label(self, text=self.master.schema['l_date_next'],style='Smp.TLabel')
        f_date_next = ttk.Label(self, text=m.last_watering_copy(),
                            style='Bldlb.TLabel')
        l_bloom = ttk.Label(self, text=self.master.schema['l_bloom'],style='Smp.TLabel')
        l_bloom_value = ttk.Label(self, text=m.get_flower_bloom_copy(), style='Bldlb.TLabel')
        #To solve the problem with inserting a photo, read here:
        # https://web.archive.org/web/20201111190625/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        logo_1 = Image.open(m.get_flower_image_copy())  # add foto of flower
        logo_1 = logo_1.resize((80, 80), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(logo_1)
        flower_foto = ttk.Label(self, image=photo)
        flower_foto.image = photo

        l_light_text.grid(row=0, column=0, sticky='w')
        f_light_value.grid(row=0, column=1, sticky='e')
        l_date_next.grid(row=1, column=0, sticky='w')
        f_date_next.grid(row=1, column=1, sticky='e')
        l_bloom.grid(row=2, column=0, sticky='sw')
        l_bloom_value.grid(row=2, column=1, sticky='se')
        flower_foto.grid(row=3, column=0, columnspan=2, sticky='')

# THIRD FRAME__________________________________________________________________________________________________________
# For the introduction to Tkinter Treeview widget use link:'https://www.pythontutorial.net/tkinter/tkinter-treeview/'
class Frame_3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #self['background'] = self.master['background']
        self.table = m.get_table(self.master.lang)
        self.put_widgets()

    def put_widgets(self):
         table = ttk.Treeview(self, show='headings')
         l=self.master.schema
         heads=[
             l['l_head_id'],
             l['l_head_name'],
             l['l_head_image'],
             l['l_head_light'],
             l['l_head_days'],
             l['l_head_bloom']]
         table['columns'] = heads
         table['displaycolumns']=[l['l_head_name'],l['l_head_image'],l['l_head_light'], l['l_head_days'], l['l_head_bloom'], l['l_head_id']] # command for swaps column names

         for header in heads:
             table.heading(header, text=header, anchor='center')
             table.column(header, anchor='center', width=120)
             table.column(l['l_head_id'], width=50)

         for row in self.table:
             table.insert('',END, values=row)

         scroll = ttk.Scrollbar(self, command=table.yview)
         table.configure(yscrollcommand=scroll.set)
         scroll.pack(side=RIGHT, fill=Y)
         table.pack(expand=YES, fill=BOTH)





app = App()
app.mainloop()

