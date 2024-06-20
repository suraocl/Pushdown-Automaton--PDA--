# calculate/calculator.py
# Bu dosya, matematiksel ifadelerin sonucunu hesaplayan fonksiyonu içerir.

def ifadeyi_degerlendir(ifade):
    try:
        # İfadeyi değerlendir ve sonucu döndür
        sonuc = eval(ifade)
        return sonuc
    except Exception as e:
        # Hata durumunda mesaj yazdır ve None döndür
        print(f"İfade değerlendirilirken hata: {e}")
        return None
