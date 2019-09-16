def password_check(password):
    if len(password)<10:
        return False
    count=0
    p=list(password)
    for i in p:
        if i.isdigit:
            count=count+1
    return count>2

print(password_check("FERfe59rffe"))