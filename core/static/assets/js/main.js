const input = document.querySelector(".ingreso_datos");
const button = document.querySelector("button");
const resultado = document.querySelector(".reflejar_res");


button.addEventListener('click', (e) =>  {
    e.preventDefault();
    traerDatos(input.value);
})

function traerDatos(cp){
    fetch(`https://apis.forcsec.com/api/codigos-postales/20220728-d261a2762f2e367c/${cp}`)
        .then((res) => res.json())
        .then((data) => {
            crearResultado(data);
        });

}



function crearResultado(cp){

    const h3 = document.createElement('h3');
    h3.textContent = cp.data.municipio


    
    var muni = cp.data.municipio
    var estado = cp.data.estado
    var mexico = "Mexico"
    var codigoPostal = input.value
    var nombre = cp.data.asentamientos.nombre
    document.getElementById("pais").value=mexico;
    document.getElementById("municipio").value=muni;
    document.getElementById("estado").value=estado;
    document.getElementById("localidad").value=nombre;
    document.getElementById("codigoPostal").value=codigoPostal;

}

