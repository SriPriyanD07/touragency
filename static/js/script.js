document.addEventListener('DOMContentLoaded', function(){
    console.log('Welcome to Our Agency ');
    // alert("Hello,explorers"); // Optional: remove alert for better UX

    // Basic Globe.gl 3D globe
    if (window.Globe) {
        Globe()(document.getElementById('globeViz'))
            .width(320)
            .height(320);
    } else {
        console.error('Globe.gl library not loaded.');
    }
});