# This program calculates the total cost of a meal including tip and sales tax.
def get_meal_cost():
    try:
        meal_amount = float(input("Please enter the meal amount: "))
        if(meal_amount <= 0):
            print("Invalid amount. Please enter a value > 0.")
            return get_meal_cost()
    except ValueError:
        print("Invalid amount. Please enter a number > 0.")
        return get_meal_cost()
    except Exception as e:
        print("Error:", e, "\nPlease try again.")
        return get_meal_cost()
    return meal_amount

meal_amount = get_meal_cost()
tip_amount = meal_amount * 0.18
sales_tax = meal_amount * 0.07
total_amount = meal_amount + tip_amount + sales_tax
print(f"Meal amount: ${meal_amount:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total amount: ${total_amount:.2f}")
