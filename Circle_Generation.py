import random
import math
import plotly.express as px
df = px.data.iris
#import numpy as np
#import matplotlib.pyplot as plt
'''
x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

for i in range(0, 100):
    theta = random.random() * 2 * math.pi
#    print(f"({math.cos(theta)}, {math.sin(theta)})")
'''
x1 = (0, 0, 0)
x2 = (1, 0, 0)
x3 = (1, 1, 1)

N = 500
a1 = 0
a2 = 0
a3 = 0
Xs = []
Ys = []
Zs = []
for i in range(0, N):
    r1 = random.random()
    r2 = random.random()
    mx = max(r1, r2)
    mn = min(r1, r2)
    w1 = 1 - mx
    w2 = mx - mn
    w3 = mn
    point = (
        w1*x1[0]+w2*x2[0]+w3*x3[0],
        w1*x1[1]+w2*x2[1]+w3*x3[1],
        w1*x1[2]+w2*x2[2]+w3*x3[2]
    )
    Xs.append(point[0])
    Ys.append(point[1])
    Zs.append(point[2])
    print(point)


print(randomWeightsSumAverage(5))

#fig = px.scatter_3d(x=Xs, y=Ys, z=Zs)
#fig.show()
#rands = [random.random() for r in range(0, N)]
#points = [(math.cos(r*math.pi*2), math.sin(r*math.pi*2)) for r in rands]
#[print(pt) for pt in points]
