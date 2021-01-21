
def print_hi(name):
    print(f' {name}')



if __name__ == '__main__':
    operation = input("Enter your math operation:"
                      "\ntype exit to exit calculator\n")

    if(operation == 'exit') :
        print_hi("Thank you for using my calulator")

    else :
        print_hi([x for x in operation])


