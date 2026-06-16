# string contact
ad = "eymen tuğra"
soyad = "sarı"
yas = 17

# msj = "My name is " + ad + " " + soyad + "." + "I'm " + str(yas) + " years old."
# string format
# msj = "My name {} {}. I'm {} years old.".format(ad, soyad, yas)
# msj = "My name {1} {0}. I'm {2} years old.".format(ad, soyad, yas)
msj = "My name {a} {s}. I'm {y} years old.".format(a=ad, s=soyad, y=yas)

# f-string
msj = f"My name {ad} {soyad}. I'm {yas} years old.".format(ad, soyad, yas)



print(msj)