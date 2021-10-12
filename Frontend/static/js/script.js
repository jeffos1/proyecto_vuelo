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


        //alert(current_link)
        if (current_link == page || current_link.slice(0, -1) == page) {
            // alert(page)
            // alert(link)
            // alert(current_link.slice(0, -1))
            // alert(current_link);
            // alert(current_link.slice(0, -1))
            link.classList.add('active');

            nofound = true;
        }

    }

    // if (!nofound) {

    //     links[0].classList.add('active');
    // }


}

export function addCloseToNav() {
    // body

    if (page == "dashboard_home" || page == "dashboard") {

        let nav_container = document.querySelector('#nav_container');
        let cerrar = document.createElement('a');
        let cerrar_text = document.createTextNode("Cerrar");
        cerrar.appendChild(cerrar_text);
        cerrar.classList.add('nav-link');
        cerrar.classList.add('mr-2');
        cerrar.setAttribute('href', '../home')

        nav_container.appendChild(cerrar);
    }
}
