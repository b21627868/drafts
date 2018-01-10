sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sozluk.keys())            #Ama eger bir sözlügün sadece anahtarlarını almak
print(sozluk.values())                               #isterseniz keys() metodundan yararlanabilirsiniz:
print(sozluk.items())

liste = list(sozluk.keys())
print(liste)


soru = input("Şehrinizin adını tamamı küçük harf olacak şekilde yazın:")
cevap = {"istanbul": "gök gürültülü ve sağanak yağışlı",
"ankara": "açık ve güneşli", "izmir": "bulutlu"}
print(cevap.get(soru, "Bu şehre ilişkin havadurumu bilgisi bulunmamaktadır.")) #Birinci argüman
                                                                               #sorgulamak istedigimiz sözlük ögesidir. Ikinci argüman ise bu ögenin sözlükte bulunmadıgı
                                                                               #durumda kullanıcıya hangi mesajın gösterilecegini belirtir. Buna göre, yukarıda yaptıgımız
                                                                               #sey, önce “sorgu” degiskenini sözlükte aramak, eger bu öge sözlükte bulunamıyorsa da
                                                                               #kullanıcıya, “Bu kelime veritabanımızda yoktur!” cümlesini göstermekten ibarettir

elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")
print(adresler)
print(adresler.pop("meyveler","yok ki silem"))                  #pop.item sözlükten rastgele eleman siler
adresler.setdefault("alex","fenerbahçe")
print(adresler)
adresler.setdefault("Ahmet","asfasfas")
print(adresler)

                                                                #Gördügünüz gibi, sözlükte zaten “meyveler” adlı bir anahtar bulundugu için, Python aynı
                                                                #adı tasıyan ama degerleri farklı olan yeni bir “meyveler” anahtarı olusturmadı. Demek ki
                                                                #bu metot yardımıyla bir sözlük içinde arama yapabiliyor, eger aradıgımız anahtar sözlükte
                                                                #yoksa, setdefault() metodu içinde belirttigimiz özellikleri tasıyan yeni bir anahtar-deger çifti olusturabiliyoruz