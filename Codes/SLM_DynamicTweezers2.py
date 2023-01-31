'''
    This program intend to move the trapped atom using SLM.
    
    This file contains the part of HOLOEYE SLM Display SDK
    
    Version: 2.0
    
    
    @created on 30-10-2022
    @last edit on 31-01-2023
    @author: Mayand Dangi
'''
# -*- coding: utf-8 -*-

#--------------------------------------------------------------------#
#                                                                    #
# Copyright (C) 2020 HOLOEYE Photonics AG. All rights reserved.      #
# Contact: https://holoeye.com/contact/                              #
#                                                                    #
# This file is part of HOLOEYE SLM Display SDK.                      #
#                                                                    #
# You may use this file under the terms and conditions of the        #
# "HOLOEYE SLM Display SDK Standard License v1.0" license agreement. #
#                                                                    #
#--------------------------------------------------------------------#

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
#                            Functions                           #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

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
    
def gaussian_beam(res1, res2, sigma):
    x, y = np.meshgrid(np.linspace(-1, 1, res1),np.linspace(-1, 1, res2))
    gauss = np.exp(-0.5*(1/sigma)*(x**2+y**2))
    return gauss

def GS(source, target, retrived_phase, it):
    A = np.exp(retrived_phase*1j)
#     A = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(target)))
#     plt.plot(),plt.imshow(np.abs(np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(A)))), cmap = 'gray')
#     plt.title('T_in'), plt.xticks([]), plt.yticks([])
#     plt.show()
    
    for i in tqdm.tqdm(range(0,it)):
        B = np.abs(source)*np.exp(1j*np.angle(A))
        C = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(B)))
        D = np.abs(target)*np.exp(1j*np.angle(C))
        A = np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(D)))
        
    return np.angle(A)   








# Plays a slideshow on the SLM with pre-calculated 2d phase fields consisting of vertical blazed gratings with different periods.
# The data fields are pre-calculated and uploaded to the GPU once, and then each frame is shown on the SLM by selecting the
# appropriate phase values field on the GPU directly to reach higher performance.

#--- Import Libraries and Modules
import tqdm
import sys, time, math
import detect_heds_module_path
from holoeye import slmdisplaysdk
from slideshow_preload_print_stats import printStat

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import hangu_thepathfinder
# import GS

# Import the SLM Display SDK:
import detect_heds_module_path
from holoeye import slmdisplaysdk

# Import helper function to print timing statistics of the display duration of the handles:
from slideshow_preload_print_stats import printStat

# Import numpy:
if slmdisplaysdk.supportNumPy:
    import numpy as np

# Initializes the SLM library
slm = slmdisplaysdk.SLMInstance()

# Check if the library implements the required version
if not slm.requiresVersion(3):
    exit(1)


# Detect SLMs and open a window on the selected SLM
error = slm.open()
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Open the SLM preview window in non-scaled mode:
# This might have an impact on performance, especially in "Capture SLM screen" mode.
# Please adapt the file showSLMPreview.py if preview window is not at the right position or even not visible.
from showSLMPreview import showSLMPreview
showSLMPreview(slm, scale=0.0)


#------------------------ Configure Parameters -------------------------
# Configure slideshow (steer the laser beam from left to right and back):
# gratingPeriodMin = 8
# gratingPeriodMax = 64
# gratingPeriodStepSize = 4
dataDisplayDurationMilliSec = 1000  # duration of each data frame in ms
repeatSlideshow = -1  # <= 0 (e. g. -1) repeats until Python process gets killed
w = 2
dim_original = 5
spacing_pixel = 50
captured_prob = 0.5
origin = (500,500)
frame = 20

res1 = dim_original*spacing_pixel+origin[0]
res2 = dim_original*spacing_pixel+origin[1]

    
############################################################################################
#                                   Obtain the path                                        #
############################################################################################
moves, moveX, moveY, adj = hangu_thepathfinder.hangu_findpath_XandY(dim_original, spacing_pixel, origin, captured_prob, frame)


#############################################################################################
#                                   animate the tweezers                                    #
#############################################################################################
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
#-------------------------------------------------------------------------------------------#
source = gaussian_beam(res1, res2,0.2)
phase_in = 2*np.pi*np.random.rand(res1 ,res2)
A = source*np.exp(1j*phase_in)

