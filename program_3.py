#title: store purchase
#author: michael stoll
#date: 1/31/25
#I=item(ex: I_1 is item 1)
I_1=float(input('Cost of item 1:'))
I_2=float(input('Cost of item 2:'))
I_3=float(input('Cost of item 3:'))
I_4=float(input('Cost of item 4:'))
I_5=float(input('Cost of item 5:'))
subtotal=(I_1+I_2+I_3+I_4+I_5)
print('Subtotal:', subtotal)
print('sales tax: 7%')
total=subtotal*1.07
print('Total:', total)