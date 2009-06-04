import os
import time
import rrdtool

class Gauge(object):
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max
    def create_str(self):
        result = []
        result.append("DS")
        result.append(self.name)
        result.append("GAUGE")
        result.append("30")
        result.append(str(self.min))
        result.append(str(self.max))
        return "'" + ":".join(result) + "'"

class Derive(object):
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max
    def create_str(self):
        result = []
        result.append("DS")
        result.append(self.name)
        result.append("DERIVE")
        result.append("30")
        result.append(str(self.min))
        result.append(str(self.max))
        return "'" + ":".join(result) + "'"

class Avg(object):
    def __init__(self, steps, rows):
        self.steps = steps
        self.rows = rows
    def create_str(self):
        result = []
        result.append("RRA")
        result.append("AVERAGE")
        result.append(str(0.5))
        result.append(str(self.steps))
        result.append(str(self.rows))
        return "'" + ":".join(result) + "'"

class Row(object):
    def __init__(self):
        pass

    def Gauge(cls, name, min, max):
        g = Gauge(name, min, max)
        cls.ds.append(g)
        return g
    Gauge = classmethod(Gauge)

    def Derive(cls, name, min, max):
        d = Derive(name, min, max)
        cls.ds.append(d)
        return d
    Derive = classmethod(Derive)

    def Avg(cls, steps, rows):
        if not cls.ds:
            cls.ds = []
        if not cls.rra:
            rra = []
        a = Avg(steps, rows)
        cls.rra.append(a)
        return a
    Avg = classmethod(Avg)
        
    def Fields(cls):
        result = []
        for d in cls.ds:
            result.append(d.create_str())
        for a in cls.rra:
            result.append(a.create_str())
        return ", ".join(result)
    Fields = classmethod(Fields)

    def values(self):
        result = []
        for d in self.ds:
            result.append(str(self.__dict__[d.name]))
        return ":".join(result)

tables = []

def add(row_type):
    tables.append(row_type)
    
def run(data_dir):
    for t in tables:
        pathname = os.path.join(data_dir, t.__name__ + ".rrd")
        if not os.path.isfile(pathname):
            cmd = ("rrdtool.create('" + pathname + "', " +
                   "'--step', '" + str(t.step) + "', " +
                   t.Fields() + ")");
            print cmd
            eval(cmd)
    while True:
        time.sleep(15)
        for t in tables:
            pathname = os.path.join(data_dir, t.__name__ + ".rrd")
            v = t()
            print pathname, 'N:' + v.values()
            rrdtool.update(pathname, 'N:' + v.values())
