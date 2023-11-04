"""
================HESAP MAKİNESİ===========
toplama işlemi yap
+?kullanıcı kaç rakam toplayıcağını yazsın
kullanıcı C tuşu ile programı kapatsın
işlem bitince program başa dönsün
=========================================

==================NOTLAR=================
int => sayı
str => kelimeler(stringin küçük hali char)
Kültür değişkenleri : x,i
+? : işlem yapıldı ama bitmedi
döngü türleri => while, for,doswitch
[] => dizi ya da liste demek
append(): Bu yöntem, bir listenin sonuna yeni bir eleman ekler.
bir değişken tanımlandıktan sonra tekarar tanımlanmaz ise hep aynı değerdir.
#for eleman in a:
#    print(eleman)
Eğer dışarıya iş yapıyorsan sadece istenileni öznel iş yapıyorsan geliştirmeler dahil kodla

===============ADIMLAR===================
1)Kullanıcıya soru sor (Kaç sayı gireceksin?) (C yazarsa dur)
2)Kullanıcıdan giriş talep et (sayı giriniz:)
3)Talep edilen sayıyı diziye ekle
4)Dizi içerisinde elemanları dön ve topla
5)Ekrana yazdır (Sonuç)
6)Başa dön
"""

#==============================================
sayi = 0
adet = 0 #kaç sayı toplanacak
sum = 0 #toplam
x = 0 #döngü
sayilar = [] #sayiların girildiği liste
controller = True #boolean (True/False)

#TANIMLAMALAR
kacsayi = "Kaç sayı toplamak istiyorsun?: \n"

#==============================================
while(controller):
    adet = input(print(kacsayi))
    if(adet=="c"):
        print("Stoped")
        controller = False
    else:
        adet = int(adet)
        while(x<adet): 
            x = x+1 
            sayi = int(input("Sayı giriniz: ")) 
            sayilar.append(sayi) 
        x=0
        for x in sayilar:
            sum =sum + x
        print(sum)






"""
while(x<adet):
    x = x+1
    print(x)    
sayilar= []

int(input(print("Lütfen sayı giriniz: \n")))
sayilar.append(x)
print(sayilar)
"""