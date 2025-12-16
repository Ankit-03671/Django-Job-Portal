// Home page interactive features

// Smooth scrolling for navigation
document.addEventListener('DOMContentLoaded', function() {
    // Add scroll effect to navigation
    window.addEventListener('scroll', function() {
        const nav = document.querySelector('nav');
        if (window.scrollY > 100) {
            nav.style.background = 'rgba(0,0,0,0.95)';
            nav.style.backdropFilter = 'blur(10px)';
        } else {
            nav.style.background = 'rgba(0,0,0,0.9)';
        }
    });
    
    // Typing effect for hero title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        let i = 0;
        
        function typeWriter() {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        setTimeout(typeWriter, 500);
    }
    
    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const heroSection = document.querySelector('.hero-section');
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.5;
        
        if (heroSection) {
            heroSection.style.transform = `translateY(${rate}px)`;
        }
    });
    
    // Add hover effects to job cards
    const jobCards = document.querySelectorAll('.job-card-mini');
    jobCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Search suggestions (mock data)
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        const suggestions = [
            'Software Developer', 'Data Scientist', 'Product Manager',
            'UI/UX Designer', 'Marketing Manager', 'Sales Executive'
        ];
        
        searchInput.addEventListener('focus', function() {
            // Could implement autocomplete here
            this.placeholder = suggestions[Math.floor(Math.random() * suggestions.length)];
        });
    }
    
    // Add loading animation to CTA buttons
    const ctaButtons = document.querySelectorAll('.btn-primary, .btn-secondary, .btn-cta');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
});

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255,255,255,0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .btn-primary, .btn-secondary, .btn-cta {
        position: relative;
        overflow: hidden;
    }
`;
document.head.appendChild(style);