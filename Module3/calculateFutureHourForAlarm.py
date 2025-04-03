# This code calculates the time in hours from the current hour to the alarm hour.
def get_current_hour():
    try:
        current_hour = int(input("Enter the current hour (0-23): "))
        if(current_hour < 0 or current_hour > 23):
            print("Invalid hour. Please enter a value between 0 and 23.")
            return get_current_hour()
    except ValueError:
        print("Invalid input. Please enter a value between 0 and 23.")
        return get_current_hour()
    except Exception as e:
        print("Error:", e, "\nPlease try again.")
        return get_current_hour()
    return current_hour

def get_hours_for_alarm():
    try:
        alarm_hour = int(input("Enter number of hours to wait for alarm (> 0): "))
        if(alarm_hour <= 0):
            print("Invalid hour. Please enter a value > 0.")
            return get_hours_for_alarm()
    except ValueError:
        print("Invalid input. Please enter a number > 0.")
        return get_hours_for_alarm()
    except Exception as e:
        print("Error:", e, "\nPlease try again.")
        return get_hours_for_alarm()
    return int(alarm_hour)


current_hour = get_current_hour()
hours_to_wait_for_alarm = get_hours_for_alarm()

hour_in_future = (current_hour + hours_to_wait_for_alarm) % 24
am_or_pm = "AM"
if hour_in_future >= 12:
    am_or_pm = "PM"
hour_in_future_12 = hour_in_future % 12
if hour_in_future_12 == 0:
    hour_in_future_12 = 12

number_of_days_in_futere = hours_to_wait_for_alarm // 24

print(f"The alarm will go off in {hours_to_wait_for_alarm} hours.")
print(f"Which is {number_of_days_in_futere} days from now.")
print(f"And is at {hour_in_future} in 24-hour format.")
print(f"And is at {hour_in_future_12} {am_or_pm} in 12-hour format.")

