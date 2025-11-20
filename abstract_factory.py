from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Windows button rendered"

class MacButton(Button):
    def render(self):
        return "Mac button rendered"