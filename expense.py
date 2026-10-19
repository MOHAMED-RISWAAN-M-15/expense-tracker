import json
def main():
    global expenses
    try:
        with open("expense.json","r") as file:
            expenses=json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        expenses=[]
    match_choice()
def add_expense():
    while True:
        try:
            category=input("Enter a Category (Food/Travel/Shopping...): ").lower().strip()
            name=input("Enter a Expense Name: ").lower().strip()
            if name=="" or category=="":
                raise ValueError
        except ValueError:
            print("Invalid Name Or Category")
            continue
        try:
            amount=float(input("Enter a amount:"))
            if amount<0:
                raise ValueError
            break
        except ValueError:
            print("invalid amount ,Amount can't be negative or string")
        
    expenses.append({"name":name,"amount":amount,"category":category})
    with open("expense.json","w") as wfile:
        json.dump(expenses,wfile,indent=4)
def view_expense():
    if not expenses:
        print("No Expense Found.")
    else:
        print("Your Expenses")
        for expense in expenses:
            print(expense['name'],expense['amount'],expense.get('category','uncategorized'),sep=" - ")
def view_Total():
    if not expenses:
        print("No Expense Found.")
        return
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print("Total:",total)
def view_categories_total():
    if not expenses:
        print("No Expense Found.")
    else:
        category_total={}
        for expense in expenses:
            category=expense["category"]
            amount=expense["amount"]
            if category in category_total:
                category_total[category]+=amount
            # if food (category) exist amount increase "food":150 something
            # if not exist it create food with amount{"food":amount}
            # if another exist it increase the value(amount)
            # if doesn't exist then it create key(with name of that category) and assing the amount as a value 
            else:
                category_total[category]=amount
        for catogries,total_of in category_total.items():
            # items() unpack thepair into two variable catogries get food , total_of gets 200
            print(f"{catogries} - {total_of}")
def delete_expense():
    if not expenses:
        print("No Expense Found.")
    else:
        for index,value in enumerate(expenses,start=1):
            print(f"{index}.{value['name']}-{value['amount']}-{value['category']}")
        while True:
            try:
                choice=int(input("Enter a expense number to delete: "))
                
                if 1<=choice<=len(expenses):
                    delete=expenses.pop(choice-1)
                    with open("expense.json","w") as wfile:
                        json.dump(expenses,wfile,indent=4)
                    print(f"Deleted {delete['name']}")
                    break
                else:
                    print("Invalid expense number")
                
            except ValueError:
                print("Please Enter a valid number")
def edit_expense():
    if not expenses:
        print("No Expense Found.")
    else:
        for index,value in enumerate(expenses,start=1):
            print(f"{index}.{value['name']}-{value['amount']}-{value['category']}")
        while True:
            try:
                choice=int(input("Enter a Expense Number To Edit: "))
                
                if 1<=choice<=len(expenses):
                    expense=expenses[choice-1]
                    # list is mutubale dont need to insert or append coze expenses[0]="changed" it  directly change that index element value 
                    # it's like replace
                    while True:
                        try:
                            category=input("enter a category (Food/Travel/Shopping...): ").lower().strip()
                            name=input("Enter a Expense Name: ").lower().strip()
                            if name=="" or category=="":
                                raise ValueError
                        except ValueError:
                            print("Invalid Name Or Category")
                            continue
                        
                        expense['category']=category
                        expense['name']=name
                        break
                    while True:
                        try:
                            amount=float(input("Enter a amount:"))
                            if amount<0:
                                raise ValueError
                            expense['amount']=amount
                            with open("expense.json","w") as wfile:
                                json.dump(expenses,wfile,indent=4)
                            print("Expense Updated Successfully")
                            return 
                        # return from two loop
                        except ValueError:
                            print("Invalid amount ,Amount can't be negative or string")
                else:
                    print("Invalid expense number")
                    
            except ValueError:
                print("Please Enter a valid number")
                        
                    
                    
                    
def match_choice():
    while True:
        print("1. Add expense")
        print("2. view Expenses")
        print("3. View Total spending")
        print("4. View Catogries Total")
        print("5. Delete expense")
        print("6. Edit expense")
        print("7. Exit")
        choice=input("Choose an option:").lower().strip()
        match choice:
            case "1"|"add expense":
                add_expense()
            case "2"|"view expenses":
                view_expense()
            case "3"|"view total spending":
                view_Total()
            case "4"|"view catogries total":
                view_categories_total()
            case "5"|"delete expense":
                delete_expense()
            case "6"|"edit expense":
                edit_expense()
            case "7"|"exit":
                print("Exit")
                return
            case _:
                print("Invialid choice . Please Enter (1-7).")
                
    
    
    
if __name__=="__main__":
    main()