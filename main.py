import random
from time import sleep

from mod_queue import Manager,Person

class Tree:

    def __init__(self, age):
        if age:
            self.create_left(age - 1)
            self.create_right(age - 1)
            self.manager = Manager(Manager.manager_id)
            Manager.manager_id += 1

    def create_right(self, age):
        self.right = Tree(age)
        return self.right

    def create_left(self, age):
        self.left = Tree(age)
        return self.left


def generate_path(lenght):
    return [random.randint(0, 1) for _ in range(lenght)]


if __name__ == '__main__':
    head = Tree(3)
    while True:
        for i in generate_path(4):
            if i == 0:
                node = head.left
            else:
                node = head.right
            sleep(1)
        node.manager.queue.persons_in()
