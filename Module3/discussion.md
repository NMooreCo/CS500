Module 3: Discussion Forum
Module 3 Overview (1 of 7)
3.1 Data Types (2 of 7)
3.2 Arrays (3 of 7)
3.3 Iterating Through Arrays (4 of 7)
Current Discussion: Module 3: Discussion Forum (5 of 7)
BioSig-ID™ validation - Module 3: Critical Thinking Assignment (6 of 7)
Module 3: Critical Thinking Assignment (7 of 7)
Module 3: Discussion Forum
Identify three real-life scenarios in which an array could be used for storing information. Provide a sample code segment that illustrates how to store data in an array for one of your outlined scenarios. Provide a rationale for your response. In response to your peers, provide constructive feedback on strategies and rationales that were posted. Include additional code segments if applicable.

Be sure to post an initial, substantive response by Thursday at 11:59 p.m. MT, and respond to two or more classmates or the instructor with substantive responses by Sunday at 11:59 p.m. MT.

A substantive initial post answers the question presented completely and/or asks a thoughtful question pertaining to the topic. Be sure your post is unique. Do not repeat what other students have said.

Substantive peer responses ask thoughtful questions pertaining to the topic, and/or answer a question (in detail) posted by another student or the instructor. Note: The following are not examples of substantive contributions:

Thanking, agreeing with, or complimenting a classmate.
Providing irrelevant commentary.


1. A ledger like your bank account. An array can be used to store sequential withdraws and deposits to calculate balance

import array as arr
# Create an empty array for bank account transactions
bank_account = arr.array('d', [])

# initial deposit
bank_account.append(100.00)

# some spending
bank_account.append(-10.00)
bank_account.append(-22.00)
bank_account.append(-10.00)

# another deposit
bank_account.append(100)

total = 0.0
for transaction in bank_account:
    total += transaction
print("Final balance:", total)

2. Tracking kids math tests grades. An arracy can be used to store all test grades, update test grades, and calculate average test score
import array as arr
# Create an empty array for math test grades
math_test_grades = arr.array('i', [])

# first test
math_test_grades.append(95)

# second test
math_test_grades.append(65)

# current average
average_score = sum(math_test_grades) / len(math_test_grades)
print("Current average after 2 tests:", average_score)

# everyone in the class made below 70 so the teacher allowed everyone to retake the test
math_test_grades[1] = 85

# new average
average_score = sum(math_test_grades) / len(math_test_grades)
print("New average after retake of 2nd test:", average_score)

3. Identifying SMA in stock price. An array can be used to calculate differnt "stonk" indicators
import array as arr
# Create an array of historical stock prices and calculate simple moving average (SMA) to determine when to buy (simple example and not a recommendation)
stock_prices = arr.array('d', [100.00, 99.50, 98.75, 97.00, 96.50, 95.00])

# Calculate the SMA over the last 3 days
sma = sum(stock_prices[-3:]) / 3
print("Simple Moving Average (SMA):", sma)

# If the current price is below the SMA, it might be a good time to buy
if stock_prices[-1] < sma:
    print("Current price is below SMA. Consider buying.")
else:
    print("Current price is above SMA. Consider holding or selling.")

# Calculate the SMA over last 5 days
sma = sum(stock_prices[-5:]) / 5
print("Simple Moving Average (SMA):", sma)

# If the current price is below the SMA, it might be a good time to buy
if stock_prices[-1] < sma:
    print("Current price is below SMA. Consider buying.")
else:
    print("Current price is above SMA. Consider holding or selling.")
