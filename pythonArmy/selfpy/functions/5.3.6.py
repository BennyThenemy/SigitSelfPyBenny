def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)


def fix_age(age):
    if 13 <= age <= 19 and age not in [15, 16]:
        return 0
    else:
        return age


print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))
