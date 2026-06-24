try:
    a=int(input("Enter First Value"))
    b=int(input("Enter Second Value"))
    print("Iam try just started")
    if b%2==0:
        raise Exception
    else:
        print(a/b)
    print("Iam a try iam done")
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print("Division by evens are not allowed")
else:
    print("hi iam else now alive becausee try is executed")
finally:
    print("Hello there Iam finally Iam going to close")
    