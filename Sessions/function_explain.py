def f(x):
    print(x)
    if x<10:
        x+=1
        f(x)
        print("exiting many times")
        return
    else:
        print("exiting once" )
        return
f(1)
