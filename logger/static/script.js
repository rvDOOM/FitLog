// Document Elements

const newWorkoutElement = document.querySelector('.js-add-workout');
const setFormElement = document.querySelector('.js-workout-display');


// Add new workout

let currWorkouts = [];
newWorkoutElement.addEventListener('click',() => {
  let newWorkoutObject = {
    name: '',
    sets: [],
    html: 
    `<div class='workout-number'>Workout ${currWorkouts.length + 1}</div>
    <div class='js-workout-name-${currWorkouts.length}'></div>
    <div class='js-set-display-${currWorkouts.length}'></div>`,
    "init-setup": true,

  }
  currWorkouts.push(newWorkoutObject);
  displayWorkouts();


})

const confirm = (index) => {
  let currInputNum = ".js-workout-input-" + index;
  let currWorkoutName = ".js-workout-name-" + index;
  let currInput = document.querySelector(currInputNum);
  let content;
  currWorkoutName = document.querySelector(currWorkoutName);
  if (!currInput.value && currInput.placeholder){
    content = currInput.placeholder;
  } else {
    content = currInput.value;
  };
  currWorkouts[index].name = content;
  console.log(currWorkouts[index].name);

  let editButton = `<button class='js-edit-button-${index}' onclick="editWorkoutName(${index})">Edit</button>`;

  currWorkoutName.innerHTML = `Name: ${content}` + editButton;

  if(currWorkouts[index]["init-setup"] === true){
    console.log("We in true");
    addNewSet(index);
    currWorkouts[index]["init-setup"] = false;
  };
}

const addNewSet = (index) => {
  let newSet = {
    weight: 0,
    reps: 0
  }
  let currWorkoutDisplayElement = document.querySelector(`.js-set-display-${index}`);
  currWorkouts[index].sets.push(newSet);
  console.log(currWorkouts[index].sets);
  let currSetList = currWorkouts[index].sets;
  let finalHtml = '';

  currSetList.forEach( (element, index) => {
    const setNum = index + 1;
    let addedHtml = `<div>Set: ${setNum} <input type='text' class='js-set-weight-${index}'>
    <input type='text' class='js-set-reps-${index}'></div>`;

    finalHtml += addedHtml;
  });

  currWorkoutDisplayElement.innerHTML = finalHtml;
}

const editWorkoutName = (index) => {
  let currWorkoutElement = ".js-workout-name-" + index;
  currWorkoutElement = document.querySelector(currWorkoutElement);
  currWorkoutElement.innerHTML= 
    `Name: <input type='text' class="js-workout-input-${index}" placeholder='${currWorkouts[index].name}'>
    <button onclick='confirm(${index})'>Confirm</button>`;

  console.log("Element " + index + " edit");
}




const displayWorkouts =  () => {
  setFormElement.innerHTML = '';
  currWorkouts.forEach((object, index) => {

    console.log(index);
    setFormElement.innerHTML += object.html;


    if (currWorkouts[index]["init-setup"]) {
      console.log("Index: " + index + ": We in true 1");
      let workoutInput = `<input type="text" placeholder="" class="js-workout-input-${index}">`;
      let addSetButton = 
        `<button class="js-confirm-workout" onclick="confirm(${index})">confirm</button>`;
      let workoutDisplayElement = document.querySelector(`.js-workout-name-${index}`);

      workoutDisplayElement.innerHTML = workoutInput + addSetButton;

    } else {

      // TODO
      // Need to the logic for workouts that currently exist
      // Currently once Add Workout is pressed display breaks


    }
    console.log(object);
  })
}
