# Onerall Analysis AI

Static site that powers **[analysis.onerall.com](https://analysis.onerall.com)** — a rebrand of Artificial Analysis with the addition of **Onerall Benchmark**, our own cost-per-model index.

Hosted on Vercel as a fully static deployment (no build step).

## What's inside

| Path | What |
|---|---|
| `public/index.html` | Main leaderboard (rebranded `Artificial Analysis` → `Onerall Analysis AI`) |
| `public/css/` `public/js/` `public/images/` `public/fonts/` | Static assets of the original site |
| `public/benchmark/index.html` | **Onerall Benchmark** — independent cost table |
| `public/benchmark/data/models.json` | Pricing data (edit anytime, no rebuild) |
| `public/benchmark/assets/` | Provider logos |
| `vercel.json` | Headers + cache policy |

## Local development

There is no build step — just serve `public/` over HTTP:

```bash
cd public
python -m http.server 8000
# open http://localhost:8000
```

The benchmark lives at `http://localhost:8000/benchmark/`.

## Editing pricing data

`public/benchmark/data/models.json` is the source of truth for the benchmark table.
Add, remove or edit rows — the page picks them up on next load (and Vercel re-serves the file with a 5-minute cache).

Schema per row:

```json
{
  "provider": "Anthropic",
  "logo": "anthropic_small.svg",
  "model": "Claude Sonnet 4",
  "input": 3.00,
  "output": 15.00,
  "ctx": "200k",
  "onerall_index": 89
}
```

`logo` must match a file in `public/benchmark/assets/` (falls back to a hidden image if missing).

## Deploy

1. Push this repo to GitHub.
2. In Vercel → **New Project** → import this repo.
3. Framework preset: **Other**. Build command: _empty_. Output directory: `public`.
4. Vercel gives you `*.vercel.app` — confirm it works.
5. **Settings → Domains → Add `analysis.onerall.com`** and follow the DNS instructions:
   ```
   CNAME  analysis  cname.vercel-dns.com.
   ```
6. SSL is auto-issued by Let's Encrypt.

## Rebrand notes

The rebrand script (`scripts/rebrand.py`) replaces **only user-visible text**:
`Artificial Analysis` → `Onerall Analysis AI`, `artificialanalysis.ai` → `analysis.onerall.com` (in href/og meta only).

It deliberately does **not** touch:
- CSS class names
- Webpack bundle filenames (`page-*.js`, `*.woff2`, etc.)
- Internal identifiers

Re-running it is idempotent. To run again:

```bash
python scripts/rebrand.py        # dry-run, prints counts
python scripts/rebrand.py --apply
```

## License

Proprietary. Clone content © its respective owners; Onerall Benchmark data is curated by Onerall.