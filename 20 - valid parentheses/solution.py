# https://leetcode.com/problems/valid-parentheses/

# this can be solved with an array, but it's a good opportunity to practice implementing a stack -- which I just learned about last night!

class Stack:
  def __init__(self):
    self.data = []

  def push(self, element):
    self.data.append(element)

  def pop(self):
    if len(self.data) == 0:
      return "error: empty list"
    else:
      self.data.pop()

  def read(self):
    if len(self.data) == 0:
      return "empty"
    else:
      print(self.data[-1])

my_stack = Stack()
