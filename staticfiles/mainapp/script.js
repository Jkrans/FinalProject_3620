// add class to element
function addClassToNav(className, element) {
    var e = document.querySelector(element);
    e.classList.add(className);
  }

// change alt text of an element
function changeAltText(element, altText) {
    var e = document.querySelector(element);
    e.setAttribute("alt", altText);
}

// Christmas countdown function
function updateCountdown() {
    var now = new Date();
    var christmas = new Date(now.getFullYear(), 11, 25);
    var difference = christmas - now;

    var days = Math.floor(difference / (1000 * 60 * 60 * 24));
    var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((difference % (1000 * 60)) / 1000);

    document.getElementById("days").innerHTML = days;
    document.getElementById("hours").innerHTML = hours;
    document.getElementById("minutes").innerHTML = minutes;
    document.getElementById("seconds").innerHTML = seconds;
  }

  // update every second
  setInterval(updateCountdown, 1000);

  function letterColorChange(TextInput){
    var brandText = document.getElementById('navbar-brand-text');
    var letters = TextInput.split('');
    
    letters.forEach(function(letter) {
      var letterSpan = document.createElement('span');
      letterSpan.innerText = letter;
    
      letterSpan.addEventListener('mouseover', function() {
        letterSpan.style.color = 'red';
        letterSpan.style.transition = 'none';
      });
    
      letterSpan.addEventListener('mouseout', function() {
        letterSpan.style.color = '';
        letterSpan.style.transition = '3s ease-out';
      });
      
      brandText.appendChild(letterSpan);
    });}
  
  





























