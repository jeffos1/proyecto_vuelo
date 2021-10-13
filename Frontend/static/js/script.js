export function textDark(elements) {
    for (const key of elements) {
        key.classList.add('text-dark');
    }

}



export function class_to_active_link(links, myClass) {
    // body
    var path = window.location.pathname;
    var page = path.split("/")[1];

    let nofound = false;
    for (const link of links) {
        let current_link = link.href.split("/").pop();

        if (current_link == page || current_link.slice(0, -1) == page) {

            link.classList.add('active');

            nofound = true;
        }

    }



}

export function addCloseToNav() {
    // body

    if (page == "dashboard_home" || page == "dashboard_aviones" || page == "dashboard_pilotos" || page == "dashboard_usuarios" || page == "dashboard_vuelos" || page == "dashboard" || page == "mis_reservas") {

        let nav_container = document.querySelector('#nav_container');
        let cerrar = document.createElement('a');
        let cerrar_text = document.createTextNode("Salir");
        cerrar.appendChild(cerrar_text);
        cerrar.classList.add('nav-link');
        cerrar.classList.add('mr-2');
        cerrar.setAttribute('href', '../home')

        nav_container.appendChild(cerrar);
    }
}
