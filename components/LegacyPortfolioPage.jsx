import PageEnhancements from '@/components/PageEnhancements';

export default function LegacyPortfolioPage({ page, isHome = false }) {
  return (
    <>
      {page.styles ? <style dangerouslySetInnerHTML={{ __html: page.styles }} /> : null}
      <main dangerouslySetInnerHTML={{ __html: page.body }} />
      <PageEnhancements isHome={isHome} />
    </>
  );
}
