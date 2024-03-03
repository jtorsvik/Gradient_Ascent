# MCMCS Formative Coursework
# Luc Berthouze 2021-11-02

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
    
# Definition of a Simple landscape
def SimpleLandscape(x, y):
    return np.where(1-np.abs(2*x)>0,1-np.abs(2*x)+x+y,x+y)
    
# Definition of the gradient of the Simple landscape
def SimpleLandscapeGrad(x, y):
    """This function should return the gradient of the landscape at point x,y"""
    # TO DO: Initialise a vector g containing the gradient
    g = ...
    # TO DO: Keeping into account the definition of the function, calculate the value of g. 
    # There are 3 scenarios on the value of x to consider (use if, elif, else instructions)
    # If you cannot figure it out from the specification of the function itself, plot it! 

    return g

# Function to draw a surface (equivalent to ezmesh in Matlab)
# See argument cmap of plot_surface instruction to adjust color map (if so desired)
def DrawSurface(fig, varxrange, varyrange, function):
    """Function to draw a surface given x,y ranges and a function."""
    ax = fig.gca(projection='3d')
    xx, yy = np.meshgrid(varxrange, varyrange, sparse=False)
    z = function(xx, yy)
    ax.plot_surface(xx, yy, z, cmap='RdBu') # color map can be adjusted, or removed! 
    fig.canvas.draw()
    return ax


# Function implementing gradient ascent
def GradAscent(StartPt,NumSteps,LRate):
    for i in range(NumSteps):
        # TO DO: Calculate the 'height' at StartPt using SimpleLandscape
        
        # TO DO: Plot point on the landscape 
        # Use a markersize that you can see well enough (e.g., * in size 10)
        
        # TO DO: Calculate the gradient at StartPt using SimpleLandscapeGrad
        
        # TO DO: Calculate the new point and update StartPt
        
        # Ensure StartPt is within the specified bounds (un/comment relevant lines)
        StartPt = np.maximum(StartPt,[-2,-2])
        StartPt = np.minimum(StartPt,[2,2])

# Template 
# Plot the landscape (un/comment relevant line)
fig = plt.figure()
ax = DrawSurface(fig, np.arange(-2,2.025,0.025), np.arange(-2,2.025,0.025), SimpleLandscape)

# Enter maximum number of iterations of the algorithm, learning rate and mutation range
NumSteps=50  # You can change this
LRate=0.35  # You can change this

# TO DO: choose a random starting point with x and y in the range (-2, 2)

# Find maximum (un/comment relevant line)
GradAscent(StartPt,NumSteps,LRate)












