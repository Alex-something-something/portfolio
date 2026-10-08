(() => {
    const detailPage = document.querySelector('main.portfolio-detail');
    let lightbox;
    const visibleVideos = new Set();
    window.__portfolioVideoObserver?.disconnect();
    if (window.__portfolioVideoVisibilityHandler) {
        document.removeEventListener('visibilitychange', window.__portfolioVideoVisibilityHandler);
    }
    const videoObserver = new IntersectionObserver(entries => {
        entries.forEach(({ target: video, isIntersecting, intersectionRatio }) => {
            if (isIntersecting && intersectionRatio >= 0.6) {
                visibleVideos.add(video);
                if (!document.hidden) video.play().catch(() => {});
            } else {
                visibleVideos.delete(video);
                video.pause();
            }
        });
    }, { threshold: [0, 0.6] });
    window.__portfolioVideoObserver = videoObserver;
    window.__portfolioVideoVisibilityHandler = () => {
        visibleVideos.forEach(video => {
            if (document.hidden) video.pause();
            else if (video.isConnected) video.play().catch(() => {});
        });
    };
    document.addEventListener('visibilitychange', window.__portfolioVideoVisibilityHandler);

    function getLightbox() {
        if (lightbox) return lightbox;
        lightbox = document.createElement('dialog');
        lightbox.className = 'media-lightbox';
        lightbox.setAttribute('aria-label', 'Enlarged project image');
        lightbox.innerHTML = '<div class="media-lightbox-actions"><button type="button" class="media-lightbox-zoom">Zoom in</button><button type="button" class="media-lightbox-close">Close</button></div><img alt=""><p class="media-lightbox-caption"></p>';
        const zoomButton = lightbox.querySelector('.media-lightbox-zoom');
        zoomButton.setAttribute('aria-pressed', 'false');
        zoomButton.addEventListener('click', () => {
            const zoomed = lightbox.classList.toggle('is-zoomed');
            zoomButton.textContent = zoomed ? 'Fit to screen' : 'Zoom in';
            zoomButton.setAttribute('aria-pressed', String(zoomed));
        });
        lightbox.querySelector('.media-lightbox-close').addEventListener('click', () => lightbox.close());
        lightbox.addEventListener('click', (event) => {
            if (event.target === lightbox) lightbox.close();
        });
        lightbox.addEventListener('close', () => {
            lightbox.classList.remove('is-zoomed');
            zoomButton.textContent = 'Zoom in';
            zoomButton.setAttribute('aria-pressed', 'false');
        });
        document.body.append(lightbox);
        return lightbox;
    }

    function openLightbox(source, alt, caption, isDiagram = false) {
        const dialog = getLightbox();
        dialog.classList.toggle('is-diagram', isDiagram);
        dialog.querySelector('img').src = source;
        dialog.querySelector('img').alt = alt;
        dialog.querySelector('.media-lightbox-caption').textContent = caption || alt;
        dialog.showModal();
        dialog.querySelector('.media-lightbox-close').focus();
    }

    document.querySelectorAll('[data-media]').forEach(slot => {
        const isVideo = slot.dataset.mediaType === 'video';
        const media = document.createElement(isVideo ? 'video' : 'img');

        // Missing media must remain visible as a filename placeholder. Hiding the
        // slot or one of its ancestors can remove whole project sections and
        // collapse the two-column page layout.
        slot.hidden = false;
        const figure = slot.closest('figure.media-slide');
        if (figure) figure.hidden = false;
        const caption = figure ? null : slot.nextElementSibling;
        if (caption?.classList.contains('caption')) caption.hidden = false;
        [slot.closest('.project-carousel'), slot.closest('.image-block'), slot.closest('.project-hero-media')]
            .filter(Boolean)
            .forEach(container => { container.hidden = false; });
        slot.dataset.mediaState = 'loading';
        slot.classList.add('is-loading');

        const show = () => {
            if (!media.isConnected) slot.append(media);
            slot.dataset.mediaState = 'available';
            slot.classList.remove('is-loading', 'is-missing');
            slot.classList.add('has-media');
            slot.classList.add(isVideo ? 'has-video-media' : 'has-image-media');
            if (!isVideo && detailPage?.contains(slot)) {
                slot.classList.add('is-zoomable');
                slot.tabIndex = 0;
                slot.setAttribute('role', 'button');
                slot.setAttribute('aria-haspopup', 'dialog');
                slot.setAttribute('aria-label', `View larger: ${media.alt || 'project image'}`);
                slot.title = 'View larger image';
            }
        };

        if (isVideo) {
            media.controls = true;
            media.autoplay = false;
            if (slot.dataset.poster) media.poster = slot.dataset.poster;
            media.playsInline = true;
            media.preload = 'metadata';
            media.muted = true;
            media.defaultMuted = true;
            media.loop = true;
            media.setAttribute('aria-label', slot.dataset.alt);
            media.addEventListener('loadedmetadata', () => {
                show();
                videoObserver.observe(media);
            }, { once: true });
        } else {
            media.alt = slot.dataset.alt;
            media.decoding = 'async';
            media.addEventListener('load', show, { once: true });
            if (detailPage?.contains(slot)) {
                const openImage = () => {
                    if (slot.dataset.mediaState !== 'available') return;
                    const caption = slot.closest('figure.media-slide')?.querySelector('figcaption')
                        || slot.nextElementSibling;
                    openLightbox(media.currentSrc || media.src, media.alt,
                        caption?.matches('figcaption, .caption') ? caption.textContent.trim() : media.alt);
                };
                slot.addEventListener('click', openImage);
                slot.addEventListener('keydown', (event) => {
                    if (event.key !== 'Enter' && event.key !== ' ') return;
                    event.preventDefault();
                    openImage();
                });
            }
        }

        media.addEventListener('error', () => {
            media.remove();
            slot.hidden = false;
            slot.dataset.mediaState = 'missing';
            slot.classList.remove('is-loading', 'has-media', 'has-image-media', 'has-video-media');
            slot.classList.add('is-missing');
            slot.classList.remove('is-zoomable');
            slot.removeAttribute('tabindex');
            slot.removeAttribute('role');
            slot.removeAttribute('aria-haspopup');
            slot.removeAttribute('aria-label');
        });

        media.src = slot.dataset.media;
    });

    detailPage?.querySelectorAll('.engineering-visual svg[role="img"]').forEach(svg => {
        const visual = svg.closest('.engineering-visual');
        const alt = svg.querySelector('title')?.textContent.trim() || 'Engineering diagram';
        visual.classList.add('is-zoomable');
        visual.tabIndex = 0;
        visual.setAttribute('role', 'button');
        visual.setAttribute('aria-haspopup', 'dialog');
        visual.setAttribute('aria-label', `View larger: ${alt}`);
        const openDiagram = () => {
            const copy = svg.cloneNode(true);
            copy.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
            const source = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(new XMLSerializer().serializeToString(copy))}`;
            openLightbox(source, alt, alt, true);
        };
        visual.addEventListener('click', openDiagram);
        visual.addEventListener('keydown', (event) => {
            if (event.key !== 'Enter' && event.key !== ' ') return;
            event.preventDefault();
            openDiagram();
        });
    });
})();
