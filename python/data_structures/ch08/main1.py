from stacks1 import Stack1

N = 4
stack = Stack1(N)

print("Length:", len(stack))
print("Is Empty:", stack.is_empty())
print("Push from 1 to", N)

for i in range(1, N + 1):
    print("Push:", i)
    stack.push(i)
    print("Stack:", stack)
    print("Peek:", stack.peek())

print("Is Empty:", stack.is_empty())
for i in stack:
    print("Element:", i)

print()
for i in range(N):
    print("Peek and Pop: ", stack.peek())
    stack.pop()
    print("Stack:", stack)

print("Length:", len(stack))
print("Is Empty:", stack.is_empty())