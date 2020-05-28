var superficie=document.getElementById("superficie").getContext("2d");

var chart = new Chart(superficie, {
    type:"bar",
    data:{
      labels:["Natural", "Sintético"],
      datasets:[
        {
          label:"Tipo de Superficie",
          backgroundColor:"rgb(71,160,245)",
          data:[36,0]
        }
      ]
    }
});

var lesion=document.getElementById("lesion").getContext("2d");

var chart = new Chart(lesion, {
    type:"bar",
    data:{
      labels:["Tobillo", "Pie", "Cadera", "Rodilla", "Dedos (Pies)"],
      datasets:[
        {
          label:"Parte del Cuerpo",
          backgroundColor:"rgb(246,101,101)",
          data:[14,4, 0, 18, 0]
        }
      ]
    }
});

var jugada=document.getElementById("jugada").getContext("2d");

var chart = new Chart(jugada, {
    type:"bar",
    data:{
      labels:["PI", "PINR", "PIR", "Pase", "PD", "PDNR", "PDR", "Corrida"],
      datasets:[
        {
          label:"Tipo de Jugada",
          backgroundColor:"rgb(129,252,116)",
          data:[3, 0, 0, 15, 6, 0, 1, 11]
        }
      ]
    }
});

var posicion=document.getElementById("posicion").getContext("2d");

var chart = new Chart(posicion, {
    type:"bar",
    data:{
      labels:["DB", "DL", "LB", "OL", "RB", "TE", "WR"],
      datasets:[
        {
          label:"Tipo de Superficie",
          backgroundColor:"rgb(245,181,62)",
          data:[7, 4, 11, 4, 2, 1, 7]
        }
      ]
    }
});

var superficie2=document.getElementById("superficie2").getContext("2d");

var chart = new Chart(superficie2, {
    type:"bar",
    data:{
      labels:["Natural", "Sintético"],
      datasets:[
        {
          label:"Tipo de Superficie",
          backgroundColor:"rgb(71,160,245)",
          data:[0, 41]
        }
      ]
    }
});

var lesion2=document.getElementById("lesion2").getContext("2d");

var chart = new Chart(lesion2, {
    type:"bar",
    data:{
      labels:["Tobillo", "Pie", "Cadera", "Rodilla", "Dedos (Pies)"],
      datasets:[
        {
          label:"Parte del Cuerpo",
          backgroundColor:"rgb(246,101,101)",
          data:[21, 2, 0, 18, 0]
        }
      ]
    }
});

var jugada2=document.getElementById("jugada2").getContext("2d");

var chart = new Chart(jugada2, {
    type:"bar",
    data:{
      labels:["PI", "PINR", "PIR", "Pase", "PD", "PDNR", "PDR", "Corrida"],
      datasets:[
        {
          label:"Tipo de Jugada",
          backgroundColor:"rgb(129,252,116)",
          data:[4, 1, 1, 17, 3, 1, 2, 12]
        }
      ]
    }
});

var posicion2=document.getElementById("posicion2").getContext("2d");

var chart = new Chart(posicion2, {
    type:"bar",
    data:{
      labels:["DB", "DL", "LB", "OL", "RB", "TE", "WR"],
      datasets:[
        {
          label:"Tipo de Superficie",
          backgroundColor:"rgb(245,181,62)",
          data:[12, 3, 10, 2, 4, 1, 9]
        }
      ]
    }
});
