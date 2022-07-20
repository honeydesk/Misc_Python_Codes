class BasicHosting:
    def __init__(self, domain, coupon, price):
        self.domain = domain
        self.coupon = coupon
        self.price = price
    
    def discount_price(self, discount):
        self.price *= discount
        
class DeluxeHosting(BasicHosting):
    def discount_price(self, discount, new_user='Yes'):
        if new_user == 'No':
            BasicHosting.discount_price(self, discount = 1)
        else:
            BasicHosting.discount_price(self, discount)

# While both existing users have a discount coupon, the first user does not enjoy any discount 
# as they are purchasing Deluxe Hosting, which is not eligible for a discount.
user1 = DeluxeHosting('Yes', 'Yes', 10)
user1.discount_price(0.9, 'No')
print(user1.price)

user2 = BasicHosting('Yes', 'Yes', 5)
user2.discount_price(0.9)
print(user2.price)