#render_farm
This is a render farm manager... in its early stages.
At the moment it takes a blender file to render a still
image split between two computers. The filename, number of
samples, and the split point between the two halves are specified
on a web form and on submit, child processes are spawned and
blender is invoked headless, and in the background, and  
the stream of outputs from the two computers are sent to two
text areas on the form. 

next steps: 
1. remove the split and hand out narrow strips to
as the current renders are completed. This will eliminate the
need to judge the relative speeds of the worker nodes. 
2. Also, make it easy to add/remove computers to/from the pool.
