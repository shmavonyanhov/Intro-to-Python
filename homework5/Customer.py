import Productcheck

def buy(product,num,price):
    if Productcheck.check(product,num):
        print("You bought "+product+" and spent ",num*price)
    else:
        print("Sorry! We are out of this product.")

buy("candy",8,10)
buy("candy",12,10)