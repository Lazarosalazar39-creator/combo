def greetings():
    print("hello world")

def orderPizza():
    # ask for size
    pizza_size= input("would you like 6, 8, or 10 slice pizza pie?")
    if pizza_size == "6":
        print("small pizza, comin up")
    elif pizza_size == "8":
        print("medium pizza, comin up")
    elif pizza_size == "10":
        print("large pizza, comin up")
    else:
        print("¿Que?")
    # TODO: ask for toppings
    print(pizza_size)

def main():
    greetings()
    orderPizza()


if __name__ == "__main__":
    main()

# if fav_color
# print (the sky sure is blue today)
# elif fav_color ==purlple":
# print ("roll pirates roll)" \
# "elif fav_color ==red " \
# "print ("will you be my valentine?")")")
# print (:user's favorite color is "+fav_color )')