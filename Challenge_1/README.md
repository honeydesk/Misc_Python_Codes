# Misc_Python_Codes

##Code Challenge:

Below is a parent class for Basic Hosting and a child class for Deluxe Hosting. 
The parent class has three attributes (domain, coupon, and price) and one method 
to discount the price attribute.

Your challenge now is to nullify the discount_price method if a customer is
an existing user of Deluxe Hosting. However, for new users, the discounted
price remains valid. The discount also applies to Basic Hosting irrespective
of whether the user is a new or existing user.
Note that the method discount_price needs to be prefaced by the parent class
name when used in a child class (i.e. BasicHosting.discount_price ).
