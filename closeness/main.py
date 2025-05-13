"""
The person's closeness to the target is determined by dividing the ideal distance by the person's distance.
Ideal distance = 1.0
Person's distance 1 + ed
where ed = Euclidean distance

Euclidean distance is given by taking the 
1. square root of
2. sum of
3. square of
4. the differences between
5. max attribute and given attribute
"""

from math import sqrt



class Person:

    def __init__(self, frequency_of_contact, shared_experiences, mutuals, time_known, intimacy, max_mutuals, max_time_known):
        self.__max_frequency = 5
        self.__max_shared_experiences = 3
        self.max_mutuals = max_mutuals
        self.max_time_known = max_time_known
        self.__max_intimacy = 3

        self.frequency_of_contact = frequency_of_contact
        self.shared_experiences = shared_experiences
        self.mutuals = mutuals
        self.time_known = time_known
        self.intimacy = intimacy


    def closeness(self):
        euclidean_distance = sqrt(sum([(self.__max_frequency - self.frequency_of_contact)**2, (self.__max_shared_experiences - self.shared_experiences)**2, (self.max_mutuals - self.mutuals)**2, (self.max_time_known - self.time_known)**2, (self.__max_intimacy - self.intimacy)**2]))
        closeness = (1 / (1 + euclidean_distance))
        return closeness



frequency_of_contact = int(input('> '))
shared_experiences = int(input('> '))
mutuals = int(input('> '))
time_known = int(input('> '))
intimacy = int(input('> '))


person1 = Person(frequency_of_contact, shared_experiences, mutuals, time_known, intimacy, 10, 10)
print(person1.closeness())
