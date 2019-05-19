#Blender render farm

This is a Blender render farm manager... in its early stages. At the moment it takes a blender file to render a still image split between two computers. The filename, the <userid>@<ipaddress> of each rendering node (only two at the moment), the number of samples desired, and the number of strips to divide the image are specified on a web form and on submit, child processes are spawned and blender is invoked headless, and in the background, and the stream of outputs from the two computers are sent to two text areas on the form. 

next steps: 

1. make it easy to add/remove computers to/from the pool.
2. cleanup and a lot of organization work
3. remove excess code and files

requires Nodejs, express, and socket.io