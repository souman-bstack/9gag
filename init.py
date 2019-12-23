import mongoengine

def init_all():
    mongoengine.connect('gag', alias='default')