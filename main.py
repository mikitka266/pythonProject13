class User:
    def __init__(self, name , age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Long of name must be beetween 6 and 30 symbols. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Age must be a chislo. Use int or float. {type(age) = } ')
        elif age <0:
            raise ValueError(f'Age must be a positive. {age = }')
        else:
            self.age = age


user = User('Patrick', 12)