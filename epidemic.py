# Programowanie I R
# Symulacja rozprzestrzeniania się epidemii - praca wspólna

import math
import random

class Person:
    maxDistance = 1.
    maxIllDistance = 0.1
    
    def __init__(self, x = 0, y = 0, status = "zdrowy"):
        self.x = x
        self.y = y
        self.status = status
            
    def move(self):
        if self.status == "chory":
            max_distance = maxIllDistance
        else:
            max_distance = maxDistance
        
        r = max_distance * sqrt(random.uniform(0, 1))
        theta = 2 * math.pi * random.uniform(0, 1)
        
        self.x = self.x + r * math.cos(theta)
        self.y = self.y + r * math.sin(theta)
    
    def info(self):
        return f"({self.x}, {self.y}): {self.status}"
        
    def __str__(self):
        return self.info()

class Population:
    infectionProbability = 0.2
    infectionDistance = 1.

    def __init__(self, N, height = 100, width = 100):
        self.people = []
        self.h = height
        self.w = width
        
        for i in range(N):
            x = random.uniform(0, self.w)
            y = random.uniform(0, self.h)
            status = random.choices( ["zdrowy", "chory", "nosiciel"], [1 - infectionProbability, infectionProbability / 2, infectionProbability / 2] )[0]
            self.people.append(Person(x, y, status))
    
    def move(self):
        for p in self.people:
            p.move()
            p.x = p.x % self.w
            p.y = p.y % self.h
        
        # DO ZROBIENIA: dodanie mechanizmu zakażania

    def paint(self):
        # DO ZROBIENIA
        pass
    
    def info(self):
        s = ""
        for p in self.people:
            s += str(p) + "\n"
        return s

    def __str__(self):
        return self.info()
    
    # DO ZROBIENIA: iterator

# DO ZROBIENIA: główny program (wyświetlanie animacji)