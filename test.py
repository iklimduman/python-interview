# state machine class
class stateMachine(object):

    # main state holder
    mainState = 0

    # user input and calculation state
    def state_calculate(self):
        # math operators
        operators = ["+","-","*","/"]

        # get user input
        operation = input(  "Please enter an operation"
                            "\nType exit to exit calculator:   ")
        
        # temp variables
        var = ""
        clc = 0
        currentOperator = ""

        indexOfOperation = 0
        endOfOperation = len(operation)

        # exit?
        if operation == "exit":
            self.mainState = 1

        else:
            self.mainState = 0

            # check chars in user input
            for x in operation :

                indexOfOperation = indexOfOperation + 1

                # check if variable or operator
                isOperator = 0
                for y in operators :

                    # current char is an operator
                    if  x == y :
                        isOperator = 1

                        if currentOperator == "+":
                            clc = clc + int(var)
                            var = ""
                            
                        elif currentOperator == "-":
                            clc = clc - int(var)
                            var = ""

                        elif currentOperator == "*":
                            clc = clc * int(var)
                            var = ""

                        elif currentOperator == "/":
                            clc = clc / int(var)
                            var = ""

                        elif currentOperator == "":
                            clc = int(var)
                            var = ""
                        
                        currentOperator = x

                # current char is not an operator
                if isOperator == 0 :
                    var = var + x
                
                isOperator = 0

                # end of user input
                if indexOfOperation == endOfOperation :

                    if currentOperator == "+":
                        clc = clc + int(var)
                        var = ""
                        
                    elif currentOperator == "-":
                        clc = clc - int(var)
                        var = ""

                    elif currentOperator == "*":
                        clc = clc * int(var)
                        var = ""

                    elif currentOperator == "/":
                        clc = clc / int(var)
                        var = ""
            
            # print calculation
            print("Ans: " + str(clc))
            
    # exit state
    def state_exit(self):
        print("EXIT")
        self.mainState = 2

    # main states
    states = {
        0: state_calculate,
        1: state_exit
    }
    
    # main state handler
    def stateMachineHandler(self):
        while self.mainState != 2:
            func = self.states.get(self.mainState, "nothing")
            func(self)


# === Actual Code === #

# create object
smObj = stateMachine()

# run
smObj.stateMachineHandler()



