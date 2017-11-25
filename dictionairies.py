sozluk = {}
print(type(sozluk))

kelimeler = {"kitap": "book"}
print(len(kelimeler))

sozluk = {"kitap" : "book",
     "bilgisayar" : "computer",
     "programlama": "programming",
            "dil" : "language",
         "defter" : "notebook"}

sozluk_1 = {"kitap": "book", "bilgisayar": "computer", "programlama": "programming",
"dil": "language", "defter": "notebook"}

print(sozluk["kitap"])
print(sozluk["bilgisayar"])
#print(sozluk["leonardo"])  hata verir çünkü leonardo indexli bir değer yok

telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                    "eda ala" : "0212 212 12 12"}
kisi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")
if kisi in telefon_defteri:
        cevap = "{} adlı kişinin telefon numarası: {}"
        print(cevap.format(kisi, telefon_defteri[kisi]))
else:
    print("Aradığınız kişi telefon rehberinde yok!")

lebron = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
           "Mehmet Yağız" : ["Adana", "Mühendis", 40],
            "Seda Bayrak" : ["İskenderun", "Doktor", 30]}

print(lebron["Seda Bayrak"])