
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
subtotal = float(input("Please enter the subtotal: "))



if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        new_price = subtotal - (subtotal * 0.1)
        tax = subtotal * 0.06
        total = new_price + tax
        print(f"Discount amount is {subtotal * 0.1}$")
        print(f"Subtotal: {new_price}$")
        print(f"Sales tax: {tax}$")
        print(f"Total amount: {total}$")
    else:
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Subtotal: {subtotal}$")
        print(f"Sales tax: {tax}$")
        print(f"Total amount: {total}$")
else:
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Subtotal: {subtotal}$")
        print(f"Sales tax: {tax}$")
        print(f"Total amount: {total}$")



# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

# Get the subtotal from the user.
subtotal = float(input("Please enter the subtotal: "))

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
weekday = current_date_and_time.weekday()

# If the subtotal is greater than 50 and today is
# Tuesday or Wednesday, compute the discount amount.
if subtotal >= 50 and (weekday == 1 or weekday == 2):
    discount = round(subtotal * DISC_RATE, 2)
    print(f"Discount amount: {discount}")
    subtotal -= discount

# Compute the sales tax. Notice that we compute the sales tax
# after computing the discount because the customer does not
# pay sales tax on the full price but on the discounted price.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax}")

# Compute the total by adding the subtotal and the sales tax.
total = subtotal + sales_tax

# Display the total for the user to see.
print(f"Total: {total:.2f}")


