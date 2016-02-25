# pyhow
Learn python by playing with sample codes and become a guru... (one day in the far \_\_future\_\_)

## Description
**pyhow** is a collection of sample codes that uses and explains python core components.

You will find sample code for **built-in** functions classes, exceptions, obejcts and for some modules like **itertools**, **functools** etc...

### An example of output:
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

## How to use it?
### Requirements
The only requirements are **python** and **python-setuptools**.

### Install
You can install **pyhow** on your system or virtualenv:
```
python setup.py install
```

###Run
Usage
```
pyhow <sample-name>
```
For exemple, to show the string formating samples
```
pyhow string_format
```
Help and available samples
```
usage: pyhow [-h]
             {builtin_exceptions,builtin_objects,lib_functools,lib_itertools,string_format}

Select one of the following samples:
  builtin_exceptions: built-in exceptions samples.
  builtin_objects: built-in values and types samples.
  lib_functools: functools library samples.
  lib_itertools: itertools library samples.
  string_format: string formating language samples.

positional arguments:
  {builtin_exceptions,builtin_objects,lib_functools,lib_itertools,string_format}

optional arguments:
  -h, --help            show this help message and exit
```

Have fun!
