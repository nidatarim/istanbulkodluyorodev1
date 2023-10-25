# 2) Maaşı ve zam oranı girilen işcinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float (input ( "Lütfen güncel maaşınızı giriniz:"))
zamOrani = float(input ("Lütfen Zam oranınızı giriniz (%) :"))
yeniMaas= (maas * zamOrani /100 + maas)
print ("Zamlı maaşınız:", yeniMaas)

