# pda_service.py
# Bu dosya, Pushdown Automaton (PDA) simülasyonunu gerçekleştiren soyut sınıfı içerir.

from abc import ABC, abstractmethod

class PDAService(ABC):
    def __init__(self):
        self.stack = []  # Yığın veri yapısı
        self.state = 'baslangic'  # Başlangıç durumu

    @abstractmethod
    def process_character(self, char):
        pass

    def validate_expression(self, expression):
        for char in expression:
            if not self.process_character(char):
                print("İfade geçersiz.")
                return False
        if self.state != 'sayi' or self.stack:
            print("Hata: Tamamlanmamış ifade veya eşleşmeyen parantez.")
            print(f"Son Durum: {self.state}, Yığın: {self.stack}")
            return False
        print("İfade geçerli.")
        return True
