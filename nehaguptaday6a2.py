#!/usr/bin/env python
# coding: utf-8

# # FOR FINDING CONE SURFACE AREA AND VOLUME

# In[12]:


import math

radius = float(input('Please Enter the Radius of a Cone: '))
height = float(input('Please Enter the Height of a Cone: '))

# Calculate Length of a Slide (Slant)
l = math.sqrt(radius * radius + height * height)

# Calculate the Surface Area
SA = math.pi * radius * (radius + l)

# Calculate the Volume
Volume = (1.0/3) * math.pi * radius * radius * height


print("\n Length of a Side (Slant)of a Cone = %.2f" %l)
print(" The Surface Area of a Cone = %.2f " %SA)
print(" The Volume of a Cone = %.2f" %Volume)


# # endd------------------
