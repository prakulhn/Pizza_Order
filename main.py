print("Welcome to Python Pizza Hut!")
pizza_size = input("Enter the pizza size: Small(S/s), Medium(M/m), Large(L/l)? ")
bill = 0
if pizza_size == 'S' or pizza_size == 's':
    bill = 100
    print("Pizza Price: Rs.100")
elif pizza_size == 'M' or pizza_size == 'm':
    bill = 200
    print("Pizza Price: Rs.200")
elif pizza_size == 'L' or pizza_size == 'l':
    bill = 300
    print("Pizza Price: Rs.300")
pepperoni = input("Do you want pepperoni for the pizza: Yes(Y/y) / No(N/n)? ")
if pepperoni == 'Y' or pepperoni == 'y':
    if pizza_size == 'S' or pizza_size == 's':
        bill = bill + 30
        print("Pepperoni Price: Rs.30")
    elif pizza_size == 'M' or pizza_size == 'm' or pizza_size == 'L' or pizza_size == 'l':
        bill = bill + 50
        print("Pepperoni Price: Rs.50")
extra_cheese = input("Do you want extra cheese: Yes(Y/y) / No(N/n)? ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill = bill + 20
    print("Extra Cheese Price: Rs.20")
print(f"Net Payable = {bill} \nThank You, Visit Once Again!")


