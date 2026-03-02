greeting = input("Greeting: ")

greeting = greeting.strip().lower()

if greeting.startswith("hello") or greeting.startswith("Hello"):
    print("You get 0$")
elif greeting.startswith("h") or greeting.startswith("H"):
    print("You get 20$")
else:
    print("You get 100$")