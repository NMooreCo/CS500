# calculate total rainfall and average rainfall
def get_number_of_years_for_rainfall():
    while True:
        try:
            number_of_years = int(input("Enter the number of years for calculating rainfall: "))
            if number_of_years <= 0:
                raise ValueError("Number of years must be a positive integer.")
            return number_of_years
        except ValueError as e:
            print(e)
            print("Please enter a valid positive integer.")

def get_amount_of_rainfall(year, month):
    while True:
        try:
            rainfall = float(input(f"Enter the rainfall for year {year + 1} month {month + 1}: "))
            if rainfall < 0:
                raise ValueError("Rainfall cannot be negative.")
            return rainfall
        except ValueError as e:
            print(e)
            print("Please enter a valid positive number.")

number_of_years = get_number_of_years_for_rainfall()
print(f"Calculating rainfall for {number_of_years} years.")
total_rainfall = 0.0
total_months = number_of_years * 12
for year in range(number_of_years):
    print(f"Year {year + 1}:")
    for month in range(12):
        rainfall = get_amount_of_rainfall(year, month)
        total_rainfall += rainfall
average_rainfall = total_rainfall / total_months
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall} inches")
print(f"Average rainfall per month: {average_rainfall} inches")