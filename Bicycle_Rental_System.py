import datetime


def validate_input(func):
    def wrapper(self, n):
        if n <= 0:
            print("Number of bicycle should be positive!")
            return None
        return func(self, n)

    return wrapper


def validate_stock(func):
    def wrapper(self, n):
        if n >= self.stock:
            print(f"Sorry. The available bicycle are {self.stock}.")
            return None
        return func(self, n)

    return wrapper


class Bicycle_Rental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"We have currently {self.stock} bicycle for rent.")
        return self.stock

    @validate_input
    @validate_stock
    def rent_in_hourly(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle on hourly basis today at {now}.")
        print("You will be charged 20 Taka for each hour per bicycle.")
        self.stock -= n
        return now

    @validate_input
    @validate_stock
    def rent_in_daily(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle on daily basis today at {now} hours.")
        print("You will be charged 100 Taka for each hour per bicycle.")
        self.stock -= n
        return now

    @validate_input
    @validate_stock
    def rent_in_weakly(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle on weakly basis today at {now} hours.")
        print("You will be charged 300 Taka for each hour per bicycle.")
        self.stock -= n
        return now


rent1 = Bicycle_Rental(10)
rent1.display_stock()

rent1.rent_in_hourly(2)
rent1.display_stock()

rent1.rent_in_weakly(2)
rent1.display_stock()

rent1.rent_in_daily(2)
rent1.display_stock()


