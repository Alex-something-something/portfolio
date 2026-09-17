const repositoryName = process.env.GITHUB_REPOSITORY?.split('/')[1];
const isGitHubPagesBuild = process.env.GITHUB_ACTIONS === 'true' && repositoryName;
const basePath = isGitHubPagesBuild ? `/${repositoryName}` : '';

/** @type {import('next').NextConfig} */
const nextConfig = {
  agentRules: false,
  output: 'export',
  trailingSlash: true,
  images: { unoptimized: true },
  basePath,
  assetPrefix: basePath
};

export default nextConfig;
