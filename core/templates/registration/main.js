const input = document.querySelector(".ingreso_datos");
const button = document.querySelector("button");
const resultado = document.querySelector(".reflejar_res");



function traerDatos(){
    fetch("https://apis.forcsec.com/api/codigos-postales/20220728-d261a2762f2e367c/75510")
        .then((res) => res.json())
        .then((data) => {
            crearResultado(data);
        });

}



function crearResultado(cp){

    const h3 = document.createElement('h3');
    h3.textContent = cp.data.municipio

    const div = document.createElement('div');
    div.appendChild(h3);


    resultado.appendChild(div);

}

traerDatos();