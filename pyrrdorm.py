import os
import time
import rrdtool
from collections import defaultdict

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

class Table(object):
    ds = defaultdict(list)
    rra = defaultdict(list)

    def __init__(self):
        pass

    @classmethod
    def Gauge(cls, name, min=0, max=100):
        g = Gauge(name, min=0, max=100)
        Table.ds[cls.TableName()].append(g)
        return g

    @classmethod
    def Derive(cls, name, min=0, max='U'):
        d = Derive(name, min, max)
        Table.ds[cls.TableName()].append(d)
        return d

    @classmethod
    def Avg(cls, steps, rows):
        a = Avg(steps, rows)
        Table.rra[cls.TableName()].append(a)
        return a
        
    @classmethod
    def Fields(cls):
        result = []
        a = lambda x : result.append(x.create_str())
        [a(x) for x in Table.ds[cls.TableName()]]
        [a(x) for x in Table.rra[cls.TableName()]]

        return ", ".join(result)

    def values(self):
        result = []
        [result.append(str(self.__dict__[d.name]))
         for d in Table.ds[self.TableName()]]
            
        return ":".join(result)

tables = []

def add(row_type):
    tables.append(row_type)
    
def run(data_dir):
    for t in tables:
        pathname = os.path.join(data_dir, t.TableName() + ".rrd")
        if not os.path.isfile(pathname):
            cmd = ("rrdtool.create('" + pathname + "', " +
                   "'--step', '" + str(t.step) + "', " +
                   t.Fields() + ")");
            print cmd
            eval(cmd)
    while True:
        time.sleep(15)
        for t in tables:
            pathname = os.path.join(data_dir, t.TableName() + ".rrd")
            v = t()
            print pathname, 'N:' + v.values()
            rrdtool.update(pathname, 'N:' + v.values())
