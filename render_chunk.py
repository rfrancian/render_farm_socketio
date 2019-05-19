# This file is called by blenderScript_LH and blenderScript_RH
# 
#   all nodes have NAS mounted to /Volumes/blenderFiles 
#   as follows:
#   sudo mount -t nfs 192.168.86.23:/volume1/blender /Volumes/blenderFiles
#
#
#
#  run like:
#   
#  sshpass -p <password> ssh <node address> < path to blender > -b < blend file > -P < python file >  --  min_x  max_x  min_y  max_y  samples
#  -b run in background
#  -P python script
#   --   space before and after --  separates arguments from command line
#
#
# commands for render scripts. 
#  render RH side on ubuntu 192.168.86.36
#  sshpass -p YngWtsfAIWr517! ssh rsf@192.168.86.36 /snap/blender/20/blender -b /Volumes/blenderFiles/argvTestStrip.blend -P /Volumes/blenderFiles/render_chunk.py -- 0.5 1.0 0.0 1.0 256
#
#  render LH side on MacOS  192.168.86.20
#  sshpass -p zazen ssh robertfrancian@192.168.86.20 /Applications/Blender/blender.app/Contents/MacOS/blender -b /Volumes/blenderFiles/argvTestStrip.blend -P /Volumes/blenderFiles/render_chunk.py -- 0.0 0.5 0.0 1.0 256
#
#  the following line is from ./blenderScript_LH  the script accepts two args  $1 = blend filename  $2 = samples
# sshpass -p zazen ssh robertfrancian@192.168.86.20 /Applications/Blender/blender.app/Contents/MacOS/blender -b $1 -P /Volumes/blenderFiles/render_chunk.py -- 0.0 0.5 0.0 1.0 $2
#
#  the following line is from ./blenderScript_RH  the script accepts two args  $1 = blend filename  $2 = samples
# sshpass -p YngWtsfAIWr517! ssh rsf@192.168.86.36 /snap/blender/20/blender -b $1 -P /Volumes/blenderFiles/render_chunk.py -- 0.5 1.0 0.0 1.0 $2



import bpy
import sys
import os

# parse command line arguments

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"



#set render attributes

xres = 2048
yres = 4096
respercent = 100
seed = 0
samples = int(argv[4])

# set seed and samples
#bpy.data.scenes["Scene"].cycles.seed= seed
bpy.data.scenes["Scene"].cycles.samples= samples


# set caustics
#bpy.data.scenes["Scene"].cycles.caustics_reflective = False
#bpy.data.scenes["Scene"].cycles.caustics_refractive = False

# set resolution and %
#bpy.data.scenes["Scene"].render.resolution_x= xres
#bpy.data.scenes["Scene"].render.resolution_y= yres
#bpy.data.scenes["Scene"].render.resolution_percentage= respercent

#set frame start and stop
bpy.data.scenes["Scene"].frame_start=1
bpy.data.scenes["Scene"].frame_end=1

# set metadata info
bpy.data.scenes['Scene'].render.use_stamp=True
#bpy.data.scenes['Scene'].render.use_stamp_note=True
#bpy.data.scenes['Scene'].render.stamp_note_text= ' strips samples 256, caustics off '


#set render border
bpy.data.scenes["Scene"].render.use_border = True
bpy.data.scenes["Scene"].render.border_min_x = float(argv[0])
bpy.data.scenes["Scene"].render.border_max_x = float(argv[1])
bpy.data.scenes["Scene"].render.border_min_y = float(argv[2])
bpy.data.scenes["Scene"].render.border_max_y = float(argv[3])


# build filename
filename = bpy.path.basename(bpy.data.filepath)
filename = os.path.splitext(filename)[0]
filename = "/Volumes/blenderFiles/output/" + filename + "_" + argv[0] + "_" + argv[1] + "_" + argv[2] + "_" + argv[3]

# set output filename
bpy.data.scenes['Scene'].render.filepath = filename


# redirect output to log file
#logfile = 'blender_render.log'
#open(logfile, 'a').close()
#old = os.dup(1)
#sys.stdout.flush()
#os.close(1)
#os.open(logfile, os.O_WRONLY)


# render
bpy.ops.render.render( write_still=True)

filename = filename + ".png"
os.chmod(filename, 0o777)

# disable output redirection
#os.close(1)
#os.dup(old)
#os.close(old)




