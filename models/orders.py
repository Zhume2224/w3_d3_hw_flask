from models.order import Order

order1=Order('April','Vinilla',1)
# order1.topping=[]
order1.add_topping('chocolate')
order1.add_topping('almond flakes')

order2=Order('July','Chocolate',2)
order2.topping=[]
# order2.topping.add_topping('none')


order3=Order('May','pistacho',1)
order3.add_topping('almond flakes')
order3.add_topping('strawberry')


orders=[order1,order2,order3]



