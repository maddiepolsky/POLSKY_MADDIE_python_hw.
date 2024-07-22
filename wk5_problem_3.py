import math

def find_distance(movements):
    x, y = 0, 0
    for move in movements:
        direction, steps = move.split()
        steps = int(steps) 
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    distance = math.sqrt(x**2 + y**2)
    return round(distance)

movements = ["UP 5", "DOWN 4", "LEFT 3", "RIGHT 2"]  

print(find_distance(movements))  
