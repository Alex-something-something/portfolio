(() => {
    const hero = document.querySelector('.hero');
    const nav = document.querySelector('.site-nav');
    const replay = document.querySelector('.launch-replay');
    const blueprint = document.querySelector('.argo-blueprint');
    const drawingReplay = document.querySelector('.argo-replay');
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    if (!hero || !replay || !blueprint || !drawingReplay) return;
    let timeout;
    function hideNavigation() {
        if (!nav) return;
        nav.classList.add('is-awaiting-hero');
        nav.inert = true;
    }
    function revealNavigation() {
        if (!nav) return;
        nav.classList.remove('is-awaiting-hero');
        nav.inert = false;
    }
    function finish() {
        clearTimeout(timeout);
        hero.classList.remove('is-launching');
        revealNavigation();
    }
    function play() {
        if (motion.matches) return;
        clearTimeout(timeout);
        hero.classList.remove('is-launching');
        hideNavigation();
        void hero.offsetWidth;
        hero.classList.add('is-launching');
        timeout = setTimeout(finish, matchMedia('(max-width: 650px)').matches ? 7100 : 4700);
    }
    function draw() {
        blueprint.classList.remove('is-waiting');
        if (motion.matches) return;
        blueprint.classList.remove('is-drawing');
        void blueprint.offsetWidth;
        blueprint.classList.add('is-drawing');
    }
    replay.addEventListener('click', play);
    hero.addEventListener('keydown', event => { if (event.key === 'Escape') finish(); });
    drawingReplay.addEventListener('click', () => {
        stopBlueprintWatch();
        draw();
    });
    motion.addEventListener('change', () => {
        if (motion.matches) { finish(); blueprint.classList.remove('is-drawing', 'is-waiting'); }
    });
    replay.hidden = false;
    drawingReplay.hidden = false;
    // Reserve the header's space while it is hidden, avoiding layout shifts.
    const initialHero = hero.getBoundingClientRect();
    const visibleHeight = Math.min(initialHero.bottom, innerHeight) - Math.max(initialHero.top, 0);
    if (!motion.matches && visibleHeight / initialHero.height >= .25) hideNavigation();
    function skipOffscreenHero() {
        if (hero.getBoundingClientRect().bottom <= (nav?.getBoundingClientRect().height || 0)) {
            if (hero.classList.contains('is-launching') || nav?.classList.contains('is-awaiting-hero')) finish();
        }
    }
    window.addEventListener('scroll', skipOffscreenHero, { passive: true });
    window.addEventListener('resize', skipOffscreenHero);
    // Each fresh page load gets one launch when the hero enters view.
    // This also handles refreshes that restore a lower scroll position.
    const heroObserver = new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= .25)) {
            play();
            heroObserver.disconnect();
        }
    }, { threshold: .25 });
    heroObserver.observe(hero);
    if (!motion.matches) blueprint.classList.add('is-waiting');
    let blueprintTimer;
    let blueprintObserver;
    let blueprintStarted = false;
    function stopBlueprintWatch() {
        clearTimeout(blueprintTimer);
        blueprintStarted = true;
        blueprintObserver?.disconnect();
    }
    function watchBlueprint() {
        clearTimeout(blueprintTimer);
        blueprintObserver?.disconnect();
        const navHeight = Math.ceil(nav?.getBoundingClientRect().height || 0);
        document.documentElement.style.setProperty('--site-nav-height', `${navHeight}px`);
        if (blueprintStarted || document.hidden) return;
        // Exclude the sticky navigation so it cannot cover part of the box.
        const topInset = Math.ceil(nav?.getBoundingClientRect().height || 0);
        blueprintObserver = new IntersectionObserver(entries => {
            clearTimeout(blueprintTimer);
            if (entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= .999)) {
                blueprintTimer = setTimeout(() => {
                    stopBlueprintWatch();
                    draw();
                }, 300);
            }
        }, { threshold: [0, .999, 1], rootMargin: `-${topInset}px 0px 0px 0px` });
        blueprintObserver.observe(blueprint);
    }
    document.addEventListener('visibilitychange', watchBlueprint);
    window.addEventListener('resize', watchBlueprint);
    if (nav) new ResizeObserver(watchBlueprint).observe(nav);
    watchBlueprint();
})();
