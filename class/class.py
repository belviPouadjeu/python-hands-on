class Vehicle:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the vehicle class
Vehicle1 = Vehicle(240, 18)
Vehicle1.assign_seating_capacity(5)
Vehicle1.display_properties()

Vehicle2 = Vehicle(200, 15)
Vehicle2.assign_seating_capacity(5)
Vehicle2.display_properties()
    
