# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt 


data_in = '/home/pressions/SATELITIME/data/ZR/swf/chl_32d/9km/S19972731997304.L3m_R32_CHL_chlor_a_9k_ZR.npy'


l3d=np.load(data_in)
l3d=l3d*1+0
plt.imshow(l3d)
plt.show()

print 'fin'

