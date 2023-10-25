# 5) Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi = input ("Lütfen bir sayı giriniz: ")
palindromSayi = sayi[::-1]
if sayi == palindromSayi :
   print("Girdiğiniz sayı palindrom sayısıdır.")
else:
   print("Girdiğiniz sayı palindrom sayısı değildir.")


