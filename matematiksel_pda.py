# matematiksel_pda.py
# Bu dosya, PDAService soyut sınıfından türeyen ve matematiksel ifadeleri kontrol eden sınıfı içerir.

from pda_service import PDAService

class MatematikselPDA(PDAService):
    def __init__(self):
        super().__init__()

    def process_character(self, char):
        print(f"Mevcut Durum: {self.state}, Yığın: {self.stack}, İşlenen Karakter: {char}")

        if self.state == 'baslangic':
            if char.isdigit():
                self.state = 'sayi'
            elif char == '(':
                self.stack.append('(')
            else:
                print("Hata: Başlangıç durumunda geçersiz karakter")
                return False

        elif self.state == 'sayi':
            if char in '+-*/':
                self.state = 'operator'
            elif char == ')':
                if not self.stack or self.stack.pop() != '(':
                    print("Hata: Sayı durumunda eşleşmeyen parantez")
                    return False
                self.state = 'sayi'
            elif char == '(':
                self.stack.append('(')
                self.state = 'baslangic'
            else:
                print("Hata: Sayı durumunda geçersiz karakter")
                return False

        elif self.state == 'operator':
            if char.isdigit():
                self.state = 'sayi'
            elif char == '(':
                self.stack.append('(')
                self.state = 'baslangic'
            else:
                print("Hata: Operatör durumunda geçersiz karakter")
                return False

        return True
