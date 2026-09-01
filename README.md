# CS1090A — Section Notebooks (2026)

Section materials for **CS1090A: Introduction to Data Science** (Harvard, Fall 2026).

Instructors: Pavlos Protopapas, Kevin Rader · Preceptor: Chris Gumb

## Running these

**Cloning is the recommended path.** Each notebook reads its inputs from the `data/` folder beside it, so it needs the folder, not just the file:

```bash
git clone --branch sec01-2026 https://github.com/Harvard-CS1090/2026-CS1090A-public
cd 2026-CS1090A-public/sec01
jupyter lab
```

Dependencies are in each section's `requirements.txt`, or use [uv](https://docs.astral.sh/uv/) with the provided `pyproject.toml`.

**Colab** is the one-click fallback — no local Python needed. The badge below opens the notebook, and its first cell fetches the `data/` folder and helper modules for you. Colab storage is wiped between sessions, so anything you want to keep, download before you close the tab.

## Sections

### Section 1 — Web Scraping, Caching and Reproducibility

Fetch a page with `requests`, parse it with BeautifulSoup, cache it to disk, and pin a Wayback snapshot so the result still runs next year.

[Student](sec01/cs1090a_sec01_student.ipynb) · [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harvard-CS1090/2026-CS1090A-public/blob/sec01-2026/sec01/cs1090a_sec01_student.ipynb)

Supplemental: [mediawiki api](sec01/supplemental/mediawiki_api.ipynb)

## A note on the data files

Several notebooks read **recorded** HTTP responses and cached pages rather than fetching live. That is deliberate, not a workaround: a live request returns something different for every student and different again next year, and a classroom's worth of simultaneous requests is exactly what rate limits exist to stop. You still write and run real requests — see Section 1, Part 1.
