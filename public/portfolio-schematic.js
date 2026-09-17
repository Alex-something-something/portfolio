(() => {
    const blueprint = document.querySelector('.argo-blueprint');
    if (!blueprint) return;
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    let navigating = false;

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
            } catch {
                // Navigation and highlighting still work when storage is unavailable.
            }

            const part = link.dataset.schematicPart;
            clear();
            link.classList.add('is-opening-project');
            blueprint.classList.add('is-schematic-focus', `is-highlighting-${part}`);

            const navHeight = document.querySelector('.site-nav')?.getBoundingClientRect().height || 0;
            const blueprintTop = blueprint.getBoundingClientRect().top + scrollY - navHeight - 18;
            window.scrollTo({ top: Math.max(0, blueprintTop), behavior: 'smooth' });

            setTimeout(() => {
                document.documentElement.classList.add('is-page-leaving');
                setTimeout(() => window.location.assign(link.href), 240);
            }, 950);
        });
    });

    window.addEventListener('pageshow', () => {
        navigating = false;
        clear();
    });
})();
