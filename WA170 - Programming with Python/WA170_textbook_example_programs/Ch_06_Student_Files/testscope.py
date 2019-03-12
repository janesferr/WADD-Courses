x = "module"

def f():
    x = "temporary"
    print(x)

print(x)
f()
print(x)
