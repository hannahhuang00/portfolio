var wordsList = [];
var wordsLength = wordsList.length;

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var pw = document.getElementById('pw').value;
  for (var i = 0; i < wordsList.length; i++) {
    var word = wordsList[i];
    if (pw.includes(word) && word != ""){
          alert("Your password is weak");
    } else {

    }
  }
}
            //var passwordValue = wordsList.indexOf('pw');
  //    return "The word " + wordsList + " was detected in your password.";

      //alert("Your password is weak.");
      //return true;
//  } else {
  //    return "Your password is strong.";
      //return false;
    //}
  //}
//}

//function printResults() {
//  if (checkPassword == true) {
  //    document.getElementById("results").innerHTML = "Your password is weak."
  //} else {
    //  document.getElementById("results").innerHTML = "Your password is strong."
  //}
//}
