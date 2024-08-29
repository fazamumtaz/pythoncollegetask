# a = 10
# a += 5
# a -= 3
# a *= 6
# a /= 8
# a %= 9
# a //= 6
# a **= 1
# a &= 2
# a != 3
# a ^= 4
# a >>= 4
# a <<= 4
# b=7
# print(b << 4)
# kata = "Indonesia"
# print(5 is not 5)

a = 5
b = 5
print(id(a)) 
print(id(b)) 
list_a = [1, 2, 3]
list_b = [1, 2, 3]
nama_a = 'budi'
nama_b = 'budi'
# output True
print('a is b:', a is b)
# output False
print('a is not b:', a is not b)
# output False
print('list_a is list_b:', list_a is list_b)
# output True
print('list_a == list_b:', list_a == list_b)
# output True
print('nama_a is nama_b:', nama_a is nama_b)
# output False
print('nama_a is not nama_b:', nama_a is not nama_b)

print(format(15, '04b'))

a=5
a&=not(a)
print(a)

a = 1
b = 64
print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')
print('[and]')
print('a & b =', a & b)
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'),
'\n')
print('[or]')
print('a | b =', a | b)
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'),
'\n')
print('[xor]')
print('a ^ b =', a ^ b)
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'),
'\n')

print('[not]')
print('~a ~b =', ~a, ~b)
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a,
'08b'), format(~b, '08b'), '\n')
print('[shift right]')
print('a >> b =', a >> b)
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b,
'08b'), '\n')
print('[shift left]')
print('b << a =', b << a)
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a,
'08b'), '\n')
