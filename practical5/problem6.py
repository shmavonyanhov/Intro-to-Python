def foo(user, **kwarg):
    if user == "admin":
        for k in kwarg.keys():
            print(k,":",kwarg[k])
    else:
        print("access denied to user "+user)


foo("admin", a="1", b="2")

foo("ad", a="1", b="2")
