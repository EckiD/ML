import pandas as pd
import numpy as np
from numpy.lib import recfunctions as rfn

wtype = np.dtype([('x', 'f4'), ('vx', 'f4')])


x = np.array([1.2, 3.4])
vx = np.array([13.0, 18.1])
data = np.empty(len(x), dtype=wtype)
data['x'] = x
data['vx'] = vx


x1 = np.array([2.2, 4.4])
vx1 = np.array([14.0, 19.1])
data1 = np.empty(len(x1), dtype=wtype)
data1['x'] = x1
data1['vx'] = vx1

# x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
#             ...              dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])

# Create DataFrame
print(data.dtype.names)
np.lib.mixins
joined = rfn.join_by(data.dtype.names, data, data1, jointype='outer')

df = pd.DataFrame(data)
print(df.x)
print(data['x'])
print(data1['x'])
print(joined['vx'])
print(joined[2])
