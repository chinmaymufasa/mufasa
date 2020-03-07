class pet:
    number_of_legs = 0
    def sleep(self):
        print('ZZZZZZ')
    def count_legs(self):
        print('I have', self.number_of_legs, 'legs.' )


class dog(pet):
    def bark(self):
        print('WOOF!!!')


satyam = dog()

satyam.bark()
satyam.sleep()
satyam.number_of_legs = 5
satyam.count_legs()