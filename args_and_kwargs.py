# *args
def add(*a):
    sum = 0
    for i in a:
        sum += i
    return sum


def calculate(n, **a):
    if a["shape"] == 'Square':
        return n * n
    if a["shape"] == "Circle":
        return 3.14 * n * n


print(calculate(5, shape='Square'))

# **kwargs
class Car:
    def __init__(self, **a):
        self.color = a.get("color")
        self.model = a.get("model")


my_car = Car(model="Ferrari")
print(my_car.model, my_car.color)


