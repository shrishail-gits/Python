class calci:
    def add(self):
        a = 10
        b = 10
        c = a + b
        print(c)
x = calci()
x.add()

class calci:
    def add(self):
        a = 10
        b = 10
        c = a + b
        return c
x = calci()
res = x.add()
print(res)

class calci:
    def add(self, a, b):
        c = a + b
        print(c)
x = calci()
y = 10
z = 20
res = x.add(y, z)

class calci:
    def add(self, a, b):
        c = a + b
        return c
x = calci()
y = 10
z = 20
res = x.add(y, z)
print(res)