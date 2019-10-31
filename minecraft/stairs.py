# Connect to MineCraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get our current position
x, y, z = mc.player.getPos()

# define our blocks we will be using
stairs = 53

# Now loop through our steps
for i in range(5):
    mc.setBlock(x+i-1,y+i,z+3,stairs)
    mc.setBlock(x+i-1,y+i,z+4,stairs)
