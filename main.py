#1-misol
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

print("Eng katta son:", max(a, b, c))

#2-misol
yil = int(input("Yilni kiriting: "))

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Kabisa yili")
else:
    print("Oddiy yil")

#3-misol
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

print("Eng kichik son:", min(a, b, c))

#4-misol
raqam = int(input("Raqam kiriting: "))

if raqam == 0:
    print("0")
elif raqam == 1:
    print("1")
else:
    print("Boshqa raqam")

#5-misol
a = float(input("1-tomonni kiriting: "))
b = float(input("2-tomonni kiriting: "))

if a == b:
    print("Kvadrat")
else:
    print("To'rtburchak")

#6-misol
son = float(input("Son kiriting: "))

if son <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")
