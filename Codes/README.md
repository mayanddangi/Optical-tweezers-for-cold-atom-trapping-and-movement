The DynamicTweezers.py file is a software component that is designed to simulate the movement of optical tweezers. This file is useful in developing and testing algorithms for controlling the motion of optical tweezers, as it enables users to simulate the movement of the tweezers in a virtual environment.

To implement the DynamicTweezers.py file in the physical setup, the SLM_DynamicTweezers2.py file is used. This file serves as an interface between the SLM (Spatial Light Modulator) and the computer, allowing the phase for each move to be obtained and projected onto the SLM in the form of an animation. By using this file, users can project the simulated movement of the optical tweezers onto the SLM, thereby allowing them to observe the actual motion of the tweezers in real-time.

As part of future work, the code will be interfaced with a camera, which will enable the system to provide active feedback. This will allow the intensity of all traps to be equalized, thereby ensuring that all particles are being manipulated in the same way. This will help to improve the accuracy and precision of the system, and will enable it to be used in a wider range of applications.

## Prequisites
Before running or understanding this code, the following software and hardware requirements must be met:

### Software
- Python 3.9
- Holoeye SLM SDK
- Windows 10.0 or higher
- Python libraries: numpy, matplotlib, tqdm, opencv
### Hardware
- GPU (required for animation via SLM)
### Knowledge
- Proficiency in Python object-oriented programming
- Basic understanding of algorithms, optics, and spatial light modulators (SLMs)

## Installation
The program requires the following libraries to run:

 - numpy
 - matplotlib
 - OpenCV
 - tqdm
 - munkers

# Code Documentation

# Hangu - ThePathFinder
Hangu - The Pathfinder is a python program that uses the Hungarian algorithm to find the optimal path for moving an atom. 
The program takes the size of a square matrix (tweezers), spacing between two points, origin (lower left corner of the tweezers), and the probability of capturing an atom as input. 
It then generates a list of coordinates of positions of the trapped atoms in the tweezers. After that, it generates a list of coordinates of targeted atoms, based on the size of the square matrix and spacing between two atoms. 
Finally, it finds the optimal path for moving the trapped atoms to the targeted atoms using the Hungarian algorithm.

## Class definition
The program is defined by a class called `hangu_the_pathfinder`

