export function textDark(elements) {
    for (const key of elements) {
        key.classList.add('text-dark');
    }

}

export function class_to_active_link(links, myClass) {
    // body
    var path = window.location.pathname;
    var page = path.split("/").pop();

    let nofound = false;
    for (const link of links) {
        let current_link = link.href.split("/").pop();


        //alert(current_link)
        if (current_link == page) {

            link.classList.add(myClass);
            nofound = true;
        }

    }

    if (!nofound) {

        links[0].classList.add('active');
    }


}