# manage.py
# Kullanıcıdan giriş alan ve bu girişin geçerli olup olmadığını kontrol eden ana dosya

from matematiksel_pda import MatematikselPDA
from calculate.calculator import evaluate_expression

def main():
    while True:
        expression = input("Lütfen bir matematiksel ifade girin (çıkmak için 'q' tuşlayın): ")
        if expression.lower() == 'q':
            break
        elif expression.strip() == '':
            print("Bu bir matematiksel ifade değildir.")
            continue
        
        pda = MatematikselPDA()
        
        if pda.validate_expression(expression):
            print(f"İfade geçerli: {expression}")
            result = evaluate_expression(expression)
            if result is not None:
                print(f"İfadenin sonucu: {result}")
        else:
            print("İfade geçersiz.")

if __name__ == "__main__":
    main()
