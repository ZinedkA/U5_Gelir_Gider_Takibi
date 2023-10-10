import os
class Muhasebe:
    def __init__(oz):
        # Başlangıçta bakiye, gelir ve çıkış sıfıra ayarlanıyor.
        oz.bakiye = 0
        oz.girdi = 0
        oz.cikti = 0
#-----------------------------------------------------------------------------------------------
    def maas(oz, miktar):
        # Maaş fonksiyonu: Gelir olarak eklenen miktar, girdiye eklenir.
        oz.girdi += miktar
#-----------------------------------------------------------------------------------------------
    def cikis(oz, miktar):
        # Çıkış fonksiyonu: Harcamalar olarak eklenen miktar, çıkışa eklenir.
        oz.cikti -= miktar        
#-----------------------------------------------------------------------------------------------
    def gelir_ekle(oz, miktar):
        # Gelir ekleme fonksiyonu: Bakiye, gelir ve toplam gelir güncellenir.
        oz.bakiye += miktar
        oz.girdi += miktar
        ekran_temizleme()
        print(f"\nToplam Para Girişi   : {oz.girdi}")
        print(f"Toplam para Çıkışı   : {abs(oz.cikti)}")
        print(f"Gelir eklendi. Bakiye: {oz.bakiye}")
        ifade(oz) 
#-----------------------------------------------------------------------------------------------
    def gider_ekle(oz, miktar):       
        # Gider ekleme fonksiyonu: Bakiye, çıkış ve toplam çıkış güncellenir.
        oz.bakiye -= miktar
        oz.cikti -= miktar
        ekran_temizleme()
        print(f"\nToplam Para Girişi   : {oz.girdi}")
        print(f"Toplam para Çıkışı   : {abs(oz.cikti)}")
        print(f"Gider eklendi. Bakiye: {oz.bakiye}")
        ifade(oz)
        if oz.bakiye < 0:
            print(f"\n! Harcamalarınıza Dikkat Edin !")        
#-----------------------------------------------------------------------------------------------
    def bakiye_sorgula(oz):
        # Bakiye sorgulama fonksiyonu: Mevcut bakiye ve toplam giriş ve çıkışı gösterir.
        ekran_temizleme()
        print(f"\nToplam Para Girişi   : {oz.girdi}")
        print(f"Toplam para Çıkışı   : {abs(oz.cikti)}")
        print(f"Mevcut Bakiyeniz     : {oz.bakiye}")
        ifade(oz)
#-----------------------------------------------------------------------------------------------
def ekran_temizleme():
    # Ekranı temizleme fonksiyonu: Ekranı temizlemek için kullanılır.
    os.system('cls')
#-----------------------------------------------------------------------------------------------
def ifade(oz):
    # İfade fonksiyonu: Bakiye durumuna göre ifadeyi gösterir.
    if oz.bakiye > 0:
        print(f":)")
    elif oz.bakiye == 0:
        print(f":|")
    else:
        print(f":(")
#-----------------------------------------------------------------------------------------------
def main():
    muhasebe_programi = Muhasebe()    
    while True:
        print("\n1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Sorgula")
        print("4. Çıkış")
        secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")
        if secim == "1":
            miktar = float(input("Gelir miktarını girin: "))
            muhasebe_programi.gelir_ekle(miktar)          
        elif secim == "2":
            miktar = float(input("Gider miktarını girin: "))
            ekran_temizleme()
            muhasebe_programi.gider_ekle(miktar)
        elif secim == "3":
            muhasebe_programi.bakiye_sorgula()
        elif secim == "4":
            print("Programdan çıkılıyor.")
            break
        else:
            ekran_temizleme()
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
