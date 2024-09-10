bill_amount=float(input("Enter the bill amount:"))
tip_percent=float(input("Enter the tip percentage:"))

def calculate_tip(bill_amount,tip_percent):
   tip= bill_amount*tip_percent/100
   return tip

tip_amount = calculate_tip(bill_amount,tip_percent)
print(f"Your tip amount is {tip_percent}")