class Time:
    def __init__(self,hr,min,sec):
        self.__hour=hr
        self.__minute=min
        self.__second=sec
    def __add__(self,other):
        sec=self.__second+other.__second
        min=self.__minute+other.__minute
        hr=self.__hour+other.__hour
        if sec>=60:
            min+=1
            sec-=60
        if min>=60:
            hr+=1
            min-=60
        return Time(hr,min,sec)
    def display(self):
        print(f"{self.__hour}:{self.__minute}:{self.__second}")

t1=Time(4,45,50)
t2=Time(5,30,25)
t3=t1+t2
print("sum of two times:")
t3.display()