plt.subplot(121),plt.imshow(source, cmap = 'gray')
plt.title('A_in'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(phase_in, cmap = 'gray')
plt.title('A_in_phi'), plt.xticks([]), plt.yticks([])
plt.show()
plt.close()

fig = plt.figure()
#------------------------------------------------------------------------------------------#


'''
if slmdisplaysdk.supportNumPy:
    gratingPeriodList = np.arange(-gratingPeriodMin, -(gratingPeriodMax+1), -gratingPeriodStepSize)
    gratingPeriodList = np.concatenate((gratingPeriodList, np.arange(gratingPeriodMax, gratingPeriodMin-1, -gratingPeriodStepSize)))
    gratingPeriodList = np.concatenate((gratingPeriodList, np.arange(gratingPeriodMin, gratingPeriodMax+1, gratingPeriodStepSize)))
    gratingPeriodList = np.concatenate((gratingPeriodList, np.arange(-gratingPeriodMax, -(gratingPeriodMin-1), gratingPeriodStepSize)))
else:
    print("Cannot find NumPy. This example will be really slow.")

    gratingPeriodList = []
    gratingPeriodList.extend( range(-gratingPeriodMin, -(gratingPeriodMax+1), -gratingPeriodStepSize) )
    gratingPeriodList.extend( range(gratingPeriodMax, gratingPeriodMin-1, -gratingPeriodStepSize) )
    gratingPeriodList.extend( range(gratingPeriodMin, gratingPeriodMax+1, gratingPeriodStepSize) )
    gratingPeriodList.extend( range(-gratingPeriodMax, -(gratingPeriodMin-1), gratingPeriodStepSize) )

print("gratingPeriodList = " + str(gratingPeriodList))
print("len(gratingPeriodList) = " + str(len(gratingPeriodList)))


# Calculate the data we want to show:
print("Calculating data ...")
start_time = time.time()

# Pre-calculate the phase fields in full SLM size:
phaseModulation = 2.0*math.pi  # radian
dataWidth = slm.width_px
dataHeight = slm.height_px # Can be set to 1 to have a faster calculation in case of vertical blazed gratings.
print("dataWidth = " + str(dataWidth))
print("dataHeight = " + str(dataHeight))
'''

durationInFrames = int((float(dataDisplayDurationMilliSec)/1000.0) * slm.refreshrate_hz)
if durationInFrames <= 0:
    durationInFrames = 1  # The minimum duration is one video frame of the SLM

print("slm.refreshrate_hz = " + str(slm.refreshrate_hz))
print("durationInFrames = " + str(durationInFrames))

#####################################################################################
#                               Loading frames to GPU                               #
#####################################################################################

dataHandles = []

for f in range(frame):

    print(f)

    sim = []
    for i in range(len(moveX)):
        sim.append([int(moveX[i][f]), int(moveY[i][f])])
    Array = np.zeros((dim_original*(spacing_pixel)+origin[0], dim_original*(spacing_pixel)+origin[1]))
    for i in sim:
        Array[i[0]-w:i[0]+w, i[1]-w:i[1]+w] = 1
                
    phase = GS(source, Array, phase_in, 50)
    # phaseData = np.abs(np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(source*np.exp(phase*1j)))))

    error, handle = slm.loadPhasevalues(phase)

    # if error == ErrorCode.OutOfVideoMemory:
    #     print("No video memory left at " + str(nHandles) + ". Skipping the rest")
    #     break
    
    # error, handle = slm.loadPhasevalues(phase)
    assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

    handle.durationInFrames = durationInFrames

    error = slm.datahandleApplyValues(handle, slmdisplaysdk.ApplyDataHandleValue.DurationInFrames)
    assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

    dataHandles.append(handle)
    
# Make sure all data was loaded:
for handle in dataHandles:
    error = slm.datahandleWaitFor(handle, slmdisplaysdk.State.ReadyToRender)
    assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

print("100%")
# end_time = time.time()
# print("Calculation took "+ str("%0.3f" % (end_time - start_time)) +" seconds\n")

#----------------------------------------- Show the pre-calculated data:
print("Showing data...")

# Play complete slideshow:
n = 0
while (n < repeatSlideshow) or (repeatSlideshow <= 0):
    n += 1

    print("Show data for the " + str(n) + ". time ...")

    # Play slideshow once:
    for handle in dataHandles:
        error = slm.showDatahandle(handle, slmdisplaysdk.ShowFlags.PresentAutomatic)
        assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

    # Update the handles to the latest state:
    for handle in dataHandles:
        error = slm.updateDatahandle(handle)
        assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

    # Print the actual statistics (last data handle has wrong visible time before any other data was shown):
    print("Showing timing statistics...")
    printStat("loadingTimeMs", dataHandles[0:-1])
    printStat("conversionTimeMs", dataHandles[0:-1])
    printStat("processingTimeMs", dataHandles[0:-1])
    printStat("transferTimeMs", dataHandles[0:-1])
    printStat("renderTimeMs", dataHandles[0:-1])
    printStat("visibleTimeMs", dataHandles[0:-1])

# One last image to clear the SLM screen after the slideshow playback:
# (Also possible by just calling slm.showBlankscreen(128))
data = slmdisplaysdk.createFieldUChar(1, 1)

if slmdisplaysdk.supportNumPy:
    data[0, 0] = 128
else:
    data[0][0] = 128

error, dh = slm.loadData(data)
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

error = slm.showDatahandle(dh, slmdisplaysdk.ShowFlags.PresentAutomatic)
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Release handles and their data to free up video memory:
dataHandles = None

# Wait until the SLM process is closed:
print("Waiting for SDK process to close. Please close the tray icon to continue ...")
error = slm.utilsWaitUntilClosed()
assert error == slmdisplaysdk.ErrorCode.NoError, slm.errorString(error)

# Unloading the SDK may or may not be required depending on your IDE:
slm = None
