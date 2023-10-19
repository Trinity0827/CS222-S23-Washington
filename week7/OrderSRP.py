class Order:
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount

    def calculate_total_amount(self):
        pass
    
    def generate_invoice(self):
        pass

    def save_to_database(self):
        pass

class Order:
    def __init__(self, order_id, customer, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.total_amount = total_amount

class OrderCalculator:
    @staticmethod
    def calculate_total_amout(order : Order):
        pass

class InvoiceGenerator:
    @staticmethod
    def generate_invoice(order : Order):
        pass

class OrderRepository:
    @staticmethod
    def save_to_datatbase(order : Order):
        pass




