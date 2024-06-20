
def ifadeyi_degerlendir(ifade):
    try:
        sonuc = eval(ifade)
        return sonuc
    except Exception as e:
        # Hata durumu ve None döndür
        print(f"İfade değerlendirilirken hata: {e}")
        return None
