l=[1,2,3,4]
l1=[53,32,23,1,24,2]
l2= [12,6,42,6,2,16,3]
l3 = l2 #deep copy yapar normal copyden farkı eleman ekleyince yada silince diğerinden de silinir eğer copy yaparsan hangi listeden silersen diğer listeyi etkilemez
print(l3)
l2.append(1231)
print(l3)
print(l2)
l.extend(l1)
print(l)
print(l1)
l2.append(l1)
print(l2)

liste = [["Ahmet", "Mehmet", "Ayşe"],
["Sedat", "Serkan", "Selin"],
["Zeynep", "Nur", "Eda"]]

print(liste[0][0])
print(max(l,l2))