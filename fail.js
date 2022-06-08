const randColor = () =>  {return "#" + Math.floor(Math.random()*16777215).toString(16).padStart(6, '0').toUpperCase();};
let x = randColor()
document.getElementById("yes").innerHTML=x
document.getElementById("yes").style.color=x