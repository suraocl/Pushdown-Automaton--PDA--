# calculate/calculator.py
# Bu dosya, matematiksel ifadelerin sonucunu hesaplayan fonksiyonu içerir.

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"İfade değerlendirilirken hata: {e}")
        return None
