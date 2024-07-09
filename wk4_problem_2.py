#Create a class called Car, which takes in the following attributes: ● Color
#● Speed (in miles per hour)
#● Max number of passengers
#● Current number of passengers

class Car:
    def __init__(self, color, speed, max_passengers, currrent_passengers):
        self.color = color
        self.speed = speed
        self.max_passengers = max_passengers
        self.current_passengers = currrent_passengers

        def get_color (self):
            return self.color
        def get_distance_traveled(self, time):
            return self.speed*time
        def add_passenger(self):
            if self.max_passengers > self.currrent_passengers:
                self.current_passengers += 1
            else:
                print ("Error: the vehicle is at maximum capacity.")
        def remove_passenger(self):
            if self.currrent_passengers > 0:
                self.current_passengers -= 1
            else: 
                print ("Error: no passengers can be removed from the car.")

#not sure how to make it run but thats the problem        

 my_car = Car ("Blue", 25, 6, 4) 
Car.introduce()      