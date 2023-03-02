# COMMAND LINE CALCULATOR
def get_choice():
    return input("Enter a valid expression(q to exit): ")

def evaluate():
    while True:
        try:
            result = get_choice()
            if result == 'q':
                break

            print(eval(result))
        except:
            pass

if __name__ == "__main__":
    evaluate()