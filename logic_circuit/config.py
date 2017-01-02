import os

class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://shaun:5432/logic-circuits"
    DEBUG = True
    SECRET_KEY = os.environ.get("LOGIC_CIRCUIT_SECRET_KEY", os.urandom(12))
    
