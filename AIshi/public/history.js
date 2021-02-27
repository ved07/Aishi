function displayMessage(firstName, lastName, time, symptom){

  var container = document.getElementById('container');
  var newDiv = document.createElement('div');
  newDiv.classList.add('symptomDiv');
  var name = document.createElement('p');
  name.innerText = firstName + " " + lastName;
  var br = document.createElement('br');
  var br2 = document.createElement('br');
  var data = document.createElement('i');
  data.innerHTML = time.toDate();
  var symptoms = document.createElement('p');
  symptoms.innerText = symptom;
  var br3 = document.createElement('br');
  var newButton = document.createElement('button');
  newButton.classList.add('callBtn');
  newButton.innerText = "Call a doctor";
  newButton.onclick = "../click";

  newDiv.appendChild(name);
  newDiv.appendChild(br);
  newDiv.appendChild(data);
  newDiv.appendChild(br2)
  newDiv.appendChild(symptoms);
  newDiv.appendChild(br3);
  newDiv.appendChild(newButton);
  container.appendChild(newDiv);


}

function loadHistory() {
  var query = firebase.firestore().collection('issue').orderBy('timestamp', 'desc').limit(12);

  query.onSnapshot(function(snapshot){
    snapshot.docChanges().forEach(function(change){
      var message = change.doc.data();
      displayMessage(message.firstName, message.lastName, message.timestamp, message.symptoms);
    });
  });
}

loadHistory();
