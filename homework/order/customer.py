
class Customer:
    def __init__(self, first_name, last_name, phone_num, city):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.city = city

    def __str__(self):
        return f'Customer: {self.last_name} {self.first_name[0]}. {self.city} {self.phone_num}'
