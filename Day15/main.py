MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "grounds" : 18,
            "milk" : 0
        },
        "cost": 1.5
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "grounds" : 24,
            "milk" : 150
        },
        "cost": 2.5
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "grounds" : 24,
            "milk" : 100
        },
        "cost" : 3.0
    },
}

resources = {
    "water" : 623,
    "milk" : 400,
    "grounds" : 76,
}

coins = {
    "pennies" : 0.01,
    "dimes" : 0.1,
    "quarters" : 0.25,
}

total_money = 0

def check_resources(action):
    enough_resuorces = True
    for key in resources:
        if MENU[action]['ingredients'][key] >= resources[key]:
            print(f"There is not enough {key}")
            enough_resuorces = False
        elif enough_resuorces==True:
            resources[key] = resources[key] - MENU[action]['ingredients'][key]
    if enough_resuorces == False:
       return False


def check_action (action):
    if action == "report":
        print(f"Water:  {resources['water']} ml")
        print(f"Milk:   {resources['milk']} ml")
        print(f"Coffee: {resources['grounds']} g")
        print(f"Total money: ${total_money}")
        return 3
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        return 1
    elif action == "exit":
        return 0
    else:
        return 2

running = True

while running:
    action = input("what would you like to have (espresso/latte/cappuccino)?")
    
    action_type = check_action(action)

    if action_type == 1: #Valid coffee
        if check_resources(action) == False:
            continue
    elif action_type == 0: #exit
        break
    elif action_type == 3: #report
        continue
    else: #Invalid response
        print("You have not typed a valid response.")
        continue
    

    total_paid = 0;
    for key in coins:
        total_paid += float(input(f"How many {key} are you paying? "))*coins[key]
        print(total_paid)
    
    if total_paid == MENU[action]['cost']:
        print("enjoy your coffee")
        total_money += MENU[action]['cost']
    elif total_paid > MENU[action]['cost']:
        print(f"Enjoy your coffee, here's ${total_paid - MENU[action]['cost']}")
        total_money += MENU[action]['cost']
    elif total_paid < MENU[action]['cost']:
        print("You didn't put in enough money.")

    
    keep_running = str(input("Do you want to try again/get another coffee? (y/n)"))
    if keep_running == "y":
        continue
    else:
        break
