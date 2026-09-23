import './globals.css';

const repositoryName = process.env.GITHUB_REPOSITORY?.split('/')[1];
const usesCustomDomain = Boolean(process.env.CUSTOM_DOMAIN);
const publicBasePath = process.env.GITHUB_ACTIONS === 'true' && repositoryName && !usesCustomDomain
  ? `/${repositoryName}`
  : '';

export const metadata = {
  title: {
    default: 'Alexander Tong Engineering Portfolio',
    template: '%s | Alexander Tong'
  },
  description: 'Alexander Tong’s mechanical engineering portfolio, featuring spaceflight hardware, research fixtures, manufacturing, and electromechanical design.'
};

export const viewport = {
  width: 'device-width',
  initialScale: 1
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: "document.documentElement.classList.add('portfolio-js')" }} />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link rel="apple-touch-icon" sizes="180x180" href={`${publicBasePath}/apple-touch-icon.png`} />
        <link rel="icon" type="image/png" sizes="32x32" href={`${publicBasePath}/favicon-32x32.png`} />
        <link rel="icon" type="image/png" sizes="16x16" href={`${publicBasePath}/favicon-16x16.png`} />
        <link rel="manifest" href={`${publicBasePath}/site.webmanifest`} />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
      </head>
      <body>{children}</body>
    </html>
  );
}
