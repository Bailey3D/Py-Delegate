# Py-Delegate
Simple python module to add a delegate decorator type

```.py
from delegate import delegate


@delegate
def foo():
  print("Foo")
  
def bar():
  print("Bar")
  
foo.bind(bar)
```
