greeting = input("greeting: ").strip()
if greeting.lower() == "hello":
    print("$0")
elif greeting.lower().startswith("hello "):
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")