The DynamicTweezers.py file is a software component that is designed to simulate the movement of optical tweezers. This file is useful in developing and testing algorithms for controlling the motion of optical tweezers, as it enables users to simulate the movement of the tweezers in a virtual environment.

To implement the DynamicTweezers.py file in the physical setup, the SLM_DynamicTweezers2.py file is used. This file serves as an interface between the SLM (Spatial Light Modulator) and the computer, allowing the phase for each move to be obtained and projected onto the SLM in the form of an animation. By using this file, users can project the simulated movement of the optical tweezers onto the SLM, thereby allowing them to observe the actual motion of the tweezers in real-time.

As part of future work, the code will be interfaced with a camera, which will enable the system to provide active feedback. This will allow the intensity of all traps to be equalized, thereby ensuring that all particles are being manipulated in the same way. This will help to improve the accuracy and precision of the system, and will enable it to be used in a wider range of applications.

## Prequisites
Before running or understanding this code, the following software and hardware requirements must be met:

### Software
- Python 3.0
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

## Credits
The program is developed by Mayand Dangi.


Hangu - The Pathfinder is a program designed to find the optimal path for moving an atom using the Hungarian algorithm. The program takes input of the size of a square matrix (tweezers), spacing between two points, origin (lower left corner of the tweezers), and the probability of capturing an atom. It generates a list of coordinates of positions of the trapped atoms in the tweezers. Then, it generates a list of coordinates of targeted atoms, based on the size of the square matrix and spacing between two atoms. Finally, it finds the optimal path for moving the trapped atoms to the targeted atoms using the Hungarian algorithm.



