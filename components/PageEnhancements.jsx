'use client';

import { useEffect } from 'react';

const scripts = [
  'portfolio-media.js',
  'portfolio-carousel.js',
  'portfolio-intro.js',
  'portfolio-schematic.js'
];

const navigationKeys = {
  internal: 'portfolio:internal-navigation',
  homeVisited: 'portfolio:home-visited',
  introComplete: 'portfolio:intro-complete',
  schematicComplete: 'portfolio:schematic-complete',
  mobileReturnToHero: 'portfolio:mobile-return-to-hero'
};

let navigationContextInitialized = false;

function initializeNavigationContext(isHome) {
  if (navigationContextInitialized) return;
  navigationContextInitialized = true;

  try {
    const navigationType = performance.getEntriesByType('navigation')[0]?.type;
    const internalNavigation = sessionStorage.getItem(navigationKeys.internal) === 'true';
    sessionStorage.removeItem(navigationKeys.internal);

    const freshSiteEntry = navigationType === 'navigate' && !internalNavigation;
    if (navigationType === 'reload' || freshSiteEntry) {
      sessionStorage.removeItem(navigationKeys.introComplete);
      sessionStorage.removeItem(navigationKeys.schematicComplete);
      sessionStorage.removeItem(navigationKeys.homeVisited);
    }

    if (isHome) sessionStorage.setItem(navigationKeys.homeVisited, 'true');
  } catch {
    // The portfolio still works when session storage is unavailable.
  }
}

function markInternalNavigation() {
  try {
    sessionStorage.setItem(navigationKeys.internal, 'true');
  } catch {
    // Navigation remains functional without persisted animation state.
  }
}

function loadScript(source) {
  return new Promise((resolve, reject) => {
    const existing = [...document.scripts].find((script) => script.dataset.portfolioScript === source);
    if (existing) {
      if (existing.dataset.loaded === 'true') resolve();
      else {
        existing.addEventListener('load', resolve, { once: true });
        existing.addEventListener('error', reject, { once: true });
      }
      return;
    }

    const script = document.createElement('script');
    script.src = source;
    script.async = false;
    script.dataset.portfolioScript = source;
    script.onload = () => {
      script.dataset.loaded = 'true';
      resolve();
    };
    script.onerror = reject;
    document.body.append(script);
  });
}

export default function PageEnhancements({ isHome }) {
  useEffect(() => {
    initializeNavigationContext(isHome);
    const controller = new AbortController();
    const prefix = isHome ? '' : '../';
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const mobile = window.matchMedia('(max-width: 650px)');

    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          currentObserver.unobserve(entry.target);
        }
      });
    }, { root: null, rootMargin: '0px', threshold: 0.15 });

    document.querySelectorAll('.scroll-fade').forEach((element) => observer.observe(element));

    const revealSelector = isHome
      ? '.project-grid > .section-title, #contact'
      : 'main > nav, .project-header, .project-hero-media, .content-section, main > .detail-return, main > footer';
    const revealElements = [...document.querySelectorAll(revealSelector)]
      .filter((element) => !element.closest('.hero, .argo-blueprint'));

    revealElements.forEach((element, index) => {
      element.classList.add('portfolio-reveal');
      element.style.setProperty('--portfolio-reveal-delay', `${Math.min(index % 3, 2) * 70}ms`);
    });

    const revealObserver = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          currentObserver.unobserve(entry.target);
        }
      });
    }, { root: null, rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    if (motion.matches) {
      revealElements.forEach((element) => element.classList.add('is-revealed'));
    } else {
      document.documentElement.classList.add('portfolio-motion-ready');
      requestAnimationFrame(() => revealElements.forEach((element) => revealObserver.observe(element)));
    }

    function transitionToInternalPage(event) {
      if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      const link = event.target instanceof Element ? event.target.closest('a[href]') : null;
      if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self') || link.dataset.schematicPart) return;

      const destination = new URL(link.href, location.href);
      if (destination.origin !== location.origin) return;
      const isMobileReturnLink = !isHome && mobile.matches && link.classList.contains('back-link');
      if (isMobileReturnLink) destination.hash = '';
      const sameDocument = destination.pathname === location.pathname && destination.search === location.search;
      if (sameDocument && destination.hash) return;

      event.preventDefault();
      if (isHome && mobile.matches) {
        try {
          sessionStorage.setItem(navigationKeys.mobileReturnToHero, 'true');
        } catch {
          // The return transition still works when session storage is unavailable.
        }
      }
      markInternalNavigation();
      document.documentElement.classList.add('is-page-leaving');
      setTimeout(() => location.assign(destination.href), motion.matches ? 0 : 240);
    }

    function restorePage() {
      document.documentElement.classList.remove('is-page-leaving');
      if (!isHome || !mobile.matches) return;
      try {
        if (sessionStorage.getItem(navigationKeys.mobileReturnToHero) !== 'true') return;
        sessionStorage.removeItem(navigationKeys.mobileReturnToHero);
        history.scrollRestoration = 'manual';
        const returnToHero = () => window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
        returnToHero();
        requestAnimationFrame(() => {
          returnToHero();
          setTimeout(returnToHero, 50);
        });
        setTimeout(() => { history.scrollRestoration = 'auto'; }, 150);
      } catch {
        // Browser scroll restoration remains available without session storage.
      }
    }

    document.addEventListener('click', transitionToInternalPage);
    window.addEventListener('pageshow', restorePage);
    restorePage();

    async function startEnhancements() {
      const requiredScripts = isHome ? scripts : scripts.slice(0, 1);
      for (const script of requiredScripts) {
        if (controller.signal.aborted) return;
        await loadScript(`${prefix}${script}`);
      }
    }

    startEnhancements().catch((error) => {
      if (!controller.signal.aborted) console.error('Portfolio enhancement failed to load.', error);
    });

    return () => {
      controller.abort();
      observer.disconnect();
      revealObserver.disconnect();
      document.removeEventListener('click', transitionToInternalPage);
      window.removeEventListener('pageshow', restorePage);
      document.documentElement.classList.remove('portfolio-motion-ready');
    };
  }, [isHome]);

  return null;
}
