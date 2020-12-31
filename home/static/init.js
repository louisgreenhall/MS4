document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {});


    var elems2 = document.querySelectorAll('.sidenav');
    var instances2 = M.Sidenav.init(elems2, {});
});