def main():
    a = 5
    print('a =', a, id(a))
    b = 3 + 2
    print('b =', b, id(b))
    a = 7
    print ('a =', a, id (a))
    print ('b =', b, id (b))

if __name__ == '__main__':
    main()

