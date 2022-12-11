
document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialisation
    var datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // select initialisation
    var selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // collapsible task initilisation
    var collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse);
});