(() => {
    // Future categories opt in with data-project-category="Category name".
    // Three or fewer cards remain a grid; larger categories use this carousel.
    document.querySelectorAll('[data-project-category]').forEach((track, index) => {
        if (track.children.length <= 3 || track.classList.contains('carousel-track')) return;
        const region = document.createElement('div');
        region.className = 'project-carousel';
        region.setAttribute('role', 'region');
        region.setAttribute('aria-roledescription', 'carousel');
        region.setAttribute('aria-label', track.dataset.projectCategory);
        track.before(region);
        region.append(track);
        track.classList.add('carousel-track');
        track.id ||= `category-projects-${index}`;
        const controls = document.createElement('div');
        controls.className = 'carousel-controls';
        controls.hidden = true;
        controls.innerHTML = `<button type="button" data-carousel="previous" aria-label="Previous projects" aria-controls="${track.id}"><svg class="ui-arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 12H4M10 6l-6 6 6 6"/></svg></button><span class="carousel-status" aria-live="off"></span><button type="button" data-carousel="next" aria-label="Next projects" aria-controls="${track.id}"><svg class="ui-arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h16M14 6l6 6-6 6"/></svg></button>`;
        region.prepend(controls);
    });

    document.querySelectorAll('.project-carousel').forEach(region => {
        const track = region.querySelector('.carousel-track');
        const cards = [...track.children];
        const controls = region.querySelector('.carousel-controls');
        const status = controls.querySelector('.carousel-status');
        const nav = document.querySelector('nav');
        const motion = matchMedia('(prefers-reduced-motion: reduce)');
        let visible = false, held = false, moving = false;
        let visibleSince = 0, pauseUntil = 0, nextRotation = 0, timer, motionTimer;
        const step = () => cards[1].offsetLeft - cards[0].offsetLeft;
        const count = () => Math.max(1, Math.round((track.clientWidth + 30) / step()));
        const position = () => Math.round(track.scrollLeft / step());
        function label() {
            status.textContent = `${position() + 1}–${Math.min(cards.length, position() + count())} of ${cards.length}`;
        }
        function schedule() {
            clearTimeout(timer);
            if (!visible || held || motion.matches || document.hidden) return;
            const due = Math.max(visibleSince + 3000, pauseUntil, nextRotation);
            timer = setTimeout(() => {
                status.setAttribute('aria-live', 'off');
                move(1);
                nextRotation = Date.now() + 4000;
                schedule();
            }, Math.max(0, due - Date.now()));
        }
        function pause(cancelMotion = false) {
            pauseUntil = Date.now() + 10000;
            nextRotation = 0;
            status.setAttribute('aria-live', 'polite');
            if (cancelMotion && moving) {
                moving = false;
                clearTimeout(motionTimer);
                track.scrollTo({ left: track.scrollLeft, behavior: 'instant' });
            }
            schedule();
        }
        function move(direction) {
            const max = Math.max(0, cards.length - count());
            let next = position() + direction;
            if (next > max) next = 0;
            if (next < 0) next = max;
            moving = true;
            clearTimeout(motionTimer);
            track.scrollTo({ left: next * step(), behavior: motion.matches ? 'instant' : 'smooth' });
            // Programmatic scroll events must not be mistaken for user input.
            motionTimer = setTimeout(() => { moving = false; }, 1000);
        }
        function updateVisibility() {
            const rect = track.getBoundingClientRect();
            const navBottom = nav && getComputedStyle(nav).visibility !== 'hidden'
                ? Math.max(0, nav.getBoundingClientRect().bottom) : 0;
            const shown = Math.max(0, Math.min(innerHeight, rect.bottom) - Math.max(navBottom, rect.top));
            const nextVisible = !document.hidden && rect.height > 0 && shown >= rect.height / 2 && rect.right > 0 && rect.left < innerWidth;
            if (nextVisible !== visible) {
                visible = nextVisible;
                if (visible) visibleSince = Date.now();
                schedule();
            }
            label();
        }
        controls.querySelector('[data-carousel="previous"]').addEventListener('click', () => { pause(); move(-1); });
        controls.querySelector('[data-carousel="next"]').addEventListener('click', () => { pause(); move(1); });
        region.addEventListener('pointerdown', () => { held = true; pause(true); });
        const release = () => { if (held) { held = false; pause(); } };
        window.addEventListener('pointerup', release);
        window.addEventListener('pointercancel', release);
        window.addEventListener('blur', release);
        region.addEventListener('wheel', () => pause(true), { passive: true });
        region.addEventListener('keydown', () => pause(true));
        region.addEventListener('click', () => pause());
        region.addEventListener('focusin', () => pause());
        track.addEventListener('scroll', () => {
            label();
            if (!moving) pause();
        }, { passive: true });
        track.addEventListener('scrollend', () => { moving = false; clearTimeout(motionTimer); });
        window.addEventListener('scroll', updateVisibility, { passive: true });
        window.addEventListener('resize', updateVisibility);
        document.addEventListener('visibilitychange', () => { updateVisibility(); schedule(); });
        motion.addEventListener('change', schedule);
        const resize = new ResizeObserver(updateVisibility);
        resize.observe(track);
        if (nav) resize.observe(nav);
        controls.hidden = false;
        updateVisibility();
    });
})();
