'''
        
    Version: 1.1
    
    
    @created on 30-10-2022
    @last edited on 30-01-2023
    @author: Mayand Dangi
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# import hangu_thepathfinder
from hangu_thepathfinder_class import hangu_the_pathfinder
import GS


dim_original = 5
spacing_pixel = 50
captured_prob = 0.5
origin = (50,50)
frame = 10

res1 = dim_original*spacing_pixel+origin[0]
res2 = dim_original*spacing_pixel+origin[1]

hangu_moves = hangu_the_pathfinder(dim_original, spacing_pixel, origin, captured_prob, frame)
moves, moveX, moveY, a = hangu_moves.hangu_findpath_XandY()

# moves, moveX, moveY, a = hangu_thepathfinder.hangu_findpath_XandY(dim_original, spacing_pixel, origin, captured_prob, frame)


'''
    Animate the tweezers
'''
def slide(f):
    if(f>0 and f<frame):
        ax.cla()
        sim = []
        for i in range(len(moveX)):
            sim.append([int(moveX[i][f]), int(moveY[i][f])])
        plot(sim, dim_original, spacing_pixel, origin)
        


def plot(target_list, dim, spacing, origin):
    Array = np.zeros((dim*(spacing)+origin[0], dim*(spacing)+origin[1]))
    for i in target_list:
        Array[i[0], i[1]] = 1
#     plotArray(arr)
    i = 0
    j = 0
    x = []
    y = []
    while i<len(Array):
        while j<len(Array[0]):
            if Array[i][j] == True:
                x.append(j)
                y.append(i)
            j += 1
        i += 1
        j = 0
    ax.plot(x,y,'ro')
    plt.grid(True)
    plt.autoscale(False)
    plt.ylim(-1,len(Array))
    plt.xlim(-1,len(Array))


plt.close()
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
anim  = animation.FuncAnimation(fig, slide, interval = 10)
plt.show()
plt.close()
#-----------------------------------------------------------------------------

source = GS.gaussian_beam(res1, res2,0.2)
phase_in = 2*np.pi*np.random.rand(res1 ,res2)
A = source*np.exp(1j*phase_in)

plt.subplot(121),plt.imshow(source, cmap = 'gray')
plt.title('A_in'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(phase_in, cmap = 'gray')
plt.title('A_in_phi'), plt.xticks([]), plt.yticks([])
plt.show()

'''
for f in range(0,frame):
    sim = []
    for i in range(len(moveX)):
        sim.append([int(moveX[i][f]), int(moveY[i][f])])

    Array = Array = np.zeros((dim_original*(spacing_pixel)+origin[0], dim_original*(spacing_pixel)+origin[1]))
    for i in sim:
        Array[i[0]-2:i[0]+2, i[1]-2:i[1]+2] = 1
    phase = GS.GS(source, Array, phase_in,10)
    plt.imshow(np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j))))))
    plt.show()
'''

'''
def plot_adj2(target_list, dim, spacing, origin):
    Array = np.zeros((dim*(spacing)+origin[0], dim*(spacing)+origin[1]))
    for i in target_list:
        Array[i[0]-2:i[0]+2, i[1]-2:i[1]+2] = 1
    phase = GS.GS(source, Array, phase_in,10)
    imobj.set_array(np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j))))))
    plt.grid(True)
    plt.autoscale(False)
    plt.ylim(-1,len(Array))
    plt.xlim(-1,len(Array))
    return imobj

  
def slide_phase(f):
    if(f>0 and f<frame):
        ax.cla()
        sim = []
        for i in range(len(moveX)):
            sim.append([int(moveX[i][f]), int(moveY[i][f])])
        im = plot_adj2(sim, dim_original, spacing_pixel, origin)
        return [im]
'''

'''
def slide_phase(f):
    if(f>0 and f<frame):
        sim = []
        for i in range(len(moveX)):
            sim.append([int(moveX[i][f]), int(moveY[i][f])])
        Array = np.zeros((dim_original*(spacing_pixel)+origin[0], dim_original*(spacing_pixel)+origin[1]))
        for i in sim:
            Array[i[0]-2:i[0]+2, i[1]-2:i[1]+2] = 1
            
        phase = GS.GS(source, Array, phase_in,10)
        arr = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j)))))
        im.set_array(arr)
#         plt.grid(True)
#         plt.autoscale(False)
#         plt.ylim(-1,len(Array))
#         plt.xlim(-1,len(Array))
        return im,
'''



plt.close()
fig = plt.figure()

sim = []
for i in range(len(moveX)):
    sim.append([int(moveX[i][0]), int(moveY[i][0])])
Array = np.zeros((dim_original*(spacing_pixel)+origin[0], dim_original*(spacing_pixel)+origin[1]))
for i in sim:
    Array[i[0]-2:i[0]+2, i[1]-2:i[1]+2] = 1
            
phase = GS.GS(source, Array, phase_in,10)
arr = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j)))))
im = plt.imshow(arr, animated = True)



def slide_phase1(f):
    if(f<frame):
        sim = []
        for i in range(len(moveX)):
            sim.append([int(moveX[i][f]), int(moveY[i][f])])
        Array = np.zeros((dim_original*(spacing_pixel)+origin[0], dim_original*(spacing_pixel)+origin[1]))
        for i in sim:
            Array[i[0]-2:i[0]+2, i[1]-2:i[1]+2] = 1
                
        phase = GS.GS(source, Array, phase_in,50)
        arr = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j)))))
        im.set_array(arr)
        
        return [im]
        
        
anim  = animation.FuncAnimation(fig, slide_phase1, interval = 500)
plt.show()
# anim.save("Animation.gif", dpi=300, writer=PillowWriter(fps=25))

# plt.close()


