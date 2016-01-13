
class My_dict(dict):

    def __init__(self):
        super(My_dict, self).__init__()
        self.order_dict = []

    def __setitem__(self, key, value):
        super(My_dict, self).__setitem__(key, value)

        self.order_dict.append( (key, value ))
        self.order_dict.sort(key = lambda x: x[0])

    def __repr__(self):

        kv_format = lambda x : "'" + x + "'" if isinstance(x, str) else str(x)

        s = '{'
        s += ', '.join( [ kv_format(k) + ' : ' + kv_format(v) for k, v in self.order_dict] )
        s += '}'

        return s

