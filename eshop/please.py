


# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
#
# salom_ber()


# student = {
#     'ism': 'MuhammadYusuf',
#     'familya': 'Mahmudov',
#     'yosh': 20,
#     'fakultet': 'RvaM',
# }
# for k, q in student.items():
#     print(f"{k}")
#     print(f"{q}")

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }
#
# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }
#
# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }
#
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
#
# print(cars[0])

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone 12 pro max'
#     }
#
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
#
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# student_225 = {'ism':'Yusuf','yil':2003,'kurs':3}
# print(f"Yotoqxonada {student_225['ism'].title()} ismi {student_225['yil']} da tug'ilgan {student_225['kurs']}-kurs bola yashaydi")

# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')


# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism = ['Temur', 'Jamshid', 'Jaloldin', 'Feruzbek', 'Alimardon']
# for n in ism:
#     n = input("Ismingiz nima>> ")
#     if n == 'Temur':
#         print("Assalomu Alaykum")
#     else:
#         print("Siz emas")


# number = list(range(1, 25))
# number_sqtr = []
# for sqrt in number:
#     number_sqtr.append(sqrt ** 2)
# print(f"{sqrt ** 2} <<")
# print(number_sqtr)

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#
# print(sonlar)
# print(sonlar_kvadrati)

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# phones = {
#     'ali': 'iphoneX',
#     'olim': 'samsung',
#     'bek': 'realme',
# }
# for k,q in phones.items():
#     print(f"{k.title()} ning telfoni {q}")

# phones = {
#     'ali': 'iphoneX',
#     'olim': 'samsung',
#     'bek': 'realme',
# }
# phone = phones['ali']
# print(f"Alining telfoni {phone}")
# tel= phones.get('ali','Bunday odam yoq')
# print(tel)

# ism = input('Ismingiz nima? \n>>> ')
# if ism.lower() != 'ali':
#     print(f"Uzr,{ism.title()} o'ylab keling")
# else:
#     print("Ha mujiki")

# dostlar=[]
# print("5 ta eng yaqin do'stingizni kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting!"))
# print(f"{dostlar} - eng yaqin do'stlariz")

# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# fruits = ['olma', 'anjir', 'shaftoli', 'o\'rik']
# print("Birinchi meva:", fruits[0])
# print(fruits)

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng")
