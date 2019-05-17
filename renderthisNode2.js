
// this file starts a render child process spawn.
// it takes the workerNode ID in the form <user>@<ip_address>, the blender filename, the number of samples desired, 
// and the script name and starts (at the moment in my studio) my laptop doing the LH (lefthand side of the image)
// and my ubuntu machine doing the Node2
// both outputs are to stdout at the moment
// next steps:
// send the script and filenames from the webform and call this function
// then open a textarea/window on the web page and send the output there.




const {spawn} = require('child_process');

function renderthisNode2(ScriptName, Filename, Samples, WorkerNode2, minX, maxX) {

console.log('here: ',ScriptName, Filename, Samples, WorkerNode2);

const childProcessNode2 = spawn(ScriptName, [Filename, Samples, WorkerNode2, minX, maxX]);

    childProcessNode2.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });


    childProcessNode2.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`);
    });
  

    childProcessNode2.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

  
  console.log('### DONE');
}


module.exports= renderthisNode2;




