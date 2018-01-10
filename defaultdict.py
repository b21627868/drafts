import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for leb in s:
    print(leb[1])
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)   #k ler ilk tupleın elemanları ve onları key olarak alıyo ve v leride liste olarak onların dictionarysi yapıyo
    print(d)
list(d.items())
print(d)


s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
  d[k] += 1   #k missisipinin harfleri oluyo ve k leri key olarak defaultdict in içine atıyo k aynı olunca +1 ekliyo hiç yoksa ve ilk defa geliyosa gene 1 ekliyo
  print(d)

list(d.items())


