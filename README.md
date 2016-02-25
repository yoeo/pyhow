# pyhow
Learn python by playing with sample codes and become a guru... (one day in the far \_\_future\_\_)

An example of output:
```
>>>  ITERTOOLS LIBRARY SAMPLES.


COMBINATION


  CHAIN: Merge multiple iteratiors.
    |
    |  def chain():
    |      chained = itertools.chain('BAG', 'DAD')
    |      return ''.join(chained)
    |
    |-- chain() = 'BAGDAD'


  GROUPBY: Group sorted elements.
    |
    |  def groupby():
    |      def square(value):
    |          return  value**2
    |      sorted_items = sorted(range(-2, 3), key=square)
    |      grouped = itertools.groupby(sorted_items, key=square)
    |      return dict((key, list(values)) for key, values in grouped)
    |
    |-- groupby() = {0: [0], 1: [-1, 1], 4: [-2, 2]}

```

##How to use it?
###Requirements
The only requirements are **python** and **python-setuptools**.

###Install
You can install **pyhow** on your system or virtualenv:
```
python setup.py install
```

###Run
```
```
