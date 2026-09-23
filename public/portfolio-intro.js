(() => {
    const hero = document.querySelector('.hero');
    const nav = document.querySelector('.site-nav');
    const replay = document.querySelector('.launch-replay');
    const blueprint = document.querySelector('.argo-blueprint');
    const drawingReplay = document.querySelector('.argo-replay');
    const launchStage = hero?.querySelector('.launch-stage');
    const motion = matchMedia('(prefers-reduced-motion: reduce)');
    const mobile = matchMedia('(max-width: 650px)');
    if (!hero || !replay || !blueprint || !drawingReplay) return;
    const introKey = 'portfolio:intro-complete';
    const schematicKey = 'portfolio:schematic-complete';
    function isComplete(key) {
        try { return sessionStorage.getItem(key) === 'true'; }
        catch { return false; }
    }
    function markComplete(key) {
        try { sessionStorage.setItem(key, 'true'); }
        catch { /* Keep the animations functional when storage is unavailable. */ }
    }
    function positionLaunchStage() {
        if (!launchStage) return;
        launchStage.setAttribute('transform', mobile.matches ? 'translate(0 -80)' : 'translate(160 0)');
    }
    positionLaunchStage();
    const introWasCompleted = isComplete(introKey);
    const schematicWasCompleted = isComplete(schematicKey);
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
        markComplete(introKey);
        revealNavigation();
    }
    function play() {
        if (motion.matches) return;
        clearTimeout(timeout);
        hero.classList.remove('is-launching');
        hideNavigation();
        void hero.offsetWidth;
        hero.classList.add('is-launching');
        timeout = setTimeout(finish, mobile.matches ? 7100 : 4700);
    }
    function draw() {
        blueprint.classList.remove('is-waiting');
        markComplete(schematicKey);
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
        if (motion.matches) {
            finish();
            markComplete(schematicKey);
            blueprint.classList.remove('is-drawing', 'is-waiting');
        }
    });
    replay.hidden = false;
    drawingReplay.hidden = false;
    // Reserve the header's space while it is hidden, avoiding layout shifts.
    const initialHero = hero.getBoundingClientRect();
    const visibleHeight = Math.min(initialHero.bottom, innerHeight) - Math.max(initialHero.top, 0);
    if (!motion.matches && !introWasCompleted && visibleHeight / initialHero.height >= .25) hideNavigation();
    function skipOffscreenHero() {
        if (hero.getBoundingClientRect().bottom <= (nav?.getBoundingClientRect().height || 0)) {
            if (hero.classList.contains('is-launching') || nav?.classList.contains('is-awaiting-hero')) finish();
        }
    }
    window.addEventListener('scroll', skipOffscreenHero, { passive: true });
    window.addEventListener('resize', () => {
        positionLaunchStage();
        skipOffscreenHero();
    });
    // Each fresh page load gets one launch when the hero enters view.
    // This also handles refreshes that restore a lower scroll position.
    if (!introWasCompleted && !motion.matches) {
        const heroObserver = new IntersectionObserver(entries => {
            if (entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= .25)) {
                play();
                heroObserver.disconnect();
            }
        }, { threshold: .25 });
        heroObserver.observe(hero);
    } else {
        hero.classList.remove('is-launching');
        revealNavigation();
        if (motion.matches) markComplete(introKey);
    }
    if (!motion.matches && !schematicWasCompleted) blueprint.classList.add('is-waiting');
    else blueprint.classList.remove('is-waiting');
    let blueprintTimer;
    let blueprintObserver;
    let blueprintStarted = schematicWasCompleted || motion.matches;
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
        const requiredVisibility = mobile.matches ? .4 : .999;
        blueprintObserver = new IntersectionObserver(entries => {
            clearTimeout(blueprintTimer);
            if (entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= requiredVisibility)) {
                blueprintTimer = setTimeout(() => {
                    stopBlueprintWatch();
                    draw();
                }, 300);
            }
        }, { threshold: [0, requiredVisibility, 1], rootMargin: `-${topInset}px 0px 0px 0px` });
        blueprintObserver.observe(blueprint);
    }
    document.addEventListener('visibilitychange', watchBlueprint);
    window.addEventListener('resize', watchBlueprint);
    if (nav) new ResizeObserver(watchBlueprint).observe(nav);
    if (motion.matches) markComplete(schematicKey);
    watchBlueprint();
})();
