(() => {
    const blueprint = document.querySelector('.argo-blueprint');
    if (!blueprint) return;
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    let navigating = false;
    let settleTimer;

    function afterViewportSettles(callback) {
        clearTimeout(settleTimer);
        let finished = false;

        function finish() {
            if (finished) return;
            finished = true;
            clearTimeout(settleTimer);
            window.removeEventListener('scroll', restart);
            callback();
        }

        function restart() {
            clearTimeout(settleTimer);
            settleTimer = setTimeout(finish, 100);
        }

        window.addEventListener('scroll', restart, { passive: true });
        requestAnimationFrame(restart);
    }

    function clear() {
        blueprint.classList.remove('is-highlighting-recovery', 'is-highlighting-aerocover', 'is-schematic-focus');
        document.documentElement.classList.remove('is-page-leaving');
        document.querySelectorAll('.project-card.is-opening-project').forEach(card => card.classList.remove('is-opening-project'));
    }

    document.querySelectorAll('a[data-schematic-part]').forEach(link => {
        link.addEventListener('click', event => {
            if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || motion.matches) return;
            event.preventDefault();
            if (navigating) return;
            navigating = true;
            try {
                sessionStorage.setItem('portfolio:internal-navigation', 'true');
                sessionStorage.setItem('portfolio:schematic-complete', 'true');
                if (matchMedia('(max-width: 650px)').matches) {
                    sessionStorage.setItem('portfolio:mobile-return-to-hero', 'true');
                }
            } catch {
                // Navigation and highlighting still work when storage is unavailable.
            }

            const part = link.dataset.schematicPart;
            clear();
            link.classList.add('is-opening-project');

            const navHeight = document.querySelector('.site-nav')?.getBoundingClientRect().height || 0;
            const blueprintTop = blueprint.getBoundingClientRect().top + scrollY - navHeight - 18;
            afterViewportSettles(() => {
                blueprint.classList.add('is-schematic-focus', `is-highlighting-${part}`);

                const focusDelay = matchMedia('(max-width: 650px)').matches ? 1100 : 950;
                setTimeout(() => {
                    document.documentElement.classList.add('is-page-leaving');
                    setTimeout(() => window.location.assign(link.href), 240);
                }, focusDelay);
            });
            window.scrollTo({ top: Math.max(0, blueprintTop), behavior: 'smooth' });
        });
    });

    window.addEventListener('pageshow', () => {
        navigating = false;
        clearTimeout(settleTimer);
        clear();
    });
})();
