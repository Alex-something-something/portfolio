(() => {
    const setRelatedVisibility = (slot, visible) => {
        const figure = slot.closest('figure.media-slide');
        const item = figure || slot;
        item.hidden = !visible;

        if (!figure) {
            const caption = slot.nextElementSibling;
            if (caption?.classList.contains('caption')) caption.hidden = !visible;
        }
    };

    const pruneEmptyContainer = slot => {
        const containers = [
            slot.closest('.project-carousel'),
            slot.closest('.image-block'),
            slot.closest('.project-hero-media')
        ].filter(Boolean);

        containers.forEach(container => {
            const slots = [...container.querySelectorAll('[data-media]')];
            const finished = slots.every(item => item.dataset.mediaState !== 'loading');
            const available = slots.some(item => item.dataset.mediaState === 'available');
            if (finished) container.hidden = !available;
        });
    };

    document.querySelectorAll('[data-media]').forEach(slot => {
        const isVideo = slot.dataset.mediaType === 'video';
        const media = document.createElement(isVideo ? 'video' : 'img');
        slot.dataset.mediaState = 'loading';
        setRelatedVisibility(slot, false);

        const show = () => {
            if (!media.isConnected) slot.append(media);
            slot.dataset.mediaState = 'available';
            slot.classList.add('has-media');
            slot.classList.add(isVideo ? 'has-video-media' : 'has-image-media');
            setRelatedVisibility(slot, true);
            pruneEmptyContainer(slot);
        };
        if (isVideo) {
            media.controls = true;
            media.playsInline = true;
            media.preload = 'metadata';
            if (slot.dataset.autoplay === 'true') {
                media.autoplay = true;
                media.muted = true;
                media.defaultMuted = true;
                media.loop = true;
            }
            media.setAttribute('aria-label', slot.dataset.alt);
            media.addEventListener('loadedmetadata', () => {
                show();
                if (slot.dataset.autoplay === 'true') media.play().catch(() => {});
            }, { once: true });
        } else {
            media.alt = slot.dataset.alt;
            media.decoding = 'async';
            media.addEventListener('load', show, { once: true });
        }
        media.addEventListener('error', () => {
            media.remove();
            slot.dataset.mediaState = 'missing';
            slot.classList.remove('has-media', 'has-image-media', 'has-video-media');
            setRelatedVisibility(slot, false);
            pruneEmptyContainer(slot);
        });
        media.src = slot.dataset.media;
    });
})();
