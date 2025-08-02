// El Error Ocurre Porque El Navegador Utiliza El Atributo Integrity Para Verificar La Integridad Del Recurso Descargado (En Este Caso, El Fichero Css). Si El Hash Definido En Integrity No Coincide Con El Contenido Del Recurso Real (Es Decir, El Fichero Css En La Url Proporcionada), El Navegador Bloquea La Carga Por Razones De Seguridad.
// El Atributo Integrity Es Útil Cuando Se Cargan Recursos Externos Y Necesitas Asegurarte De Que No Han Sido Modificados. Sin Embargo, Si Cambias Dinámicamente Los Estilos, Puede Ser Más Práctico Eliminar Este Atributo.
// Siempre Prueba Las Url Para Verificar Que Los Recursos Se Cargan Correctamente.

// Asociar Un Valor Personalizado A Un <Link>, Puedes Usar Los Atributos De Datos Personalizados (Data-*), Que Están Diseñados Precisamente Para Este Propósito.
// Lexible: Puedes Agregar Cualquier Información Personalizada Sin Romper La Semántica Html.
// Estándar: Totalmente Compatible Con El Estándar Html5.
// Accesible: Fácil De Manejar Con Javascript Mediante Dataset.

// Conclusión:

// Si Necesitas Almacenar Información Adicional Como Un Value, Utiliza Un Atributo Data-*. Este Enfoque Es Más Adecuado Y Conforme Al Estándar Html Que Intentar Agregar Atributos No Válidos Como Value.

document.addEventListener('DOMContentLoaded', function () {
    const linkElement = document.querySelector('link.Theme');
    const aElement = document.getElementById('get-started')
    
    if (linkElement.dataset.theme === "darkly" && aElement && aElement.classList.contains("btn-light")) {
        aElement.classList.remove("btn-light");
        aElement.classList.add("btn-dark");

    } else if (linkElement.dataset.theme === "flatly" && aElement && aElement.classList.contains("btn-dark")) {
        console.log("Hola")
        aElement.classList.remove("btn-dark");
        console.log(aElement.classList);
        aElement.classList.add("btn-light");
    }

    document.getElementById('btnradio-theme-light').onclick = () => {
        linkElement.removeAttribute("integrity");
        linkElement.integrity = "sha512-qoT4KwnRpAQ9uczPsw7GunsNmhRnYwSlE2KRCUPRQHSkDuLulCtDXuC2P/P6oqr3M5hoGagUG9pgHDPkD2zCDA==";
        linkElement.href = "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/flatly/bootstrap.min.css";
        linkElement.dataset.theme = "flatly";
    };

    document.getElementById('btnradio-theme-dark').onclick = () => {
        linkElement.removeAttribute("integrity");
        linkElement.integrity = "sha512-HDszXqSUU0om4Yj5dZOUNmtwXGWDa5ppESlX98yzbBS+z+3HQ8a/7kcdI1dv+jKq+1V5b01eYurE7+yFjw6Rdg==";
        linkElement.href = "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/darkly/bootstrap.min.css";
        linkElement.dataset.theme = "darkly";
    };
});