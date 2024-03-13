document.addEventListener('DOMContentLoaded', function () {
    const modeSwitch = document.getElementById('modeSwitch');
    const modeText = document.getElementById('modeText');

    modeSwitch.addEventListener('change', function () {
        document.body.classList.toggle('dark-mode');
        if (document.body.classList.contains('dark-mode')) {
            modeText.textContent = 'Dark Mode';
            document.querySelector('.mode-switch').classList.add('dark-mode');
        } else {
            modeText.textContent = 'Light Mode';
            document.querySelector('.mode-switch').classList.remove('dark-mode');
        }
    });

    // Check the user's preferred color scheme and set the initial mode
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark-mode');
        modeText.textContent = 'Dark Mode';
        modeSwitch.checked = true;
    }

    // Scroll-triggered fade-in animation for gallery images
    const galleryImages = document.querySelectorAll('.gallery-image');

    function checkVisibility() {
        galleryImages.forEach((image) => {
            const rect = image.getBoundingClientRect();
            const isVisible = (rect.top >= 0) && (rect.bottom <= window.innerHeight);

            if (isVisible) {
                image.classList.add('fade-in');
            } else {
                image.classList.remove('fade-in');
            }
        });
    }

    // Initial check on page load
    checkVisibility();

    // Listen for scroll events
    window.addEventListener('scroll', checkVisibility);
});
