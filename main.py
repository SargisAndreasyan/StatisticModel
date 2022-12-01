
class Node:
    left = None
    right = None


class Tree:

    def __init__(self, age):
        if age:
            self.create_left(age - 1)
            self.create_right(age - 1)

    def create_right(self, age):
        self.right = Tree(age)
        return self.right

    def create_left(self, age):
        self.left = Tree(age)
        return self.left


if __name__ == '__main__':
    head = Tree(3)
    print()
