class Product :
    count = 0

    def __init__(self, name, price) :
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self) :
        print(f"The price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls) :
        print(f"Total Object = {cls.count}")

    @staticmethod
    def cal_discount(price, discount) :
        final_price = price - (price*(discount/100))
        print(f"Final price = {final_price}")

p1 = Product("Phone", 10000)
p2 = Product("Laptop", 50000)
p3 = Product("Keybord", 250)
p4 = Product("Mouse", 150)
p5 = Product("Speaker", 550)

p1.get_info()
p2.get_info()
p3.get_info()
p4.get_info()
Product.get_count()

p2.cal_discount(p2.price, 15)
