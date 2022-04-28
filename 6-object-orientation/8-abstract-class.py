# abc -- abstract base class
# abc.ABC -- Abstract Base Class
# abc.@abstractmethod -- which makes a function abstract

from abc import  ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# --------------------------------------------------

class HondaCity(Car):
    def start(self):
        print("HC- start")

    def stop(self):
        print("HC-stop")

h=HondaCity()
h.start()
h.stop()