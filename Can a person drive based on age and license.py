def can_drive(age, has_license):
    return age >= 18 and has_license
print(can_drive(20, True))   # True
print(can_drive(17, True))   # False
print(can_drive(20, False))  # False
