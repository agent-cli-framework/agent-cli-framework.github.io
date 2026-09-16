# agent-cli-framework.github.io

The project site for [aclif](https://github.com/agent-cli-framework/aclif), served by GitHub Pages at https://agent-cli-framework.github.io.

Static HTML with one stylesheet and no build step. `.nojekyll` tells Pages to serve the files as they are.

| Page | Covers |
|---|---|
| `index.html` | What aclif is, why a CLI, what an agent gets, where it runs |
| `getting-started.html` | Install, credentials, the introspection workflow, reading the envelope |
| `build-a-cli.html` | Scaffolding a CLI with its own name and providers, provider instances, writing a provider |
| `embedding.html` | The runtime, the three ways to run it, the gateway with SSO and a vault, what a host supplies |
| `providers.html` | Shipped providers, the three tiers, writing a provider, tenant catalogs, canonical names, manifests |
| `faq.html` | Developer FAQ, the most current statement of the argument: access via aclif versus an MCP server, the three ways to run it, runtime requirements, gateway credentials and shared service accounts, context cost and design-time command selection, providers and instances, custom APIs, tenant customizations, canonical names, errors, introspection and quota |

## Publishing

The repository is public and GitHub Pages serves `main` from the root folder at https://www.aclif.ai, with `aclif.ai` redirecting to it. GitHub wrote the `CNAME` file when the custom domain was set in Settings, Pages. It holds `www.aclif.ai` and should not be edited by hand, since a change here changes the domain setting.

DNS at Hover: four A records and four AAAA records on `aclif.ai` pointing at GitHub Pages, and `www` as a CNAME to `agent-cli-framework.github.io`. Once the certificate is issued, turn on "Enforce HTTPS" in the same settings page.

## Editing

Every page has the same header and footer. Edit them in all six files together. Content follows the aclif repository's documentation, and the deep links point at `docs/` on the `main` branch, so a renamed document there needs the matching link changed here.
