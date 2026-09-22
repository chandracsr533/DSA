text = "python"

stack = []

for char in text:
    stack.append(char)

reversed_text = ''

# while stack:
for _ in range(len(stack)):
    reversed_text += stack.pop()

print(reversed_text)
