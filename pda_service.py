#soyut sınıf

from abc import ABC, abstractmethod

class PDAService(ABC):
    def __init__(self):
        self.stack = []  # Yığın veri yapısı
        self.state = 'q0'  # Başlangıç durumu

    @abstractmethod
    def process_character(self, char):
        pass

    def ifadeyi_dogrula(self, ifade):
        # İfadeyi karakter karakter işle
        for char in ifade:
            if not self.process_character(char):
                print("İfade geçersiz.")
                return False
        # Son durumda yığın boş olmalı ve geçerli durumda olmalı
        if self.state != 'q1' or self.stack:
            print("Hata: Tamamlanmamış ifade veya eşleşmeyen parantez.")
            print(f"Son Durum: {self.state}, Yığın: {self.stack}")
            return False
        print("İfade geçerli.")
        return True
