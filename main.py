from datetime import *
import sqlite3
from tkinter import *


#Multilingual option________________________________________________________________________________________
def get_lang(lang): #Dictionary selection with key (widget name): widget text according to the given one, in accordance with the language of the selected interface.
    result={}
    with sqlite3.connect('db/datebase.db') as db:
        db.row_factory=sqlite3.Row
        cursor = db.cursor()
        query = """ SELECT l_name,l_{} FROM lang """.format(lang)
        cursor.execute(query)
        result = dict(cursor)
    return result


def get_flower_copy_name(lang):##Variations in combobox.
    all_name=[]
    with sqlite3.connect('db/datebase.db') as db:
        cursor = db.cursor()
        query1 = """  SELECT name FROM flower_copy WHERE name_id='name_{}' """.format(lang)
        cursor.execute(query1)
        for i in list(cursor.fetchall()):
            all_name.append(i[-1])
    return all_name


def get_table(lang):#Database output for the third window.
    all_data=[]
    with sqlite3.connect('db/datebase.db') as db:
        cursor=db.cursor()
        query1="""  SELECT id,name,image,light,days,bloom FROM flower_copy WHERE name_id='name_{}' """.format(lang)
        cursor.execute(query1)
        all_date=cursor.fetchall()
    return(all_date)


def get_date_copy():#Data output for buttons.
    all_date=[]
    res={}
    with sqlite3.connect('db/datebase.db') as db:
        cursor=db.cursor()
        query="""  SELECT name,image,light,days,bloom,date_s FROM flower_copy JOIN submit on flower_copy.name=submit.name_s """
        cursor.execute(query)
        #all_date=cursor.fetchall()
        all_date=list(cursor.fetchone())
    return all_date

def get_flower_light_copy(): #Light.
    light = get_date_copy()
    return light[2]

def get_flower_bloom_copy(): #Blooming.
    bloom = get_date_copy()
    return bloom[4]

def get_flower_image_copy(): #Image.
    image = get_date_copy()
    return image[1]

def get_flower_days_copy(): #Days.
    days = get_date_copy()
    return days[3]

def last_watering_copy(): #Watering
    d_1=get_date_copy()[5].split('-')
    if d_1==['']:
        a=str(datetime.now().date()).split('-')
        wat_date = datetime(int(a[0]), int(a[1]), int(a[2]))
        next_wat = wat_date + timedelta(days=get_flower_days_copy())
        next_date = str(next_wat).split(' ')[0]
        b = next_date.split("-")
        c = ''
        while len(b) > 0:
            c += f'{b[-1]}-'
            del b[-1]
        return c[:-1]
    else:
        wat_date=datetime(int(d_1[2]),int(d_1[1]),int(d_1[0]))
        next_wat=wat_date+timedelta(days=get_flower_days_copy())
        next_date=str(next_wat).split(' ')[0]
        b=next_date.split("-")
        c=''
        while len(b)>0:
            c+=f'{b[-1]}-'
            del b[-1]
        return c[:-1]


def insert_info(name,date): #Date from  "submit".
    success=False
    with sqlite3.connect('db/datebase.db') as db:
        cursor = db.cursor()
        query1 = """ UPDATE submit SET name_s==?,date_s==? WHERE id==?"""
        cursor.execute(query1, (name, date, 1))
        db.commit()
        seccess= True
    return seccess



