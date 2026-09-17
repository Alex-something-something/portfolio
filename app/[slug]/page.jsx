import { notFound } from 'next/navigation';
import LegacyPortfolioPage from '@/components/LegacyPortfolioPage';
import { portfolioPages, readPortfolioPage } from '@/lib/portfolio-content';

export function generateStaticParams() {
  return Object.keys(portfolioPages).map((slug) => ({ slug }));
}

export async function generateMetadata({ params }) {
  const { slug } = await params;
  const filename = portfolioPages[slug];
  if (!filename) return {};
  const page = readPortfolioPage(filename);
  return { title: page.title.replace(/\s*\|\s*Alexander Tong\s*$/i, '') };
}

export default async function PortfolioDetailPage({ params }) {
  const { slug } = await params;
  const filename = portfolioPages[slug];
  if (!filename) notFound();
  const page = readPortfolioPage(filename);
  return <LegacyPortfolioPage page={page} />;
}
