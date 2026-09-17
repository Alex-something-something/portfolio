import LegacyPortfolioPage from '@/components/LegacyPortfolioPage';
import { readPortfolioPage } from '@/lib/portfolio-content';

export const metadata = {
  title: 'Alexander Tong Engineering Portfolio'
};

export default function HomePage() {
  const page = readPortfolioPage('index.html', true);
  return <LegacyPortfolioPage page={page} isHome />;
}
