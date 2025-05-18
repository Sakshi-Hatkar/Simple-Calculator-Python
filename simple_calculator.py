while(True):
    try:
        a = int(input("enter a num:  "))
        if(a==0):
            break
        b = int(input("enter a num:  "))
        if(b==0):
            break
        print("Enter the operation you want to perform\nPress + for add\nPress - for sub\nPress * for multiply\nPress / for divide")
        o = input("Enter operation: ")
        match o:
            case "+":
                print(f"The sum is {a+b}")
            case "-":
                print(f"The subtract is {a-b}")
            case "*":
                print(f"The multiply is {a*b}")
            case "/":
                print(f"The divide is {a/b}")
            case _:
                print("Error")

    except Exception as e:
        print("Invalid input",e)
