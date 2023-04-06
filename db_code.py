import sqlite3

#with sqlite3.connect('db/datebase.db') as db:
    #cursor=db.cursor()
    #query1 ="""INSERT INTO flower(id,name,image,light,days,bloom) VALUES(1,'euharis','im/euharis.png','west-east',5,'febrary') """
    #query2 = """INSERT INTO flower(id,name,image,light,days,bloom) VALUES(2,'aloe','im/aloe.png','west-east-nord',6,'not bloom') """
    #query3 = """INSERT INTO flower(id,name,image,light,days,bloom) VALUES(3,'orchid','im/orchid.png','west-south',7,'march-july') """
    #query4 = """INSERT INTO flower(id,name,image,light,days,bloom) VALUES(4,'zamic','im/zamic.png','west-east',10,'august') """
    #cursor.execute(query1)
    #cursor.execute(query2)
    #cursor.execute(query3)
    #cursor.execute(query4)
    #db.commit()

#Adding data to a table "flower"_________________________________________________________________
#flower_info=[
        #('euharis', 'im/euharis.png', 'west-east', 5, 'febrary'),
        #('aloe', 'im/aloe.png', 'west-east-nord', 6, 'not bloom'),
        #('orchid', 'im/orchid.png', 'west-south', 7, 'march-july'),
        #('zamic', 'im/zamic.png', 'west-east', 10, 'august')
    #]
#with sqlite3.connect('db/datebase.db') as db:
    #cursor=db.cursor()
    #query ="""INSERT INTO flower(name,image,light,days,bloom) VALUES(?,?,?,?,?); """
    #cursor.executemany(query,flower_info)
    #db.commit()


#Addition date to table "flower"__________________________________________________________________
#flower_info=[
        #('anturium', 'im/anturium.png', 'west-nord', 3, 'june'),
        #('sinningia', 'im/sinningia.png', 'west', 4, 'april-august'),
        #('pelargonium', 'im/pelargonium.png', 'west-south', 7, 'may-october'),
        #('narcissus', 'im/narcissus.png', 'south', 6, 'august'),
        #('aglaonema', 'im/aglaonema.png', 'nord', 7, 'not bloom'),
        #('calathea', 'im/calathea.png', 'nord', 5, 'not bloom')
    # ]
#with sqlite3.connect('db/datebase.db') as db:
    #curso=r=db.cursor()
    # query ="""INSERT INTO flower(name,image,light,days,bloom) VALUES(?,?,?,?,?); """
    # cursor.executemany(query,flower_info)
    # db.commit()

# flower_info=[
#         ('nephrolepis', 'im/nephrolepis.png', 'west-nord', 3, 'not bloom'),
#         ('hedera', 'im/hedera.png', 'west', 6, 'not bloom'),
#         ('hippeastrum', 'im/hippeastrum.png', 'west-south', 7, 'may-october')
#         ]
# with sqlite3.connect('db/datebase.db') as db:
#      cursor=db.cursor()
#      query ="""INSERT INTO flower(name,image,light,days,bloom) VALUES(?,?,?,?,?); """
#      cursor.executemany(query,flower_info)
#      db.commit()




#Adding data to a table "submit"________________________________________________________________
#with sqlite3.connect('db/datebase.db') as db:
    #cursor=db.cursor()
    #query1 ="""INSERT INTO submit(id,name_s,date_s) VALUES(1,'aloe','06-02-2023'); """
    #cursor.execute(query1)
    #db.commit()

#_______________________________________________________________________________________________
#Create a table for languages "lang":
#with sqlite3.connect('db/datebase.db') as db:
    #cursor=db.cursor()
    #query="""CREATE TABLE IF NOT EXISTS lang(l_id INTEGER,l_name TEXT,l_en TEXT,l_ru TEXT)"""
    #cursor.execute(query)

