brackets = "{()}[{}][]"
stack = []
bracket_map = {")": "(", "}": "{", "]": "["}
is_valid = True

for char in brackets:
    if char in bracket_map:
        if stack and stack[-1] == bracket_map[char]:
            stack.pop()
        else:
            is_valid = False
            break
    else:
        stack.append(char)

if is_valid and len(stack) == 0:
    print("valid")
else:
    print("not valid")