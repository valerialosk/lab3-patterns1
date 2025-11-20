class OldSystem:
    def specific_request(self):
        return "!emosewa si edoc ruoy"

class Target:
    def request(self):
        return "Your code is awesome!"

class Adapter(Target):
    def __init__(self, old_system):
        self._old_system = old_system
    
    def request(self):
        return self._old_system.specific_request()[::-1]