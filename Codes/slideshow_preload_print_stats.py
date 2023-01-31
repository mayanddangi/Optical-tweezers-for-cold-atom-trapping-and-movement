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


from holoeye import slmdisplaysdk

# Function to print some statistics:
def printStat(stat, dataHandles):
    sum = 0.0
    count = 0
    min = 10000
    max = -10000

    for handle in dataHandles:
        # get the stat from the handle
        v = getattr(handle, stat)

        # check if this action did happen at all
        if v == slmdisplaysdk.Datahandle.NotDone:
            continue

        # process value
        sum += float(v)
        count += 1

        if v < min:
            min = v

        if v > max:
            max = v

    # check if any handle did this action
    if count > 0:
        avg = sum / count

        print("    {0:<24} -> min: {1:<3}  -  avg: {2:6.2f}  -  max: {3:<3}".format(stat, min, avg, max))
    else:
        print("    {0:<24} -> min: {1}  -  avg:   {1}  -  max: {1}".format(stat, "n/a"))