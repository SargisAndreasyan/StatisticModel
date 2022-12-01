import random
from time import time, sleep
import threading


class Queue:
    MIN_SERVE = 1
    MAX_SERVE = 3
    MIN_REQUIRED_TIME = 0
    MAX_REQUIRED_TIME = 3
    MIN_IN = 0
    MAX_IN = 0
    MIN_CAN_WAIT = 0
    MAX_CAN_WAIT = 10
    WORKING_TIME = 30
    persons = []
    deny = 0
    accept = 0

    def add(self, person):
        all_time = 0
        for person in self.persons:
            all_time += person.time_use
        if all_time < person.can_wait:
            self.persons.append(person)

    def manager(self):
        now = time()
        while time() - now < 10:
            sleep(random.randint(self.MIN_IN, self.MAX_IN))
            self.add_person()
        print(f"Accept {self.accept}\nDeny {self.deny}")

    def serve(self):
        if len(self.persons):
            self.persons[-1].using()
            self.accept += 1
            print('yee')
        else:
            self.deny += 1

    def add_person(self):
        person = Person(random.randint(self.MIN_REQUIRED_TIME, self.MAX_REQUIRED_TIME),
                        random.randint(self.MIN_CAN_WAIT, self.MAX_CAN_WAIT))
        self.add(person)


class Person:
    time_use = 0
    can_wait = 0
    id = 0

    def __init__(self, use_time, can_wait):
        self.time_use = use_time
        self.can_wait = can_wait


if __name__ == '__main__':
    queue = Queue()
    t = threading.Thread(target=queue.manager)
    t.start()
