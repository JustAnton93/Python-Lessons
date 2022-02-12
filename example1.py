a = "printer", "skaner", "nout"
b = [9, 0, 21]
f = {2, 8, 36}
c = "g"
d = {"d":"m"}
r = (10>5)
w = 5
print(type(a))
print(type(b))
print(type(f))
print(type(c))
print(type(d))
print(type(r))
print(type(w))
b = [9, "a", {21}, (10 > 5), ([]), {"b":"a"}]
index = []
for index in b:
    print(type(index))
1 2 3 1 2 3
a: list = input('Vvedite raznye dannye')
a = a.split()
