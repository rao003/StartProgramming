from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z = mc.player.getPos()

mc.setBlocks(x-2,y-1,z-2,x+2,y-1,z+2,5) #floor
mc.setBlocks(x-2,y,z-2,x-2,y+2,z+2,5) #wall1
mc.setBlocks(x-2,y,z-2,x+2,y+2,z-2,5) #wall2
mc.setBlocks(x+2,y,z-2,x+2,y+2,z+2,5) #wall3
mc.setBlocks(x-2,y,z+2,x+2,y+2,z+2,5) #wall4

mc.setBlocks(x-2,y+3,z-2,x+2,y+3,z+2,17) #roof
