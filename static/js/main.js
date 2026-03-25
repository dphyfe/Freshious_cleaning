/* Freshious Cleaning — Main JS */

document.addEventListener('DOMContentLoaded', () => {

    // --- Navbar scroll effect ---
    const nav = document.getElementById('mainNav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 60) {
                nav.classList.add('shadow');
                nav.style.paddingTop = '.4rem';
                nav.style.paddingBottom = '.4rem';
            } else {
                nav.classList.remove('shadow');
                nav.style.paddingTop = '.75rem';
                nav.style.paddingBottom = '.75rem';
            }
        });
    }

    // --- Animate on scroll (simple IntersectionObserver) ---
    const animEls = document.querySelectorAll('.hover-lift, .service-card, .team-card, .addon-card');
    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.style.opacity = '1';
                    e.target.style.transform = 'translateY(0)';
                    io.unobserve(e.target);
                }
            });
        }, { threshold: 0.12 });

        animEls.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(24px)';
            el.style.transition = 'opacity .5s ease, transform .5s ease';
            io.observe(el);
        });
    }

    // --- Set minimum date on contact form date input ---
    const dateInput = document.querySelector('input[name="preferred_date"]');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

});
