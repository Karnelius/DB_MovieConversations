class Person:
    #def __init__(self, name, age):
      #  self.name = name
       # self.age = age

    def __init__(self,**kwargs):
        self.__dict__ = kwargs

def main():
    p_dict= {
        'name': "David",
        'age' : 33,
        'music' : "Rock",
        'city': 'London'
    }

    p1 = Person(**p_dict)
    #print(p1.__dict__)
    print(p1.name)
    print(p1.city)

if __name__ == '__main__':
    main()
