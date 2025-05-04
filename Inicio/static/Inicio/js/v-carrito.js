var item1 = document.getElementById("item1");
var item2 = document.getElementById("item2");
var item3 = document.getElementById("item3");
var iteminv = document.getElementById("iteminvisible");
var iteminv2 = document.getElementById("iteminvisible2");
var iteminv3 = document.getElementById("iteminvisible3");

if (iteminv) iteminv.style.display = 'none';
if (iteminv2) iteminv2.style.display = 'none';
if (iteminv3) iteminv3.style.display = 'none';

function eliminar() {
    if (item1) item1.style.display = 'none';
    if (iteminv) iteminv.style.display = '';
}

function eliminar2() {
    if (item2) item2.style.display = 'none';
    if (iteminv2) iteminv2.style.display = '';
}

function eliminar3() {
    if (item3) item3.style.display = 'none';
    if (iteminv3) iteminv3.style.display = '';
}