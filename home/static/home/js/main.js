document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('homeButton');
    button.addEventListener('click', function () {
        alert(gettext('Button clicked!'));
    });
});