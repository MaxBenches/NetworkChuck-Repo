print("Hello, welcome to BigBench Coffee!")
name = input("\nWhat is your name?\n")

menu = "Black coffee, Espresso, Latte, Cappucino"


#if Ben comes in and is evil, and he has done more than 4 good deed, then he can come in
if name == "Loki":
    print("\nGet out " + name + "! You're not welcome here!")
    exit()
elif name == "Patricia":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("Get out you evil " + name + "! You are not welcome here!")
        exit()
    else:
        print("\nFinally a good " + name + "! Come on in!")
elif name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes" and name == "Ben":
        deed_status = int(input("How many good deeds have you done?\n"))
        if deed_status < 4:
            print("Get out you evil " + name + "! You're not welcome here!")
            exit()
        else:
            print("\nGreat, then you are welcome here!")
    else:
        print("\nFinally a good " + name + "! Come on in!")
else:
    print("\nHello " + name + ", thank you so much for coming in today.")


order = input("\nWhat would you like from our menu today? Here is what we're serving:\n\n" + menu + "\n")

if order == "Black coffee":
    price = 3
elif order == "Espresso":
    price = 4
elif order == "Latte":
    whipped_cream_status = input("Would you like extra whipped cream?\n")
    if whipped_cream_status == "Yes":
        price = 7
    else:
        price = 5
elif order == "Cappucino":
    price = 6
else:
    print("\nSorry, we don't serve that here.")
    exit()


quantity = int(input("\nHow many coffees would you like?\n"))

total = price * int(quantity)
print("\nThat will be " + str(total) + "$, please.")

response = input()
if quantity > 1:
    print("\nThank you " + name + ", your " + str(quantity) + " " + order + "s will be ready in a moment.")
else:
    print("\nThank you " + name + ", your " + str(quantity) + " " + order + " will be ready in a moment.")
    exit()
#This is just a test