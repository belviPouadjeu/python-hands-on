# def greet(name):
#     print(f"Hello {name}")

# for _ in range(3):
#     name = input("What's your name? ")
#     greet(name)

# def add_element(data_structure, element):
#     data_structure.append(element )

#     return data_structure

# def print_function(A):
#     for a in A:
#         print(a + '1')
# print_function(['a', 'b', 'c'])

# class Rectangle(object):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     def add_radius(self,r):
#         self.radius=self.radius + r

# C1 = Rectangle(2, 3)
# C2 = Rectangle(3, 4)

# print(C1.area())
# print(C2.area())

class Vehicle:
    color = "white"


    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity


V1 = Vehicle(150, 25)
print(V1)
