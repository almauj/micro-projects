// Smart Task Manager Logic

const tasks = [] // incomplete array (list in python) 
const completeTasks = [] // complete task array
let task

// display tasks on html document
if (tasks.length > 0){
    console.log("there are items in the list")
}
else {
    document.getElementById("noTodo").innerHTML("There are no incomplete tasks.") 
}

if (completeTasks.length = 0){
    document.getElementById("container3").innerHTML(<h4>There are no completed tasks.</h4>)
}
else {
    console.log("there are items in the list")
}

// add task to list
document.getElementById("addTask").onclick = function() {
    task = document.getElementById("writeTask").value;
    console.log(task)
    // tasks.push(task)
}


