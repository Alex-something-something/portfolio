(() => {
    document.querySelectorAll('[data-media]').forEach(slot => {
        const isVideo = slot.dataset.mediaType === 'video';
        const media = document.createElement(isVideo ? 'video' : 'img');
        const show = () => {
            if (!media.isConnected) slot.append(media);
            slot.classList.add('has-media');
        };
        if (isVideo) {
            media.controls = true;
            media.playsInline = true;
            media.preload = 'metadata';
            media.setAttribute('aria-label', slot.dataset.alt);
            media.addEventListener('loadedmetadata', show, { once: true });
        } else {
            media.alt = slot.dataset.alt;
            media.decoding = 'async';
            media.addEventListener('load', show, { once: true });
        }
        media.addEventListener('error', () => {
            media.remove();
            slot.classList.remove('has-media');
        });
        media.src = slot.dataset.media;
    });
})();
