const redHeaderDIV = document.getElementById('red_header');

redHeaderDIV.addEventListener('click', function() {
    const headerElements = document.getElementsByTagName('header')[0];
    headerElements.style.color = '#FF0000';
});