#Entering button names in English and Russian (so far in 2 languages) into the table "lang":
#l_info=[
#         ('l_flower_text','Select flower','Выберите цветок'),
#         ('l_date_last','Select last watering','Выберите  последний день полива'),
#         ('btn_submit','Submit','Отправить'),
#         ('l_light_text','Lighting','Тип освещения'),
#         ('l_date_next','Next watering','Дата следующего полива'),
#         ('l_bloom','Month bloom','Месяц цветения'),
#         ('l_head_id','id','Номер'),
#         ('l_head_name','name','Название'),
#         ('l_head_image','image','Изображение'),
#         ('l_head_light','light','тип освещения'),
#         ('l_head_days','days','дни'),
#         ('l_head_bloom','bloom','месяц цветения')
#         ('l_name_app','My flower','Мой цветок')
#          ]
# with sqlite3.connect('db/datebase.db') as db:
#     cursor=db.cursor()
#     query1 ="""INSERT INTO lang(l_name,l_en,l_ru) VALUES(?,?,?); """
#     cursor.executemany(query1,l_info)
#     db.commit()
#_______________________________________________________________________________________________
#Create table "flower_copy":
# with sqlite3.connect('db/datebase.db') as db:
    # cursor=db.cursor()
    # query="""CREATE TABLE IF NOT EXISTS flower_copy(id INTEGER,name_id TEXT,name TEXT,image TEXT,light TEXT,days INTEGER,bloom TEXT)"""
    # cursor.execute(query)


#Entering button names in English and Russian (so far in 2 languages) into the table "flower_copy":
# l_info=[
#         ('name_en','euharis', 'im/euharis.png', 'west-east', 5, 'febrary'),
#         ('name_ru','эухарис', 'im/euharis.png', 'запад-восток', 5, 'февраль'),
#
#         ('name_en','aloe', 'im/aloe.png', 'west-east-nord', 6, 'not bloom'),
#         ('name_ru', 'алоэ','im/aloe.png', 'запад-восток-север', 6, 'не цветет'),
#
#         ('name_en','orchid', 'im/orchid.png', 'west-south', 7, 'march-july'),
#         ('name_ru','орхидея', 'im/orchid.png', 'запад-юг', 5, 'март-июль'),
#
#         ('name_en','zamic', 'im/zamic.png', 'west-east', 10, 'august'),
#         ('name_ru','замиокулькас', 'im/zamic.png', 'запад-восток', 10, 'август'),
#
#         ('name_en','anturium', 'im/anturium.png', 'west-nord', 3, 'june'),
#         ('name_ru','антуриум', 'im/anturium.png', 'запад-север', 3, 'июнь'),
#
#         ('name_en','sinningia', 'im/sinningia.png', 'west', 4, 'april-august'),
#         ('name_ru', 'Синнингия', 'im/sinningia.png', 'запад', 4, 'апрель-август'),
#
#         ('name_en','pelargonium', 'im/pelargonium.png', 'west-south', 7, 'may-october'),
#         ('name_ru','пеларгония', 'im/pelargonium.png', 'запад-юг', 7, 'май -октябрь'),
#
#         ('name_en','narcissus', 'im/narcissus.png', 'south', 6, 'august'),
#         ('name_ru','нарцисс', 'im/narcissus.png', 'юг', 6, 'август'),
#
#         ('name_en','aglaonema', 'im/aglaonema.png', 'nord', 7, 'not bloom'),
#         ('name_ru','аглонема', 'im/aglaonema.png', 'север', 7, 'не цветет'),
#
#         ('name_en','calathea', 'im/calathea.png', 'nord', 5, 'not bloom'),
#         ('name_ru', 'калатея', 'im/calathea.png', 'север', 5, 'не цветет'),
#
#         ('name_en','nephrolepis', 'im/nephrolepis.png', 'west-nord', 3, 'not bloom'),
#         ('name_ru','нефролепис', 'im/nephrolepis.png', 'запад-север', 3, 'не цветет'),
#
#         ('name_en','hedera', 'im/hedera.png', 'west', 6, 'not bloom'),
#         ('name_ru', 'плющ', 'im/hedera.png', 'запад', 6, 'не цветет'),
#
#         ('name_en','hippeastrum', 'im/hippeastrum.png', 'west-south', 7, 'may-october'),
#         ('name_ru', 'гипераструм', 'im/hippeastrum.png', 'запад-юг', 7, 'май-октябрь')
#
#              ]
# with sqlite3.connect('db/datebase.db') as db:
#     cursor=db.cursor()
#     query1 ="""INSERT INTO flower_copy(name_id,name ,image ,light ,days ,bloom ) VALUES(?,?,?,?,?,?); """
#     cursor.executemany(query1,l_info)
#     db.commit()