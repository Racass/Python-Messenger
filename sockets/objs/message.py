class message(object):
    code = None
    msg = None
    client = None
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        #self.code = str(code)
        #self.msg = msg