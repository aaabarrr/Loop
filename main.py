#looping (perulangan)
print("--------Cetak angka 1 sd 5-------")
anngka=5

for no in range(anngka):
    no = no + 1
    print("angka",no)

#Latihannn
print("\n")
print("------- Cetak 1 s/d 20----------")
angka1= 20
for yes in range(angka1):
    yes =yes+1
    print("angka",yes)

print("\n")
print("------- Cetak bilangan genap 1 s/d 20----------")

bill=20
for no in range(bill):
    no += 1
    if (no % 2 ==0):
        print("bilangan genap",no)

#Looping while
print("\n")
print("------- Cetak bilangan 10 s/d 15----------")
dor =10
while(dor <= 15):
    print("Bilangan ",dor)
    dor += 1    

print("\n")
print("------- Cetak bilangan 15 s/d 10----------")
dor =15
while(dor >= 10):
    print("Bilangan ",dor)
    dor -= 1    

#looping while dengan if dan operator modulus (sisa bagi) %
print("\n")
print("----------Bilangan Ganjil----------")

data= 1
while(data <= 5):
    if(data %2 ==1):
        print("bilangan ganjil",data)
    data +=1 

print("\n")
print("----------Bilangan Genap----------")

data= 1
while(data <= 5):
    if(data %2 ==0):
        print("bilangan ganjil",data)
    data +=1 


print("\n")
print("--------Nested loop -------")
#Nesteed Loop
for i in range(5):
    for j in range(i + 1):
        print("*", end = " " )
    print(" ")

print("----------------------------------------")
string = ""
bar = 1
#looping baris
while (bar <=5):
    kol = bar
#looping kolom
    while kol > 0:
        string += "*"
        kol = kol - 1
    string += "\n"
    bar = bar + 1
print(string)
print("----------------------------------------")
a = 6
for i in range(0,a):
    for j in range (0,a-1):
        print("*", end=" ")
    a -=1
    print(" ")
print("----------------------------------------")
a = 5
s = a-1
for i in range (0,a): #baris
    for j in range(0,s): #spasi
        print(" ", end=" ")
    s -=1
    for j in range (0, i + 1): #untuk bintang
        print(" & ", end=" ")
    print(" ")
