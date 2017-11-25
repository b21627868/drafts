kisiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                                "Meslek" : "Öğretmen",
                                   "Yaş" : 34},             #sıra diye bir şey yok sözlüklerde
             "Mehmet Yağız" : {"Memleket": "Adana",
                                "Meslek" : "Mühendis",
                                   "Yaş" : 40},
              "Seda Bayrak" : {"Memleket": "İskenderun",
                                "Meslek" : "Doktor",
                                   "Yaş" : 30}}

print(kisiler["Mehmet Yağız"]["Memleket"])
print(kisiler["Seda Bayrak"]["Yaş"])
print(kisiler["Ahmet Özkoparan"]["Meslek"])
                                                                #listelerin sözlüğü olmaz çümkü listeler değiştirilebilir.
                                                                #listeleri bir string yada int e sözlğk yapabiliriz ama
kobe = {}
kobe["takım"]="lakers"
kobe["numara"]="24"
kobe["sayı"]="81"
kobe["alakasız"]=[1,2,4,45,5,"helo"]
kobe[1]= "3"
kobe[2]= 89
#kobe[[88,"alex,23",12]]=("tupple")
print(kobe)
