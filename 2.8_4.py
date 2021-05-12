class Human:
    def eat_spagetti(self):
        print('Я могу есть спагетти')

class Robot:
    def drink_oil(self):
        print("Я могу  потреблять машинное масло")

class Cyborg(Human,Robot):
    pass

c1 = Cyborg()
c1.eat_spagetti()
c1.drink_oil()



    