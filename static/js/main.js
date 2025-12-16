// Job Portal JavaScript Functions

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            showError(input, 'This field is required');
            isValid = false;
        } else {
            clearError(input);
        }
    });

    return isValid;
}

function showError(input, message) {
    clearError(input);
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.style.color = '#dc3545';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    errorDiv.textContent = message;
    input.parentNode.appendChild(errorDiv);
    input.style.borderColor = '#dc3545';
}

function clearError(input) {
    const errorMessage = input.parentNode.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
    input.style.borderColor = '#e1e5e9';
}

// Search functionality
function initializeSearch() {
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const query = document.getElementById('searchQuery').value.trim();
            const location = document.getElementById('searchLocation').value.trim();
            
            if (!query && !location) {
                e.preventDefault();
                alert('Please enter a search term or location');
            }
        });
    }
}

// Modal functionality
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

// Job application confirmation
function confirmApplication(jobTitle) {
    return confirm(`Are you sure you want to apply for ${jobTitle}?`);
}

// Auto-hide alerts
function autoHideAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
    autoHideAlerts();
    
    // Close modals when clicking outside
    window.addEventListener('click', function(event) {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });
    
    // Form validation on submit
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const formId = form.id;
            if (formId && !validateForm(formId)) {
                e.preventDefault();
            }
        });
    });
});

// Smooth scrolling for anchor links
function smoothScroll(target) {
    document.querySelector(target).scrollIntoView({
        behavior: 'smooth'
    });
}

// Loading animation
function showLoading() {
    const loader = document.createElement('div');
    loader.id = 'loader';
    loader.innerHTML = '<div class="spinner"></div>';
    loader.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    `;
    document.body.appendChild(loader);
}

function hideLoading() {
    const loader = document.getElementById('loader');
    if (loader) {
        loader.remove();
    }
}