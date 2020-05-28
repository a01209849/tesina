
$(document).ready(function() {
  $('#example').DataTable();
});

$(document).on('click', '.confirm-delete-users', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  var container = document.getElementById("modal_elemina_usuario");
  var text = document.createTextNode("¿Está seguro de eliminar al usuario " + nombre + "?");
  container.removeChild(container.lastChild);
  container.appendChild(text);
});

$(document).on('click', '.confirm-delete-pacientes', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  var container = document.getElementById("modal_elemina_pacientes");
  var text = document.createTextNode("¿Está seguro de eliminar al paciente " + nombre + "?");
  container.removeChild(container.lastChild);
  container.appendChild(text);
});

$(document).on('click', '.confirm-delete-antecedentes-hf', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  var container = document.getElementById("modal_elemina_antecedentes-hf");
  var salto = document.createElement("br");
  var text = document.createTextNode("¿Está seguro de eliminar el antecedente? ");
  var text2 = document.createTextNode(nombre);
  if(container.lastChild == null){
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }else{
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }
});

$(document).on('click', '.confirm-delete-antecedentes-pp', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  var container = document.getElementById("modal_elemina_antecedentes-pp");
  var salto = document.createElement("br");
  var text = document.createTextNode("¿Está seguro de eliminar el antecedente? ");
  var text2 = document.createTextNode(nombre);
  if(container.lastChild == null){
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }else{
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }
});

$(document).on('click', '.confirm-delete-antecedentes-pnp', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  var container = document.getElementById("modal_elemina_antecedentes-pnp");
  var salto = document.createElement("br");
  var text = document.createTextNode("¿Está seguro de eliminar el antecedente? ");
  var text2 = document.createTextNode(nombre);
  if(container.lastChild == null){
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }else{
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }
});

$(document).on('click', '.confirm-delete-lesion', function () {
  $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
  var id = $(this).attr("id");
  var nombre = document.getElementById(id).name;
  console.log(document.getElementById(id).name);
  var container = document.getElementById("modal_elemina_lesion");
  var salto = document.createElement("br");
  var text = document.createTextNode("¿Está seguro de eliminar la lesion del paciente ");
  var text2 = document.createTextNode(nombre);
  if(container.lastChild == null){
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }else{
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.removeChild(container.lastChild);
    container.appendChild(text);
    container.appendChild(salto);
    container.appendChild(text2);
  }
});

$(document).on('click', '#confirmDeleteButtonModal', function () {
  var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
  window.location = $("#".concat(caller)).attr("href");
});

function agrega_antecedentes(){

    var number = document.getElementById("cantidad");
    var i = number.value;
    number.value = parseInt(number.value, 10) + 1;
    var container = document.getElementById("container_antecedentes");

    var row = document.createElement("div");
    row.className = "row";
    row.id = "row-antecedentes";

    //------------------------------- INPUT --------------------------------
    var div1 = document.createElement("div");
    div1.className = "col";
    div1.id = "col-antecedentes";

    var label1 = document.createElement("label");
    label1.for = "Nombre de Antecedente";
    label1.id = "label-font";
    var label1t = document.createTextNode("Nombre de Antecedente");
    label1.appendChild(label1t);
    div1.appendChild(label1);

    // Create an <input> element, set its type and name attributes
    var input = document.createElement("input");
    input.type = "text";
    input.name = "nombre" + i;
    input.className = "form-control";
    input.id = "plantilla-antecedentes";
    input.placeholder = "Nombre del antecedente";
    div1.appendChild(input);

    row.appendChild(div1);

    //-------------------------------- SELECT ------------------------------
    var div2 = document.createElement("div");
    div2.className = "col";
    div2.id = "col-antecedentes";

    var label2 = document.createElement("label");
    label2.for = "Tipo de Antecedente";
    label2.id = "label-font";
    var label2t = document.createTextNode("Tipo de Antecedente");
    label2.appendChild(label2t);
    div2.appendChild(label2);

    var select = document.createElement("select");
    select.name = "tipo" + i;
    select.className = "form-control";
    select.id = "choice-antecedentes";
    select.placeholder = "";

    var z = document.createElement("option");
    z.value = "";
    var zt = document.createTextNode("Elige una opción...");
    z.appendChild(zt);
    select.appendChild(z);

    var a = document.createElement("option");
    a.value = "HF";
    var at = document.createTextNode("Heredofamiliares");
    a.appendChild(at);
    select.appendChild(a);

    var b = document.createElement("option");
    b.value = "PP";
    var bt = document.createTextNode("Personales Patológicos");
    b.appendChild(bt);
    select.appendChild(b);

    var c = document.createElement("option");
    c.value = "NP";
    var ct = document.createTextNode("Personales No Patológicos");
    c.appendChild(ct);
    select.appendChild(c);

    select.options[0].disabled = true;
    div2.appendChild(select);

    row.appendChild(div2);

    //-------------------------- DESCRIPCIÓN ----------------------
    var div3 = document.createElement("div");
    div3.className = "col";
    div3.id = "col-antecedentes";

    var label3 = document.createElement("label");
    label3.for = "Descripción";
    label3.id = "label-font";
    var label3t = document.createTextNode("Descripción");
    label3.appendChild(label3t);
    div3.appendChild(label3);

    var textarea = document.createElement("textarea");
    textarea.name = "descripcion" + i;
    textarea.className = "form-control";
    textarea.rows = "3";
    textarea.id = "plantilla-textarea";
    textarea.placeholder = "Descripción del antecedente";
    div3.appendChild(textarea);

    row.appendChild(div3);

    container.appendChild(row);
    container.appendChild(document.createElement("br"));

}

function quitar_antecedentes(){
  var number = document.getElementById("cantidad");
  var container = document.getElementById("container_antecedentes");

  if (parseInt(number.value, 10) > 1) {
    number.value = parseInt(number.value, 10) - 1;
    for(var i = 0; i < 2; i++){
      container.removeChild(container.lastChild);
    }
  }

}
