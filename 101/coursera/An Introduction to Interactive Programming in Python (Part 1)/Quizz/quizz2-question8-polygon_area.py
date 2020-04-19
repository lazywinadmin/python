#Quizz 2 - Question 8
import math
def polygonarea(sides,length):
    result = 1 / 4 * sides * length**2 / math.tan(math.pi / sides)
    print(result)
                                                            
polygonarea(5, 7)
polygonarea(7, 3)