#Blender render farm

This is a Blender render farm manager... in its early stages. At the moment it takes a blender file to render a still image split between two computers. The filename, the username@IPaddress of each rendering node (only two at the moment), the number of samples desired, and the number of strips to divide the image are specified on a web form and on submit, child processes are spawned and blender is invoked headless, and in the background, and the stream of outputs from the two computers are sent to two text areas on the form. When a worker node finishes a strip it writes the file with the name convention filename+minX+maxX+minY+maxY.png. then it takes the next available strip for rendering. At the moment the division is in vertical strips so minY/maxY are 0/1.

next steps: 

1. make it easy to add/remove computers to/from the pool.
2. cleanup and a lot of organization work
3. remove excess code and files

requires Nodejs, express, and socket.io