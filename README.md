# agent-cli-framework.github.io

The project site for [aclif](https://github.com/agent-cli-framework/aclif), served by GitHub Pages at https://agent-cli-framework.github.io.

Static HTML with one stylesheet and no build step. `.nojekyll` tells Pages to serve the files as they are.

| Page | Covers |
|---|---|
| `index.html` | What aclif is, why a CLI, what an agent gets, where it runs |
| `getting-started.html` | Install, credentials, the introspection workflow, reading the envelope |
| `build-a-cli.html` | Scaffolding a CLI with its own name and providers |
| `embedding.html` | The runtime, the three deployments, what a host supplies |
| `providers.html` | Shipped providers, the three tiers, writing a provider, catalogues, aliases, manifests |

## Publishing

The repository is private while the aclif repository is private. To publish: make this repository public, then in Settings, Pages, set the source to the `main` branch, root folder, and the custom domain to `aclif.io`. The `CNAME` file in this repository holds that domain; GitHub rewrites it if the setting changes. DNS for `aclif.io` is four A records and four AAAA records to GitHub Pages, with `www` as a CNAME to `agent-cli-framework.github.io`.

## Editing

Every page carries the same header and footer; edit them in all five files together. Content follows the aclif repository's documentation, and the deep links point at `docs/` on the `main` branch, so a renamed document there needs the matching link changed here.
