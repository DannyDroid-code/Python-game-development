# import pygame, sys
# from pygame.locals import QUIT

# pygame.init()

# height,width =500,500

# screen = pygame.display.set_mode((height,width))
# pygame.display.set_caption("Pygame shapes")

# screen.fill("red")
# pygame.draw.rect(screen,"black",(100,100,50,100))
# pygame.draw.circle(screen,"blue",(250,250),70)

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     pygame.display.update()



class person():
    #variables/properties(xtics)
       #class variables
       head = 1
       hands = 2
       legs = 2

       #instance/object variables 
       def __init__(self,name,age):
              self.name = name 
              self.age=age
             


    #methods(behaviors)
       def details(self):
              print("My name is ",self.name)
              print("I am ",self.age," years old.")


       def walk(self):
              print("I use my ",self.legs,"to walk.")
            
       def modify(self):
               print("My old name is ",self.name)
               new_name = input("Enter new name:")
               self.name = new_name
               print("My new name  is ",self.name)
               
#object/instance
# p1 = person("Allex",13,5.11,52)
# p2 = person("Danstan",28,5.11,85)

# print(p1.name)
# print(p1.age)
# p1.details()
# p2.details()
# p1.modify()


class Student(person):
  def __init__(self, name, age,year,grade):
    
    super().__init__( name,age)
    self.graduationyear = year
    self.grade=grade

x = Student("Mike",13, 2019,8)
x.modify()