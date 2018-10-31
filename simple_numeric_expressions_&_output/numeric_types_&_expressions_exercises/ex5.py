'''
Force on a Sail. How much force is on a sail?

A sail moves a boat by transferring force to its mountings. The sail in the front (the jib)
of a typical fore-and-aft rigged sailboat hangs from a stay. The sail in the back (the main) 
hangs from the mast. The forces on the stay (or mast) and sheets move the boat. The sheets 
are attached to the clew of the sail.

The force on a sail, f, is based on sail area, a (in square feet) and wind speed, ‘w‘ 
(in miles per hour).

f = w**2*0.004*a

For a small racing dinghy, the smaller sail in the front might have 61 square foot of surface.
The larger , mail sail, might have 114 square foot.

Write a print statement to figure the force generated by a 61 square foot sail in 15 miles an 
hour of wind.
'''

#sail surface area
a = 61

#wind speed
w = 15

#force of wind
f = w**2*0.004*a

print('Force generated by 61 sq.ft sail in 15mph wind: ', f)