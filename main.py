drinks={
        "espresso": {
            "inside":{
                "water": 50,
                "coffee": 18,
                "milk": 0
                    },
            "cost": 1.5
            },

        "latte":{
            "inside":{
                "water": 200,
                "coffee": 24,
                "milk": 150
                     },
            "cost": 2.5
            },
        "cappuccino":{
            "inside":{
                "water": 250,
                "coffee": 24,
                 "milk": 100
                },
            "cost": 3
            }
        }

sources={
"milk":1000,
"water":2000,
"coffee":100,
}
money=0
off_prompt=True
decision=""

#TODO:1 Print report
def remaining_function():
    remaining_milk = sources["milk"]
    remaining_water = sources["water"]
    remaining_coffee = sources["coffee"]
    print(f"Milk: {remaining_milk}" + "\n" + f"Water: {remaining_water}" + "\n" + f"Coffe: {remaining_coffee}" + "\n" + f"Money: ${money}")

#TODO:2 Check resources sufficient
def return_decision():
    return decision
def resources_sufficient():

    if sources["milk"]>=((drinks[return_decision()])["inside"])["milk"]:
        if sources["water"]>=((drinks[return_decision()])["inside"])["water"]:
            if sources["coffee"]>=((drinks[return_decision()])["inside"])["coffee"] :
                print(f"Report before purchasing {return_decision()}:")
                remaining_function()
                print("Enough sources to make the drink")
                should_pay = (drinks[return_decision()])["cost"]
                print(f"You should pay ${should_pay} for {return_decision()}")

                #print(f"Report after purchasing {return_decision()}:")
                #remaining_function()
            else:
                print("Sorry there is not enough coffe!")
        else:
            print("Sorry there is not enough water!")
    else:
        print("Sorry there is not enough milk!")

#TODO:3 Process coins
def coins_asking():
    print("Please insert the coins")
    global quarters,dimes,nickles,pennies
    quarters=int(input("How many quarters?"))
    dimes=int(input("How many dimes?"))
    nickles=int(input("How many nickles?"))
    pennies=int(input("How many pennies?"))
def coins_process(q:int,d:int,n:int,p:int):
    total_coins=float(0.25*q + 0.10*d + 0.05*n + 0.01*p)
    return total_coins

#TODO:4 Check transaction successful
def check_money():
    global sources
    global money
    if (coins_process(quarters,dimes,nickles,pennies))<(drinks[return_decision()])["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        if (coins_process(quarters,dimes,nickles,pennies))>(drinks[return_decision()])["cost"]:
            sources["milk"] -= ((drinks[return_decision()])["inside"])["milk"]
            sources["water"] -= ((drinks[return_decision()])["inside"])["water"]
            sources["coffee"] -= ((drinks[return_decision()])["inside"])["coffee"]
            money += (drinks[return_decision()])["cost"]
            change=(coins_process(quarters,dimes,nickles,pennies))-(drinks[return_decision()])["cost"]
            change=round(change,2)
            print(f"Here is ${change}")
        print(f"Here is your {return_decision()} ☕. Enjoy it!")

#TODO:5 Make coffee
def main():
    global off_prompt
    global drinks
    global sources
    global money
    global decision

    while off_prompt==True:
        decision = input("What would you like? (espresso/latte/cappuccino): ")
        if decision == "report":
            remaining_function()
        elif decision == "off":
            off_prompt = False
            print("Machine will be turn-off")
        elif decision=="latte" or decision=="espresso" or decision=="cappuccino":
            if off_prompt == True:
                return_decision()
                resources_sufficient()
                coins_asking()
                coins_process(quarters,dimes,nickles,pennies)
                check_money()
        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    main()

