
# decorator for method init of class person to substitute the old init with this new decorated version in metaclass counter
def init_update(F):
    def wrapper(*args):
        obj = args[0]
        type(obj).n_instances += 1

        return F(*args)
    return wrapper

class counter(type):
    def __new__(meta, classname, supers, classdict):
        classdict['n_instances'] = 0
        classdict['__init__'] = init_update( classdict['__init__'] )
        return type.__new__(meta, classname, supers, classdict)
##################################################################

# method init to substitute the old init in metaclass spell
def init_spell(obj, name, lastname, birthday, payperhour, hday = 8, dweek = 5):
    obj.name = name
    obj.lastname = lastname
    obj.birthday = birthday
    obj.payperhour = payperhour
    obj.hday = hday
    obj.dweek = dweek

class spell(type):
    def __new__(meta, classname, supers, classdict):
        for k, v in Worker.__dict__.items():
            if k != '__init__':
                classdict[k] = v
        classdict['__init__'] = init_spell

        return type.__new__(meta, classname, supers, classdict)
##################################################################

class Person(metaclass=spell):
    def __init__(self, name, lastname, birthday):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getLastname(self):
        return self.lastname

    def setLastname(self, newlname):
        self.lastname = newlname

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, newb):
        self.birthday = newb

    def __repr__(self):
        return '< module:{0} type:{1} at {2} legend:name={3}, lastname={4}, birthday={5} >'.format(self.__module__, type(self).__name__, hex(id(self)), self.name, self.lastname, self.birthday)

class Worker(Person):

    def __init__(self, name, lastname, birthday, payperhour, hday = 8, dweek = 5):
        super().__init__(name, lastname, birthday)

        self.payperhour = payperhour
        self.hday = hday
        self.dweek = dweek

    def _getDaySalary(self):

        return self.payperhour * self.hday

    def _getWeekSalary(self):

        return self._getDaySalary() * self.dweek

    def _getMonthSalary(self):

        return self._getWeekSalary() * 4

    def _getYearSalary(self):

        return self._getDaySalary() * 365

    def _setDaySalary(self, v):

        self.payperhour = v / self.hday

    def _setWeekSalary(self, v):

        self.payperhour = v / (self.dweek * self.hday)

    def _setMonthSalary(self, v):

        self.payperhour = v / (4 * self.dweek * self.hday)

    def _setYearSalary(self, v):
        self.payperhour = v / (365 * self.hday)

    day_salary = property(_getDaySalary, _setDaySalary, None)
    week_salary = property(_getWeekSalary, _setWeekSalary, None)
    month_salary = property(_getMonthSalary, _setMonthSalary, None)
    year_salary = property(_getYearSalary, _setYearSalary, None)
