#Define the menu of resturant 
menu ={
    'pizza':150,
    'pasta':70,
    'burger':160,
    'salad':80,
    'coffee':60,
}
#Greet
print('Welcome to Python Resturant')
print("Pizza: Rs150 \n Pasta: 70\n Burger: 160\n Salad:80\n Coffee:60")

order_total=0
#150+70=220 save hunxa order total ma 

item_1= input("Enter the name of item you want to order = ").lower()
if item_1 in menu:
    order_total += menu[item_1]#0+150
    print(f"Your item {item_1.capitalize()}has been added to your order")
else:
    print(f"Ordered item {item_1.capitalize()}is not available yet")
another_order =input("Do you want to add another item? (Yes/No): ").lower()
if another_order == 'yes':
    item_2=input("Enter the name of second item= ").lower()
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item{item_2.capitalize()} has been added to order")
    else:
        print(f"Ordered item{item_2.capitalize()}is not available yet")

print(f"the total amount of items to pay is {order_total}") 