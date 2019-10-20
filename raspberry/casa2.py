# Connect to MineCraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Get our current position
x, y, z = mc.player.getPos()

# define our blocks we will be using
stone = 1
brick = 45
air = 0
wood_plank = 5
glass_pane = 102
stairs = 53
fence = 85
roof = 67
roof_flat = 4

# Now we build our house!
# first clear the area
mc.setBlocks(x-10, y, z-10, x+10, y+15, z+10, air)
# now lay a foundation
mc.setBlocks(x-7, y-1, z-7, x+7, y-3, z+7, stone)
# add add a fence around our plot
mc.setBlocks(x-7, y, z-7, x+7, y, z-7, fence)
mc.setBlocks(x-7, y, z-7, x-7, y, z+7, fence)
mc.setBlocks(x+7, y, z+7, x+7, y, z-7, fence)
mc.setBlocks(x+7, y, z+7, x-7, y, z+7, fence)
# now make our house block
mc.setBlocks(x-5, y, z-5, x+5, y+9, z+5, 41)
# and hollow it out
mc.setBlocks(x-4, y, z-4, x+4, y+8, z+4, air)
# make the ground floor
mc.setBlocks(x-4, y-1, z-4, x+4, y-1, z+4, wood_plank)
# make the first floor
mc.setBlocks(x-4, y+4, z-4, x+4, y+4, z+4, wood_plank)
# make the ceiling
mc.setBlocks(x-4, y+9, z-4, x+4, y+9, z+4, wood_plank)
# make the door - 64 is a wood door, id 0 is the bootom, id 8 is the top part
mc.setBlock(x-5, y, z, 64, 0)
mc.setBlock(x-5, y+1, z, 64, 8)
# Add some windows
mc.setBlocks(x-5,y+1,z-2,x-5,y+2,z-3,glass_pane)
mc.setBlocks(x-5,y+1,z+2,x-5,y+2,z+3,glass_pane)
mc.setBlocks(x-5,y+6,z-2,x-5,y+7,z-3,glass_pane)
mc.setBlocks(x-5,y+6,z+2,x-5,y+7,z+3,glass_pane)
mc.setBlocks(x+5,y+1,z-2,x+5,y+2,z-3,glass_pane)
mc.setBlocks(x+5,y+1,z+2,x+5,y+2,z+3,glass_pane)
mc.setBlocks(x+5,y+6,z-2,x+5,y+7,z-3,glass_pane)
mc.setBlocks(x+5,y+6,z+2,x+5,y+7,z+3,glass_pane)
# Now add the stairs
# Create a hole in the floor first
mc.setBlocks(x+3,y+4,z+4,x,y+4,z+3,air)
# Now loop through our steps
for i in range(5):
    mc.setBlock(x+i-1,y+i,z+3,stairs)
    mc.setBlock(x+i-1,y+i,z+4,stairs)
# add some banistairs too
mc.setBlocks(x-1,y+5,z+4,x-1,y+5,z+2,fence)
mc.setBlocks(x-1,y+5,z+2,x+2,y+5,z+2,fence)
# Now lets add a roof
# First the pitches
for i in range(5):
    mc.setBlocks(x-5+i, y+10+i, z-5, x-5+i, y+10+i, z+5, roof)
    mc.setBlocks(x+5-i, y+10+i, z-5, x+5-i, y+10+i, z+5, roof, 1)
# Now the top
mc.setBlocks(x, y+14, z-5, x, y+14, z+5, roof_flat)
# Now the brick sides
for i in range(4):
    mc.setBlocks(x-1-i, y+13-i, z-5, x+1+i, y+13-i, z-5, brick)
for i in range(4):
    mc.setBlocks(x-1-i, y+13-i, z+5, x+1+i, y+13-i, z+5, brick)
