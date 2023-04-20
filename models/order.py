class Order():
    def __init__(self,customer_name,flavour,quantity):
      self.customer_name=customer_name
      self.flavour=flavour
      self.quantity=quantity
      self.topping=[]

    def add_topping(self,topping):
        self.topping.append(topping)