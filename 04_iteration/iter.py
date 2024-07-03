import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def akanksha(b):
    a = np.array(b)
    print(a)

# with file--->__next__()
'''>>> f = open("iter.py")
>>> f
<_io.TextIOWrapper name='iter.py' mode='r' encoding='cp65001'>
>>> f.readline()
'import math\n'
>>> f.readline()
'import numpy as np\n'
>>> f.readline()
'import pandas as pd\n'
>>> f.readline()
'import matplotlib.pyplot as plt\n'
>>> f.readline()
'def akanksha(b):\n'
>>> f.readline()
'    a = np.array(b)\n'
>>> f.readline()
'    print(a)\n'
>>> f.readline()
'\n'
>>> f.readline()
'' ---> line break
'''




'''
>>> f = open("iter.py")
>>> f.__next__()
'import numpy as np\n'
>>> f.__next__()
'import pandas as pd\n'
>>> f.__next__()
'import matplotlib.pyplot as plt\n'
'''



'''
>>> for line in open("iter.py"):
...     print(line,end="")
...
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def akanksha(b):
    a = np.array(b)
    print(a)

'''


'''
>>> f = open("iter.py")      
>>> while True:
...     line = f.readline()
...     if not line:break    
...     print(line,end="")
...
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def akanksha(b):
    a = np.array(b)
    print(a)

'''

# with list---->__next__()
'''
>>> l = [1,2,3,4]
>>> I=iter(l) 
>>> I
<list_iterator object at 0x000002001704BA00>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x000002001704BA00>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

#with dictionary--->__next__()
'''
>>> d = {"a":1,"b":2}
>>> for i in d.values():
...     print(i) 
...
1
2
>>> I = iter(d)
>>> I
<dict_keyiterator object at 0x00000200175441D0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''


#with range--->__next__()
'''
>>> R = range(5) 
>>> R
range(0, 5)
>>> I = iter(R) 
>>> I
<range_iterator object at 0x0000020016F7BA90>
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''