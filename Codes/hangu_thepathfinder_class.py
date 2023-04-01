'''    
    Hangu - The Pathfinder is a program to find the optimal path for moving an atom using the Hungarian algorithm.
    The program takes input of the size of a square matrix (tweezers), spacing between two points, origin (lower left corner of the tweezers), and the probability of capturing an atom. It generates a list of coordinates of positions of the trapped atoms in the tweezers. Then, it generates a list of coordinates of targeted atoms, based on the size of the square matrix and spacing between two atoms. Finally, it finds the optimal path for moving the trapped atoms to the targeted atoms using the Hungarian algorithm.

    @author: Mayand Dangi  
    Version: 3.0
    
        
    @created on 30-10-2022
    @last edit on 30-01-2023
'''

# ---- Package Import ----
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import cv2
import tqdm
import munkers

class hangu_the_pathfinder:
    def __init__(self, dim_original, spacing_pixel, origin, captured_prob, frame, **kwargs):
        self.dim_original = dim_original
        self.spacing_pixel = spacing_pixel
        self.origin = origin
        self.captured_prob = captured_prob
        self.frame = frame
        
        self.dim_target = None
        self.COM = None
        

    '''
        Plot the target list

        @input params
            target_list :   List of Points
            dim         :   Dimension of the Tweezers
            spacing     :   spacing between two points
            origin      :   Origin: left-lower point

        return type void
    '''    
    def plot_adjlist(self, target_list, **kwargs):        
        dim = self.dim_original
        spacing = self.spacing_pixel
        origin = self.origin
        
        for key, value in kwargs.items():
            if(key=='dim'):
                dim = value
            if(key=='spacing'):
                spacing = value
            if(key=='origin'):
                origin = value
                
        Array = np.zeros((dim*(spacing)+origin[0]+spacing, dim*(spacing)+origin[1]+spacing))
        for i in target_list:
            Array[i[0], i[1]] = 1

        x=[]
        y=[]
        for i in range(len(Array)):
            for j in range(len(Array)):
                if(Array[i][j] == True):
                    x.append(j)
                    y.append(i)

        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.plot(x,y,'ro')
        plt.grid(True)
        plt.autoscale(False)
        plt.ylim(-1,len(Array))
        plt.xlim(-1,len(Array))
        plt.show()
    
    
    '''
        Returns the list of coordinate point generated randomly analoagous to the trap.
        In the actual implementation the "position" of atom list will be replaced by the actual
        positions of atom captured which will be detected by another system.

        @input params
            dim         :   Dimension of the Tweezers
            spacing     :   spacing between two points
            probability :   probability of atom getting trap at a particular sites
            origin      :   lower left point

        @return :   list of coordinates of positin of trapped atom)
    '''
    def random_captured_adjlist(self, **kwargs):
        dim = self.dim_original
        spacing = self.spacing_pixel
        origin = self.origin
        probability = self.captured_prob
        
        for key, value in kwargs.items():
            if(key=='dim'):
                dim = value
            if(key=='spacing'):
                spacing = value
            if(key=='origin'):
                origin = value
            if(key=='prob'):
                probability = value
                
        position = []
        for i in range(0, dim*(spacing), spacing):
            for j in range(0, dim*(spacing), spacing):
                b = random.random()
                if(b>probability):
                    position.append((i+origin[0], j+origin[1]))
        return position
    
    
    '''
        Return the adjacency list of positions of targeted atoms 

        @input params
            dim     :   Dimension of targeted square matrix
            spacing :   required spacing between two atoms
            COM     :   coordinates of centre of targated array

        @return :   adjacency list and coordinate intervals in x and y directions
    '''
    def get_adjlist(self, dim, spacing, COM):
        x = (float(dim*spacing)-1)/2
        row_interval = [int(COM[0] - x), int(COM[0] + x)]
        col_interval = [int(COM[1] - x), int(COM[1] + x)]


        targetArray = []
        for i in range(row_interval[0], row_interval[1], spacing):
            for j in range(col_interval[0], col_interval[1], spacing):
                targetArray.append((i,j))

        return targetArray  
    
    def dist(self, pos1,pos2):
        return (pos1[1] - pos2[1])**2+(pos1[0] - pos2[0])**2

    
    '''
        Return the cost matrix based on the square of distance between the targated and reservoir sites
    '''
    def getCost(self, initalArray,targetArray):
        initial_atoms = len(initalArray)
        row = []
        cost = []
        difference = initial_atoms - len(targetArray)
        if(difference >= 0):
            for i in range(0, len(targetArray)):
                for j in range(0, initial_atoms):
                    row.append(self.dist(initalArray[j], targetArray[i]))
                cost.append(row)
                row = []
            row = [0]*(initial_atoms)
            for i in range(0, difference):
                cost.append(row)
            return [cost, initalArray, difference]
        else:
            print("insufficient initial_atoms")
            return[0,0]
   

    # Main Function: returns the X and Y coordinate of each atoms accordance with frame
    def hangu_findpath_XandY(self, **kwargs):

        # Generate Random array equivalent to the position of captured atom in lattice
        adj = self.random_captured_adjlist() # (self.dim_original, self.spacing_pixel, self.captured_prob, self.origin)
        self.plot_adjlist(adj)

        # Set the target dimension for the continous square array
        if(self.dim_target is None):
            self.dim_target = int((len(adj))**0.5)

        #------------------- Obtain Centre ----------------------------
        x = 0
        y = 0
        for i in adj:
            x+=i[0]
            y+=i[1]
        self.COM = (round(x/len(adj),0), round(y/len(adj),0))
        #-------------------------------------------------------------

        # Obtain the position of Targeted array
        target = self.get_adjlist(self.dim_target, self.spacing_pixel, self.COM)
        self.plot_adjlist(target)

        # Compute the cost matrix
        cost, initialArray, difference = self.getCost(adj, target)
        print(f'Inital positions: {initialArray}/nFinal positions: {target}')

        # Calculate moves using Hungarian Algorithm
        m = munkers.Munkres()
        hungarian_matching = m.compute(cost)
        moves = []

        for i in range(0, len(hungarian_matching)):
            if(hungarian_matching[i][0] < len(target)):
                # Move: initialArray[hungarian_matching[i][1]] --> target[hungarian_matching[i][0]]
                moves.append((initialArray[hungarian_matching[i][1]] ,target[hungarian_matching[i][0]]))
            else:
                # Move: initialArray[hungarian_matching[i][1]] --> initialArray[hungarian_matching[i][1]]
                moves.append((initialArray[hungarian_matching[i][1]], initialArray[hungarian_matching[i][1]]))


        moveX = np.zeros((len(moves), self.frame))
        moveY = np.zeros((len(moves), self.frame))

        for i in range(self.frame):
            temp = []
            for t in range(len(moves)):
                d_x = (moves[t][1][0]-moves[t][0][0])/(self.frame-1)
                moveX[t][i] = int(moves[t][0][0] + i*d_x)
                d_y = (moves[t][1][1]-moves[t][0][1])/(self.frame-1)
                moveY[t][i] = int(moves[t][0][1] + i*d_y)

        return [moves, moveX, moveY, adj]