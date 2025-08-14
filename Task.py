# ahmedova-python
QA Automation traineeship task: number check, name check, and multiples of 3 from array
# Task 1: Number check
number = int(input("Enter a number: "))
if number > 7:
    print("Hello")

# Task 2: Name check
name = input("Enter a name: ")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

# Task 3: Multiples of 3 from array
array = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Multiples of 3:")
for num in array:
    if num % 3 == 0:
        print(num)

# Task 4: Bracket sequence check
sequence = "[((())()(())]]"

def is_bracket_sequence_correct(seq):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in seq:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

print("Bracket sequence correct?", is_bracket_sequence_correct(sequence))
