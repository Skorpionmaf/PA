import time

class Person:

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


class Student(Person):

    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)
        self._lectures = dict()

    def setMark(self, lect, mark):
        assert mark >= 0 and mark <= 30, 'Not admitted mark, it must be between 0 and 30'
        self._lectures[lect] = mark

    def getMark(self, lect):
        return self._lectures[lect]

    def getAvgGrade(self):
        if len( self._lectures ) > 0:
            return sum( self._lectures.values() ) / len(self._lectures)
        else:
            return 'No marks added yet'

    grade_average = property(getAvgGrade, None, None, 'Getting average grade')

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

class Wizard(Person):

    def _getAge(self):

        today = time.localtime().tm_year
        byear = time.strptime(self.birthday, "%d %m %y").tm_year

        return today - byear

    def _setAge(self, v):

        today = time.localtime().tm_year
        birth = time.strptime(self.birthday, "%d %m %y")

        d = birth.tm_mday
        m = birth.tm_mon
        y = today - v

        self.birthday = str(d) + '-' + str(m) + '-' + str(y)


    age = property(_getAge, _setAge, None)