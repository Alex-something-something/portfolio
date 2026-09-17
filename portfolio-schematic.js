(() => {
    const blueprint = document.querySelector('.argo-blueprint');
    if (!blueprint) return;
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    const clear = () => blueprint.classList.remove('is-highlighting-recovery', 'is-highlighting-aerocover');
    window.addEventListener('pageshow', clear);
    let navigating = false;
    document.querySelectorAll('a[data-schematic-part]').forEach(link => {
        link.addEventListener('click', event => {
            if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || motion.matches) return;
            const part = link.dataset.schematicPart;
            const top = document.querySelector('.site-nav')?.getBoundingClientRect().bottom || 0;
            const visiblePart = [...blueprint.querySelectorAll(`[data-part="${part}"]`)].some(element => {
                const rect = element.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0 && rect.bottom > top && rect.top < innerHeight && getComputedStyle(element).visibility !== 'hidden';
            });
            // Never scroll back or delay navigation for a schematic outside the viewport.
            if (!visiblePart) return;
            event.preventDefault();
            if (navigating) return;
            navigating = true;
            clear();
            blueprint.classList.add(`is-highlighting-${part}`);
            setTimeout(() => window.location.assign(link.href), 350);
        });
    });
    window.addEventListener('pageshow', () => { navigating = false; });
})();
