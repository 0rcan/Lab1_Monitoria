# JOSUE JACINTO ZAMBRANO LOAIZA 2380741-3743
# ALEJANDRO SIERRA
# LAB 1 MONITORIA GRUPO 52
#CAJERO AUTOMATICO

def card(number):
    tarjetas = [ {"numero": "1234567890", "clave": "1234", "saldo": 10000},
        {"numero": "0987654321", "clave": "4321", "saldo": 5000},
        {"numero": "5678901234", "clave": "5678", "saldo": 20000}
    ]
    
    for tarjeta in tarjetas:
        if number == tarjeta["numero"]:
            print("Card found.")
            key = input("\n Enter your key: ")
            if key == tarjeta["clave"]:
                if tarjeta["saldo"] >= 10000:
                    withdraw = int(input("\n Enter your balance to withdraw: "))
                    if withdraw <= tarjeta["saldo"]:
                        tarjeta["saldo"] -= withdraw
                        print(f"\n Was given to him {withdraw}")
                        print("your courrent actual is: ",tarjeta["saldo"])
                    else:
                        print("\n Insufficient balance.")
                else:
                    print("\n Minimum balance requirement not met.")
            else:
                print("\n Incorrect key.")
            break
    else:
        print("\n Card not found.")

if __name__ == '__main__':
    number = input("\n Enter your card number: ")
    card(number)


