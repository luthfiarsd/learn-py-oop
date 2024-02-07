# abc = Abstract Base Class
from abc import ABC, abstractmethod


# ABSTRACT CLASS, SEHINGGA TIDAK BISA DIASSIGN DI OBJECT
class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    def click(self):
        print("Button clicked")


class RadioButton(Button):
    def click(self):
        print("Radio Button clicked")


tombol1 = PushButton()
tombol2 = RadioButton()
tombol1.click()
tombol2.click()