## Constructor
The `hangu_the_pathfinder` class constructor takes the following input parameters:
  - `dim_original` (int): Dimension of the square matrix (tweezers)
  - `spacing_pixel' (int): spacing between the two tweezers
  - `origin` (tuple): origin i.e. left most corner of the tweezers
  - `captured_prob` (float): probability of capturing an atom at a particular site
  - `frame` (int): number of frames for the animation / movement

In addition to the input parameters, the constructor also takes optional keyword arguments:
  - `simulation` (bool): true: if user want to simulate the movement of tweezers, false: if user have the position of atoms and want to move those pairs (default: True)
  - `inital_array` (list): list of intial positions of trapped atoms. (if `simulation` = False, then user have to provide `initial_array`
  - `target_array` (list): list of target positions for the trapped atoms
  - `showPlot` (bool): whether to show the plot of the target list or not (default: True)

## Methods
The `hangu_the_pathfinder` class has the following methods:

**`plot_adjlist(adj_list, **kwargs)`**
This method plots the adjacency list.
Parameters:
  - `adj_list` (list): list of points to be plotted
  - `dim` (int, optional): dimension of the tweezers (default: `dim_original`)
  - `spacing` (int, optional): spacing between two points (default: `spacing_pixel`)
  - `origin` (tuple, optional): origin of the tweezers (default: `origin`)
Returns:
  - `None`
</br>
</br>

**`random_captured_adjlist(**kwargs)`**
This method returns the list of coordinate points generated randomly, analogous to the trap. In the actual implementation, the "position" of the atom list will be replaced by the actual positions of atoms captured, which will be detected by another system.
Paramters:
  - `dim` (int, optional): Dimension of the tweezers (default dim_original).
  - `spacing` (int, optional): Spacing between two points (default spacing_pixel). 
  - `origin` (tuple, optional): Origin of the tweezers (default origin).
  - `prob` (float, optional): Probability of an atom getting trapped at a particular site (default captured_prob)
Return:
  - a list of coordinate points generated randomly
</br>
</br>

**`get_adjlist(dim, spacing, COM)`**
This method returns the adjacency list of positions of the targeted atoms.
Parameters:
  - `dim` (int): Dimension of the targeted square matrix. 
  - `spacing` (int): required spacing between two atoms. 
  - `COM` (tuple): Coordinates of the centre of the targeted array.
Return:
  - a adjacency list of positions of the targeted atoms
</br>
</br>

**`dist(pos1, pos2)`**
This method returns the Euclidean distance between two positions (points).
Parameters:
  - `pos1` (tuple): position of 1st point
  - `pos2` (tuple): position of 2nd point
Return:
  - euclidean distance between two points
</br>
</br>

**`__getCost(initalArray, targetArray)`**
This function computes the cost matrix between the initial and target arrays using the Euclidean distance between each pair of atoms in the two arrays. The cost matrix is used in the Hungarian algorithm to find the optimal matching between the two arrays.

Parameters:
  - `initalArray` (list): a list of tuples representing the initial positions of atoms
  - `targetArray` (list): a list of tuples representing the target positions of atoms
Returns:
  - a list cost representing the cost matrix
  - a list `initialArray` representing the initial positions of atoms
  - an integer difference representing the difference between the number of atoms in `initalArray` and `targetArray`
</br>
</br>

**`hangu_findpath_XandY()`**
This function finds the optimal path between the initial and target arrays using the Hungarian algorithm. It first generates a random array equivalent to the position of captured atoms in a lattice. Then, it sets the target dimension for the continuous square array and computes the cost matrix using the __getCost() function. Next, it calculates the moves using the Hungarian algorithm and generates the X and Y coordinates for each atom in each frame.

Parameters:
  - `None`
Returns:
  - a list moves representing the moves made by each atom
  - a 2D numpy array moveX representing the X coordinates for each atom in each frame
  - a 2D numpy array moveY representing the Y coordinates for each atom in each frame
  - a list self.adj representing the initial positions of atoms

## Example to use
```
from hangu_thepathfinder_class import hangu_the_pathfinder


dim_original = 5
spacing_pixel = 50
captured_prob = 0.5
origin = (50,50)
frame = 10


hangu_moves = hangu_the_pathfinder(dim_original, spacing_pixel, origin, captured_prob, frame)
moves, moveX, moveY, a = hangu_moves.hangu_findpath_XandY()
```


# GS.py
## Methods
**`gaussian_beam(res1, res2, sigma)`**
This function generates a 2D Gaussian beam with given resolution and sigma.
Parameters:
  - `res1` (int): The resolution of the Gaussian beam in the x direction.
  - `res2` (int): The resolution of the Gaussian beam in the y direction.
  - `sigma` (float): The standard deviation of the Gaussian distribution.
Returns:
  - a 2D numpy array representing the generated Gaussian beam.
</br>
</br>

**`GS(source, target, retrived_phase, it)`**
This function implements the Gerchberg-Saxton (GS) algorithm for phase retrieval from a given source and target. The GS algorithm iteratively updates the phase of the retrieved wavefront until it matches the phase of the target wavefront.

Parameters:
  - `source` (numpy.ndarray): a 2D numpy array representing the complex amplitude of the source wavefront.
  - `target` (numpy.ndarray): a 2D numpy array representing the complex amplitude of the target wavefront.
  - `retrived_phase`(numpy.ndarray): a 2D numpy array representing the initial phase of the wavefront.
  - `it` (int): The number of iterations for the GS algorithm.
Returns:
  - a 2D numpy array representing the phase of the retrieved wavefront after the GS algorithm has converged to a solution.


# DynamicTweezers.py
This Python script comprises a sequence of routines for pathfinding and animating a path for a 5-dimensional array. This programme shows how to use the hangu the pathfinder class. For more detail go with the flow of code.


## Credits
The program is developed by Mayand Dangi.
