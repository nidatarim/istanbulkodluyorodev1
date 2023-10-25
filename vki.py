# 1) Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle endeksini hesaplayınız.
# Vücut kitle endeksi hesaplama formülü : ağırlık/ (boy*boy)

agirlik=float (input("Lütfen ağırlığınızı giriniz(kg): "))
boy=float(input("Lütfen boyunuzu giriniz (m): "))
VKİ = agirlik / (boy **2)
print("VKİ değeriniz: ", VKİ)
print ("VKİ değerinizin 30 ve üzeri olması durumunda bir doktora görünebilirsiniz")

