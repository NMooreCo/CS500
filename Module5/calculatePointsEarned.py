# calculate number of points earned
def how_many_books_did_you_buy():
    while True:
        try:
            number_of_books = int(input("Enter the number of books you bought this month: "))
            if number_of_books < 0:
                raise ValueError("Number of books must be 0 or a positive integer.")
            return number_of_books
        except ValueError as e:
            print(e)
            print("Please enter a valid positive integer.")

def calculate_points(number_of_books):
    if number_of_books >= 8:
        return 60
    elif number_of_books >= 6:
        return 30
    elif number_of_books >= 4:
        return 15
    elif number_of_books >= 2:
        return 5
    else:
        return 0

number_of_books = how_many_books_did_you_buy()
print(f"Calculating points for {number_of_books} books.")
points_earned = calculate_points(number_of_books)

if (points_earned > 0):
    print(f"Congratulations! You earned {points_earned} points this month.")
else:
    print("You did not earn any points this month.")