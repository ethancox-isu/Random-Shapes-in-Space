import random
import math
import plotly.express as px
import plotly.graph_objects as go
from weight_generators import randomWeightsIntervalSplit, randomWeightsSumAverage

def plotPoints(points, weightFunc, N):
    # This will be a *list* of *tuples* where each tuple is (x, y, z)
    generated_points = []
    # Iterate N times -- how many random points we want
    for i in range(0, N):
        # Generate weights for all our points
        weights = weightFunc(len(points))
        accum_x = 0
        accum_y = 0
        accum_z = 0
        # For each point, add the x/y/z multiplied by the point's weight
        for i in range(0, len(points)):
            accum_x += points[i][0]*weights[i]
            accum_y += points[i][1]*weights[i]
            accum_z += points[i][2]*weights[i]
            #print(str(accum_x) + " " + str(accum_y) + " " + str(accum_z))
        # Then append this point to generated_points we made
        generated_points.append((accum_x, accum_y, accum_z))

    # List comprehensions; shorthand to iterate through and pluck out the X/Y/Z coordinates so we can use plotly
    Xs = [p[0] for p in generated_points]
    Ys = [p[1] for p in generated_points]
    Zs = [p[2] for p in generated_points]

    # Draw
    #pt_sizes = [10 for x in range(len(Xs))]
    #fig = px.scatter_3d(x=Xs, y=Ys, z=Zs, size=pt_sizes, range_x=[-1, 5], range_y=[-1, 5], range_z=[-1, 5])
    #fig.show()

    # point arrays to draw lines between every point
    lineXs, lineYs, lineZs = [], [], []
    for i in range(len(points)-1):
        for j in range(i, len(points)):
            lineXs.append(points[i][0])
            lineXs.append(points[j][0])
            
            lineYs.append(points[i][1])
            lineYs.append(points[j][1])
            
            lineZs.append(points[i][2])
            lineZs.append(points[j][2])


    goFigure = go.Figure()
    goFigure.add_trace(go.Scatter3d(x=Xs, y=Ys, z=Zs, mode="markers", marker={"size": 1}))
    goFigure.add_trace(go.Scatter3d(x=lineXs, y=lineYs, z=lineZs, mode="lines", line={"width": 1}))

    goFigure.show()

    #print(generated_points)


points = [
    (0, 0, 0),
   # (4, 0, 0),
    #(0, 4, 0),
    (2, 2, 4),
    (4, 4, 0)
]

plotPoints(points, randomWeightsIntervalSplit, 10000)
#plotPoints(points, randomWeightsSumAverage, 500)
