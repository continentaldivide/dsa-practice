# https://leetcode.com/problems/valid-parentheses/

# this can be solved with an array, but it's a good opportunity to practice implementing a stack -- which I just learned about last night!

# class methods here are pretty utilitarian -- my instinct is that in a real use case I'd want some more thoughtful, robust returns for my class methods than I'm using here.  but since the direct objective is the parentheses problem and not "implement an awesome stack structure," I'm focusing on coding to the immediate need and not over-engineering.
class Stack:
  def __init__(self):
    self.data = []

  def read(self):
    if len(self.data) == 0:
      return "empty"
    else:
      return (self.data[-1])

  def push(self, element):
    self.data.append(element)

  def pop(self):
    if len(self.data) == 0:
      return "error: empty list"
    else:
      last = self.read()
      self.data.pop()
      return last

class Solution:
    def isValid(self, s: str) -> bool:
      my_stack = Stack()
      for char in s:
        if char in ['(', '{', '[']:
          my_stack.push(char)
        if char in [')', '}', ']']:
          check_pop = my_stack.pop()
          if check_pop == "error: empty list":
            return False
          if char == ')' and check_pop in ['[','{']:
            return False
          if char == ']' and check_pop in ['(','{']:
            return False
          if char == '}' and check_pop in ['[','(']:
            return False
          
      if my_stack.read() == "empty":
        return True
      else:
        return False

print(Solution().isValid("[)"))