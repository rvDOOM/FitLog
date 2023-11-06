// Document Elements

const addWorkoutElement = document.querySelector('.js-add-workout');
const setFormElement = document.querySelector('.js-workout-display');


// Add new workout

let currWorkouts = [];
addWorkoutElement.addEventListener('click',() => {
  let newWorkoutObject = {
    name: '',
    sets: [],
    "init-setup": true 
  }
  currWorkouts.push(newWorkoutObject);
  displayManager();
})


function displayManager() {

  let workoutDisplayElement = document.querySelector('.js-workout-display');

  workoutDisplayElement.innerHTML = '';
  currWorkouts.forEach((object, index) => {

  if(object['init-setup'] === true) {
    let confirmName = 
      `<button class="js-confirm-workout" onclick="confirm(${index})">confirm</button>`;

    workoutDisplayElement.innerHTML +=
      `<div class="js-workout-display-${index}">
      <div class='workout-number'>Workout ${index + 1}</div>
      <div class='js-workout-name-${index}'>
        <input type="text" placeholder="" class="js-workout-input-${index}">${confirmName}
      </div>
      </div>`;
  } else {
    workoutDisplayElement.innerHTML +=
      `<div class="js-workout-display-${index}">
      <div class='workout-number'>Workout ${index + 1}</div>
      <div class='js-workout-name-${index}'>
        Name: ${object.name}
        <button class='js-edit-button-${index}' onclick="editWorkoutName(${index})">
        Edit
        </button>
      </div>
      <div class='js-set-display-${index}'></div>
      <div class='js-add-new-set-div-${index}'>
        <button class='js-add-new-set-button-${index}' onclick='addNewSet(${index})'>Add Set</button>
      </div>
      </div>`;
      
      let setDisplayElement = document.querySelector('.js-set-display-' + index)
      setDisplayElement.innerHTML = renderSets(index);
  };

  })

  function renderSets(index) {
    let renderedHtml = '';

    currWorkouts[index].sets.forEach((object, idx) => {
    renderedHtml += `<div>Set: ${idx + 1} <input type='text' class='js-set-weight-${index}' placeholder='${object.weight}'>
    <input type='text' class='js-set-reps-${index}' placeholder='${object.reps}'></div>`;

    })


    return renderedHtml;
  }


}

const confirm = (index) => {


  let currInputElement = ".js-workout-input-" + index;
  let currWorkoutNameElement = ".js-workout-name-" + index;
  currInputElement = document.querySelector(currInputElement);
  currWorkoutNameElement = document.querySelector(currWorkoutNameElement);

  let content;
  if (!currInputElement.value && currInputElement.placeholder){
    content = currInputElement.placeholder;
  } else {
    content = currInputElement.value;
  };

  currWorkouts[index].name = content;

  currWorkouts[index]['init-setup'] = false;
  displayManager();
};

const editWorkoutName = (index) => {
  let currWorkoutElement = ".js-workout-name-" + index;
  currWorkoutElement = document.querySelector(currWorkoutElement);
  currWorkoutElement.innerHTML= 
    `Name: <input type='text' class="js-workout-input-${index}" placeholder='${currWorkouts[index].name}'>
    <button onclick='confirm(${index})'>Confirm</button>`;

  console.log("Element " + index + " edit");
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

