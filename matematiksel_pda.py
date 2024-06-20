from pda_service import PDAService

class MatematikselPDA(PDAService):
    def __init__(self):
        super().__init__()

    def process_character(self, char):
        print(f"Mevcut Durum: {self.state}, Yığın: {self.stack}, İşlenen Karakter: {char}")

        if self.state == 'q0':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
            else:
                print("Hata: Başlangıç durumunda geçersiz karakter")
                return False

        elif self.state == 'q1':
            if char in '+-*/':
                self.state = 'q2'
            elif char == ')':
                if not self.stack or self.stack.pop() != '(':
                    print("Hata: Sayı durumundan eşleşmeyen parantez")
                    return False
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q0'
            else:
                print("Hata: Sayı durumundan geçersiz karakter")
                return False

        elif self.state == 'q2':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q0'
            else:
                print("Hata: Operatör durumunda geçersiz karakter")
                return False

        print(f"Yeni Durum: {self.state}, Yığın: {self.stack}")
        return True
