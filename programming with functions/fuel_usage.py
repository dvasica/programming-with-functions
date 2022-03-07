
def main():
    
    start_odometer = float(input("Enter the first odometer reading: "))
    
    end_odometer = float(input("Enter the last odometer reading: "))
   
    gallons_used = float(input("Enter the amount of fuel used(gallons): "))
    
    mpg = miles_per_gallon(end_odometer, start_odometer, gallons_used)


    lp100k = lp100k_from_mpg(mpg)

    
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")

def miles_per_gallon(start_odometer, end_odometer, gallons_used):

    
    mpg = abs(end_odometer - start_odometer) / gallons_used

    return mpg


def lp100k_from_mpg(mpg):
    
    
    lp100k = 235.215 / mpg
    return lp100k

main()

