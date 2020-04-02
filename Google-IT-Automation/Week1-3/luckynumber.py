
"""
def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
"""


def lucky_number(name):
    number = len(name) * 9
    lucky_num = "Hello " + name + ". Your lucky number is " + str(number)
    return lucky_num

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
