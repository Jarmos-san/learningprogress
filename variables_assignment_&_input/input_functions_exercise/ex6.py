'''
Force from a Sail. Input the height of the sail and the length. The surface area is 1/2×h×l. For
a wind speed of 25 MPH, compute the force on the sail. Small boat sails are 25-35 feet high 
and 6-10 feet long.
'''
#height
h = int(input('Enter sail height ranged between 25-35: '))
l = int(input('Enter sail length ranged between 6-10: '))

#sail surface area
a = 1/2 * h * l

#wind speed
w = int(input('What is the wind speed? '))

#force of wind
f = w**2*0.004*a

print('Force generated by sail in 25mph wind: ', f)