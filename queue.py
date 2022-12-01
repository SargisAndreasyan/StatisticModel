import random
from time import time, sleep
import threading


class Queue:
    MIN_SERVE = 0
    MAX_SERVE = 4
    MIN_REQUIRED_TIME = 0
    MAX_REQUIRED_TIME = 3
    MIN_IN = 0
    MAX_IN = 4
    WORKING_TIME = 20
    persons = []
    deny = 0
    accept = 0

    def __init__(self, min_serve=MIN_SERVE, max_serve=MAX_SERVE, min_req_time=MIN_REQUIRED_TIME,
                 max_req_time=MAX_REQUIRED_TIME, min_in=MIN_IN, max_in=MAX_IN, w_time=WORKING_TIME):
        self.MIN_SERVE = min_serve
        self.MAX_SERVE = max_serve
        self.MIN_REQUIRED_TIME = min_req_time
        self.MAX_REQUIRED_TIME = max_req_time
        self.MIN_IN = min_in
        self.MAX_IN = max_in
        self.WORKING_TIME = w_time

    def add(self, person):
        all_time = 0
        for person in self.persons:
            all_time += person.time_use
        if all_time < person.can_wait:
            self.persons.append(person)

    def persons_in(self):
        sleep(random.randint(self.MIN_IN, self.MAX_IN))
        self.add_person()

    def work(self):
        now = time()
        while time() - now < self.WORKING_TIME:
            self.serve()
            if int(time()) % random.randint(self.MIN_IN + 1, self.MAX_IN + 1) == 0:
                self.persons_in()
        print(f"Accept {self.accept}\nDeny {self.deny}")

    def serve(self):
        if len(self.persons):
            self.persons[-1].wait_for_serve()
            self.accept += 1
        else:
            self.deny += 1

    def add_person(self):
        person = Person(random.randint(self.MIN_REQUIRED_TIME, self.MAX_REQUIRED_TIME))
        self.add(person)


class Person:
    time_use = 0
    can_wait = 0
    id = 0
    MIN_CAN_WAIT = 0
    MAX_CAN_WAIT = 5

    def __init__(self, use_time):
        self.time_use = use_time
        self.can_wait = random.randint(self.MIN_CAN_WAIT,self.MAX_CAN_WAIT)

    def wait_for_serve(self):
        sleep(self.time_use)


if __name__ == '__main__':
    queue = Queue()
    t = threading.Thread(target=queue.work)
    t.start()
