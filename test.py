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

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height