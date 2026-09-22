def is_valid(brackets):
    stack = []

    pairs = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for char in brackets:
        if char in "{([":
            stack.append(char)
        else:
            # if not stack:
            if len(stack) == 0:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

brackets = "({[]})"
print(is_valid(brackets))