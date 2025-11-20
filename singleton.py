class ConfigurationManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance
    
    def set_setting(self, key, value):
        self.settings[key] = value
    
    def get_setting(self, key):
        return self.settings.get(key)