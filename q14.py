products = {}

while True:
    print("\n--- Product Menu ---")
    print("1. Add a new product")
    print("2. Update price of existing product")
    print("3. Find products in a price range")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter product name: ").lower()
        price = float(input("Enter product price: "))
        if name in products:
            print("Product already exists.")
        else:
            products[name] = price
            print("Product added.")

    elif choice == '2':
        name = input("Enter product name to update: ").lower()
        if name in products:
            new_price = float(input("Enter new price: "))
            products[name] = new_price
            print("Price updated.")
        else:
            print("Product not found.")

    elif choice == '3':
        low = float(input("Enter minimum price: "))
        high = float(input("Enter maximum price: "))
        print("\nProducts in the given price range:")
        found = False
        for name, price in products.items():
            if low <= price <= high:
                print(f"{name} : ${price}")
                found = True
        if not found:
            print("No products found in this range.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")