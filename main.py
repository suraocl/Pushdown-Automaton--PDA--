from matematiksel_pda import MatematikselPDA
from calculate.calculator import ifadeyi_degerlendir

def main():
    while True:
        ifade = input("Lütfen bir matematiksel ifade girin (çıkmak için '1' tuşlayın.): ")
        if ifade == '1':
            break
        elif ifade.strip() == '':
            print("Bu bir matematiksel ifade değildir.")
            continue

        pda = MatematikselPDA()
    
        if pda.ifadeyi_dogrula(ifade):
            print(f"İfade geçerli: {ifade}")
            sonuc = ifadeyi_degerlendir(ifade)
            if sonuc is not None:
                print(f"İfadenin sonucu: {sonuc}")
        else:
            print("İfade geçersiz.")

if __name__ == "__main__":
    main()
