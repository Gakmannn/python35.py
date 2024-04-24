# x = 0
def foo():
    global x
    x = 20

    def bar():
        global x
        x = 25
        print('x in bar', x)
    
    print("До вызова bar(): ", x)
    print("Вызываем bar()")
    bar()
    print("После вызова bar(): ", x)

foo()

print("x в глобальной областим видимости: ", x)