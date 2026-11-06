# AI plan limits (verified, updated daily)

Prices and usage limits for the paid plans of Claude, ChatGPT, Cursor, GitHub Copilot, Google AI (Gemini), Devin, Replit, Lovable, v0,
Bolt, Kiro, Amp and Augment. Every limit links to the vendor page it was copied from, with the date it was checked. Where a vendor does not
publish a number, the file says so (`"published": false`) instead of guessing.

The data is maintained at **[getstackversus.com/limits](https://getstackversus.com/limits)** and this repo mirrors it once a day
(GitHub Action, commit only when something changed), so the git history doubles as a change log.

<!-- table:start -->
| Tool | Vendor | Plans (USD / month) | Limits, sources, FAQ |
|---|---|---|---|
| Claude | Anthropic | Free, Pro $20, Max $100, Ultra $200, Team (standard seat) $25, Team (premium seat) $125, Enterprise (custom) | [claude](https://getstackversus.com/limits/claude) |
| ChatGPT + Codex | OpenAI | Free, Go $8, Plus $20, Pro ($100) $100, Pro ($200) $200, Pro ($500) $500, Business $25, Business Codex (pay as you go) (custom), Enterprise & Edu (custom) | [chatgpt](https://getstackversus.com/limits/chatgpt) |
| Cursor | Cursor (bundled with X Premium and Grok) | Free, Plus $8, Premium $30, Super $100, Ultra $200, Teams $30, Enterprise (custom) | [cursor](https://getstackversus.com/limits/cursor) |
| GitHub Copilot | GitHub (Microsoft) | Free, Student free, Pro $10, Pro+ $39, Max $100, Business $19, Enterprise $39, Copilot access $10 | [github-copilot](https://getstackversus.com/limits/github-copilot) |
| Google AI (Gemini, Antigravity) | Google | Free, AI Plus $4.99, AI Pro $19.99, AI Ultra 5x $99.99, AI Ultra 20x $199.99 | [google-ai](https://getstackversus.com/limits/google-ai) |
| Devin (Windsurf) | Cognition | Free, Pro $20, Max $200, Teams $40, Enterprise (custom) | [devin](https://getstackversus.com/limits/devin) |
| Replit | Replit | Starter free, Core $20, Pro $100, Enterprise (custom) | [replit](https://getstackversus.com/limits/replit) |
| Lovable | Lovable | Free, Pro $25, Business $50, Enterprise (custom) | [lovable](https://getstackversus.com/limits/lovable) |
| v0 | Vercel | Free, Plus $30, Business $100, Enterprise (custom) | [v0](https://getstackversus.com/limits/v0) |
| Bolt | StackBlitz | Free, Lite $9, Pro $25, Teams $30, Enterprise (custom) | [bolt](https://getstackversus.com/limits/bolt) |
| Kiro | Amazon Web Services | Free, Pro $20, Pro+ $40, Pro Max $100, Power $200, Teams (credit pooling) $20, Enterprise (custom) | [kiro](https://getstackversus.com/limits/kiro) |
| Amp | Sourcegraph | Hobby free, Individual Megawatt $20, Education (Megawatt at 50% off) $10, Individual Gigawatt $200, Teams free, Enterprise (custom) | [amp](https://getstackversus.com/limits/amp) |
| Augment Code | Augment | Standard $20, Business $100, Enterprise (custom) | [augment](https://getstackversus.com/limits/augment) |

Data checked up to **2026-11-06**.
<!-- table:end -->

## Files

| File | What |
|---|---|
| [`data/limits.json`](data/limits.json) | Tools, plans, prices (monthly and annual), every limit with metric, window (`5h`, `7d`, `month`), source URL |
| [`data/limits.csv`](data/limits.csv) | One row per plan limit, same fields flattened, for spreadsheets |
| [`data/changes.json`](data/changes.json) | Dated changes to prices and limits (old value, new value, source) |

## Use it

```bash
curl -s https://raw.githubusercontent.com/congptvinadic-debug/ai-plan-limits/main/data/limits.json \
  | jq '.tools[] | select(.id=="cursor") | .plans[] | {name, priceUsd}'
```

The same data is served live at `https://getstackversus.com/api/v1/limits.json` (and `.csv`), and agents can query it over MCP:

```bash
claude mcp add --transport http stackversus https://getstackversus.com/api/mcp
```

Per-tool pages with FAQ and head-to-head comparisons: [/limits/claude](https://getstackversus.com/limits/claude),
[/limits/compare/cursor-vs-github-copilot](https://getstackversus.com/limits/compare/cursor-vs-github-copilot),
[plan picker](https://getstackversus.com/calculators/ai-plan-picker), [change log](https://getstackversus.com/changes).

## Badges

Show the cheapest paid plan of a tool and its check date in your README or blog, e.g.
`[![Claude plans](https://getstackversus.com/badge/claude.svg)](https://getstackversus.com/limits/claude)`

[![Claude plans](https://getstackversus.com/badge/claude.svg)](https://getstackversus.com/limits/claude) [![Cursor plans](https://getstackversus.com/badge/cursor.svg)](https://getstackversus.com/limits/cursor) [![GitHub Copilot plans](https://getstackversus.com/badge/github-copilot.svg)](https://getstackversus.com/limits/github-copilot)

 All badges: [getstackversus.com/badges](https://getstackversus.com/badges).

## Corrections

Spotted a limit that changed? Open an issue with the vendor URL. Numbers are only changed after the vendor page is read again.

## License

Data: [CC BY 4.0](LICENSE). Credit "StackVersus" with a link to the tool page on getstackversus.com.
