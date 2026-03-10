while True:
    print("MAIN MENU")
    print("1. Calculator")
    print("2. Converter")
    print("3. Quick Quiz")
    print("4. Exit")
    print("="*30)
    n = int(input("Select an option (1-4): "))
    match n:
        case 1:
            print("CALCULATOR")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {num1} + {num2} = {num1 + num2}")        
        case 2:
            print("CONVERTER")
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            print(f)        
        case 3:
            print("QUICK QUIZ")
            answer = input("What is the capital of Azerbaijan? ").strip().lower()
            if answer == "baku":
                print("Correct!")
            else:
                print("Wrong. The correct answer is Baku.")      
        case 4:
            print("Exit the proqram!")
            break     
        case _:
            print("Please try again!")
