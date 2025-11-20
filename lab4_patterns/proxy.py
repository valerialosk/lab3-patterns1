from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request"

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject
    
    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        return "Access denied"
    
    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True
    
    def log_access(self):
        print("Proxy: Logging the time of request.")