# COFFEEFLOW - QUAN LY QUAN CA PHE

menu = {
    "Ca phe den": 20000,
    "Ca phe sua": 25000,
    "Bac xiu": 30000,
    "Tra sua": 35000
}

orders = []


def show_menu():
    print("\n--- MENU ---")
    for name, price in menu.items():
        print(f"{name}: {price:,} VND")


def create_order():
    show_menu()
    name = input("Nhap ten mon: ")

    if name in menu:
        quantity = int(input("Nhap so luong: "))
        if quantity > 0:
            total = menu[name] * quantity
            orders.append(total)
            print(f"Thanh tien: {total:,} VND")
        else:
            print("So luong khong hop le!")
    else:
        print("Mon khong ton tai!")


def show_orders():
    print("\n--- DANH SACH DON HANG ---")
    for i, total in enumerate(orders, 1):
        print(f"Don hang {i}: {total:,} VND")


def show_revenue():
    print(f"\nTong doanh thu: {sum(orders):,} VND")


while True:
    print("\n===== COFFEEFLOW =====")
    print("1. Xem menu")
    print("2. Tao don hang")
    print("3. Xem don hang")
    print("4. Xem doanh thu")
    print("0. Thoat")

    choice = input("Lua chon: ")

    if choice == "1":
        show_menu()
    elif choice == "2":
        create_order()
    elif choice == "3":
        show_orders()
    elif choice == "4":
        show_revenue()
    elif choice == "0":
        print("Cam on ban da su dung CoffeeFlow!")
        break
    else:
        print("Lua chon khong hop le!")
