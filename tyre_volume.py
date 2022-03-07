#tyre_volume
import math
from datetime import datetime
current_date_and_time = datetime.now()
width_tyre = int(input("Enter the width of the tyre in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tyre: "))
diameter_wheel = int(input("Enter the diameter of the wheel in inches: "))
volume = math.pi * width_tyre ** 2 * aspect_ratio * (width_tyre * aspect_ratio + 2540 * diameter_wheel) / 10000000000
print(f"The approximate volume is {volume:.2f} liters")

#Exceeding requierments question
offer = input("Do you want to buy the tires with the dimensions you entered?" )
if offer.lower() == "yes":
    phone_number = input("Please enter your phone number?" )
    print("Thank you, our representative will soon reach out to you")
    with open("volume_info.txt", "at") as volume_details:
     print(f"{current_date_and_time:%Y-%m-%d}, {width_tyre}, {aspect_ratio}, {diameter_wheel}, {volume:.2f}, {phone_number}", file = volume_details)

else:
    print("Thank you and have a nice day")
#Adding all the information to the text file
with open("volume_info.txt", "at") as volume_details:
    print(f"{current_date_and_time:%Y-%m-%d}, {width_tyre}, {aspect_ratio}, {diameter_wheel}, {volume:.2f}", file = volume_details)

    



  

    
