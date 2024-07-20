# Exercise -- if buyer has good credit, discount 10% otherwise
# give discount  5 % 


credit_status = 'bad'
house_price = 1000000
new_price =0

if credit_status == 'good':
    discount = (house_price * 10)/100
    new_price = house_price - discount
else:
    discount = (house_price * 5)/100
    new_price = house_price - discount


print("Hurray! You got discount of Rs. ", discount)
print("Your new house price is: Rs. ", new_price)
