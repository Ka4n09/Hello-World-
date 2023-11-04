"""
a = "python"
b = [1,2,3,4,5,6,7]
print(a[0])
print(a[4])
print(len(a))
print(len(b))

print(a[len(a)-1])

print(a[0:2])
print(a[2:])
print(a[:4])
print(b[2:])
print(b[:4])
print(b[::2])

a = {"Elma":3,"Armut":4,"Kiraz":5}
print(a["Elma"])
print(a["Armut"])
print(a["Kiraz"])

yas = input("Yaşınızı Girin:")
print("Yaşınız",yas )

a = input("a:")
b = input("b:")
c = input("c:")
print("toplam",a+b+c)
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("toplam",a+b+c)
"""
yas = int(input("yaşınızı giriniz:"))
if yas <18:
    print("mekana giremezsiniz...")
else:
    print("hoşgeldiniz")
   
    
    <
    >
    <=
    >=
    == iki değer eşitse true değilse false değer 
    != eşit değilse 
   

islem = int(input("işlem giriniz:"))

if islem == 1:
    print("işlem 1'i seçtiniz...")
elif islem == 2:
     print("işlem 2'i seçtiniz...")
elif islem == 3: 
    print("işlem 3'ü seçtiniz...")
else:
    print("geçersiz işlem")

a = 3 
b = 4 
if a == 3 and b == 4:
    print("evet")
else:
    print("hayır")

a = 3 
b = 4 
if a == 3 and b == 5:
    print("evet")
else:
    print("hayır")

a = 3 
b = 4 
if a == 3 or b == 5:
    print("evet")
else:
    print("hayır")

if (not(3 == 4)):
    print("evet")

i = 1
while i < 10:
    print ("i:",i)
    i = i + 1

i = 1

while i < 10:
    print ("i:",i)
    i += 1

i = 1

while i < 1000:
    print ("i:",i)
    i *= 2


i = 0

while(i < 10):
    if i == 5:
        break
    print("i:",i)
    i += 1   

i = 0

while(i < 10):
    if i == 3 or i == 5:
        i += 1
        continue
    print("i:",i)
    i += 1 

a = [1,2,3,4,5,6]
for eleman in a:
    print(eleman)


b = "python"
for karakter in b:
    print(karakter)

for sayı in range(10,100,20):
    print(sayı)

def selamla():
    print("Merhaba")
    print("Nasılsın ?")
selamla()

def selamla(isim):
    print("merhaba",isim)

selamla("murat")
selamla("ayşe")

def selamla(isim = "isimsiz"):
    print("merhaba", isim)

selamla()
selamla("murat")

def toplama(a,b,c):
    print("toplam:",a+b+c)

toplama(3,4,5)

def toplama (a,b,c):
    return a+b+c
toplam = toplama (3,4,5)

print(toplam)

liste = (1,2,3,4,5,6)
a = "araba"
print (a.startswith ("ar"))

liste = (1,2,3,4,5,6)
a = "araba"
print (a.endswith ("a"))

liste = (1,2,3,4,5,6)
a = "araba"

a = a.replace("a","o")
print(a)

liste = [1,2,3,4,5,6]
liste.append("Pyhton")
print(liste)

liste = [1,2,3,4,5,6]
liste.pop(0)
print(liste)

file = open("dosya.txt","a")

file.write("naber Python\n")
file.write("naber java\n")
file.write("naber C++\n")

file.close()

file = open("dosya.txt","r")

veri = file.read(10)
print(veri)

file.close()

file = open("dosya.txt","r")
file.seek(10)
veri = file.read(10)
print(veri)

file.close()

file = open("dosya.txt","r")

for satir in file:
    print(satir)
file.close()

class account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapBilgileri(self):
        print("self ",self.isim)
        print("numara ",self.numara)
        print("bakiye ",self.bakiye)
    def paraÇek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("bakiyeniz yeterli değil...")
        else:
            self.bakiye -= miktar
        print ("Yeni bakiye:",self.bakiye)
    def ParaYatır(self,miktar):
        self.bakiye += miktar
        print("Yeni Bakiye:",self.bakiye)

account = account("Kaan Kırmacı",123456,1000)
account.hesapBilgileri()

account.paraÇek(500)
account.ParaYatır(0)
"""









