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

"""
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
"""
"""
for i in range(1,5):
    if(i!=2):
        print(i)
        """

class Rectangle(object): 

    def __init__(self,width=2,height =3,color='r'):

        self.height=height 

        self.width=width 

        self.color=color 

    def drawRectangle(self): 

        import matplotlib.pyplot as plt 

        plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color)) 

        plt.axis('scaled') plt.show()

# Create an instance of the Rectangle class
my_rectangle = Rectangle()

# Print the width attribute of the object
print(my_rectangle.width) 