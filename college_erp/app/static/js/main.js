// Main JS file for College ERP

document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Auto hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Add active class to current nav item
    var currentLocation = window.location.pathname;
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(function(link) {
        var linkPath = link.getAttribute('href');
        if (linkPath && currentLocation.includes(linkPath) && linkPath !== '/') {
            link.classList.add('active');
            
            // If it's in a dropdown, also highlight the dropdown parent
            var dropdownParent = link.closest('.dropdown');
            if (dropdownParent) {
                var dropdownToggle = dropdownParent.querySelector('.dropdown-toggle');
                if (dropdownToggle) {
                    dropdownToggle.classList.add('active');
                }
            }
        } else if (linkPath === '/' && currentLocation === '/') {
            link.classList.add('active');
        }
    });
    
    // Print functionality
    var printButtons = document.querySelectorAll('.btn-print');
    printButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            window.print();
        });
    });
    
    // Dynamic date inputs
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        if (!input.value) {
            input.valueAsDate = new Date();
        }
    });
    
    // Form validation for custom elements
    var forms = document.querySelectorAll('.needs-validation');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});