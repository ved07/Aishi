function submitForm(){


  var symptoms = document.getElementById('symptoms').value;
  var city = document.getElementById('city').value;
  var insNo = document.getElementById('insNO').value || 0;
  var birthDate = document.getElementById('birthDate').value;
  var lastName = document.getElementById('lastName').value;
  var firstName = document.getElementById('firstName').value;
  var code = firstName + lastName;

  return firebase.firestore().collection('issue').add({
    firstName: firstName,
    lastName: lastName,
    city: city,
    insNo: insNo,
    birthDate: birthDate,
    symptoms: symptoms,
    timestamp: firebase.firestore.FieldValue.serverTimestamp()
  }).catch(function(error){
    console.error('Error writing new message to Firebase Database', error);
  });

  //add symptoms here, maybe redirect to a page with results?
}
