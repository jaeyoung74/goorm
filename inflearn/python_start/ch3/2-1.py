#print 사용법

#기본 출력
print('python start!')
print("python start!")
print('''python start''')
print("""python start""")

print()

#separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '1111', '2222', sep='-')
print('python', 'goole.com', sep='@')
print()

#end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print('Hi', end='-')
print("I'm dog")
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

#format 사용 (d:3, s:'python', f:3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%f' % (3.1434344334343))
print('{:f}'.format(3.143434343434))

print('%06.2f' % (3.1415546475663))
print('{:06.2f}'.format(3.141534645))