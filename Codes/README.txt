Hangu - The Pathfinder
Hangu - The Pathfinder is a program designed to find the optimal path for moving an atom using the Hungarian algorithm. The program takes input of the size of a square matrix (tweezers), spacing between two points, origin (lower left corner of the tweezers), and the probability of capturing an atom. It generates a list of coordinates of positions of the trapped atoms in the tweezers. Then, it generates a list of coordinates of targeted atoms, based on the size of the square matrix and spacing between two atoms. Finally, it finds the optimal path for moving the trapped atoms to the targeted atoms using the Hungarian algorithm.

The program is developed in Python 3.0 and uses various libraries like numpy, matplotlib, OpenCV, etc.

Installation
The program requires the following libraries to run:

numpy
matplotlib
OpenCV
tqdm
munkers
The above libraries can be installed using the following command:

bash
Copy code
pip install numpy matplotlib opencv-python tqdm munkers
Usage
To use the program, follow the steps below:

Clone the repository or download the source code.

Navigate to the project directory and open the terminal.

Run the hangu_the_pathfinder.py file using the command:

bash
Copy code
python hangu_the_pathfinder.py
The program will prompt for the required inputs like the size of the tweezers, spacing between two points, origin, etc. Enter the values and follow the prompts.

The program will generate the list of coordinates of the trapped atoms and the targeted atoms. It will also display the adjacency list of the targeted atoms.

The program will then find the optimal path for moving the trapped atoms to the targeted atoms using the Hungarian algorithm.

Finally, the program will display a graph showing the movement of atoms from the initial position to the target position.

Credits
The program is developed by Mayand Dangi.




