weight = 1.5

if weight <= 2:
  cost_ground = weight * 1.50 + 20

elif weight <= 6:
 cost_ground = weight * 3 + 20

elif weight <= 10:
 cost_ground = weight * 4 + 20

else:  cost_ground = weight * 4.75 + 20

cost_premium=125

if weight <= 2:
  cost_drone = weight * 4.50

elif weight <= 6:
 cost_drone = weight * 9

elif weight <= 10:
 cost_drone = weight * 12

else:  cost_drone = weight * 14.25

print("Ground Pricing = $",cost_ground)
print("Premium Ground Pricing = $",cost_premium)
print("Drone Pricing = $",cost_drone)