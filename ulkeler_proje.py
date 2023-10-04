import requests

class Ulkeler:
    def __init__(self) -> None:
        self.api_ulr = "http://hasanadiguzel.com.tr/api/countrycodes"

    def countryId(self,ulkeAdi):
        response = requests.get(self.api_ulr)
        response = response.json()
        veriler = response['data']
        for veri in veriler:
            if ulkeAdi in veri.values():
                countryID = veri['countryID']
                print(countryID)
                
    def country_phoneCode(self,ulkeAdi):
        response = requests.get(self.api_ulr)
        response = response.json()
        veriler = response['data']
        for veri in veriler:
            if ulkeAdi in veri.values():
                phoneCode = veri['phoneCode']
                print(phoneCode)
    
ulkeler = Ulkeler()

while True:
    secim = input("1-Ulke ID ogrenme\n2-Ulke telefon kodu ogrenme\n3-Çıkış\nSeçiminiz: ")
    
    if secim == '3':
        break
    elif secim == '1':
        ulkeAdi = input("Ülke adını giriniz: ")
        ulkeAdi = ulkeAdi.capitalize()
        ulkeler.countryId(ulkeAdi)
    elif secim == '2':
        ulkeAdi = input("Ülke adını giriniz: ")
        ulkeAdi = ulkeAdi.capitalize()
        ulkeler.country_phoneCode(ulkeAdi)
    else:
        print("yanlış secim")
    
    
    