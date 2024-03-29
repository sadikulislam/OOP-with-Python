import datetime


def validate_input(func):
    def wrapper(self, n):
        if n <= 0:
            print("Number of bicycles should be positive!")
            return None
        return func(self, n)

    return wrapper


def validate_stock(func):
    def wrapper(self, n):
        if n >= self.stock:
            print(f"Sorry. The available bicycles are {self.stock}.")
            return None
        return func(self, n)

    return wrapper


class BicycleRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"We currently have {self.stock} bicycles available for rent.")
        return self.stock

    @validate_input
    @validate_stock
    def rent_in_hourly(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle(s) on an hourly basis today at {now}.")
        print("You will be charged 20 Taka for each hour per bicycle.")
        self.stock -= n
        return now

    @validate_input
    @validate_stock
    def rent_in_daily(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle(s) on a daily basis today at {now}.")
        print("You will be charged 100 Taka for each hour per bicycle.")
        self.stock -= n
        return now

    @validate_input
    @validate_stock
    def rent_in_weekly(self, n):
        now = datetime.datetime.now()
        print(f"You have rented {n} bicycle(s) on a weekly basis today at {now}.")
        print("You will be charged 300 Taka for each hour per bicycle.")
        self.stock -= n
        return now

    def return_bicycle(self, rental_time, rental_basis, num_of_bicycle):
        if rental_time and rental_basis and num_of_bicycle:
            self.stock += num_of_bicycle
            now = datetime.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 20 * num_of_bicycle
            elif rental_basis == 2:
                bill = round(rental_period.days) * 100 * num_of_bicycle
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 300 * num_of_bicycle

            print("Thank you for returning your bicycle(s). We hope you enjoyed our service!")
            print(f"Your bill is {bill} Taka.")
            return bill
        else:
            print("Please make sure you rented a bicycle from us.")


class Customer:
    def __init__(self):
        self.bicycle = 0
        self.rental_basis = 0
        self.rental_time = None
        self.bill = 0

    def request_bicycle(self):
        while True:
            try:
                bikes = int(input("How many bicycles would you like to rent? "))
                if bikes < 1:
                    print("Invalid input. Number of bicycles should be greater than zero.")
                    continue
                else:
                    self.bicycle = bikes
                    return self.bicycle
            except ValueError:
                print("That's not a valid integer. Please enter a positive integer.")

    def return_bicycle(self):
        if self.bicycle and self.rental_basis and self.rental_time:
            return self.bicycle, self.rental_basis, self.rental_time
        else:
            print("Please make sure you rented a bicycle from us.")


rental_shop = BicycleRental(stock=10)

# Display available stock
rental_shop.display_stock()

# Create a customer instance
customer = Customer()

# Customer rents bicycles
customer.request_bicycle()
customer.rental_basis = 1  # Hourly rental
customer.rental_time = rental_shop.rent_in_hourly(customer.bicycle)

# Customer returns bicycles
returned_bicycles = customer.return_bicycle()
