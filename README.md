# CS1090A — Section Notebooks (2026)

Section materials for **CS1090A: Introduction to Data Science** (Harvard, Fall 2026).

Instructors: Pavlos Protopapas, Kevin Rader · Preceptor: Chris Gumb

## Running these

**Cloning is the recommended path.** Each notebook reads its inputs from the `data/` folder beside it, so it needs the folder, not just the file:

```bash
git clone --branch sec02-2026d https://github.com/Harvard-CS1090/2026-CS1090A-public
cd 2026-CS1090A-public/sec02
uv run jupyter lab
```

That is the whole setup — the same [uv](https://docs.astral.sh/uv/) you installed for HW0. `uv run` reads `pyproject.toml`, builds the environment the first time, and opens JupyterLab. Nothing to activate, nothing to install by hand.

If you'd rather do it the way HW0 Part 1 walked through, each section also ships a `requirements.txt`:

```bash
uv venv
uv pip install -r requirements.txt
source .venv/bin/activate     # Windows: .venv\Scripts\activate
jupyter lab
```

**Colab** is the one-click fallback — no local Python needed. The badge below opens the notebook, and its first cell fetches the `data/` folder and helper modules for you.

**Do `File → Save a copy in Drive` before you start.** Opening from GitHub gives you a notebook you can type in and run straight away, but with nowhere to save it — close the tab and the work is gone. Saving a copy first gives you one that persists. Separately, the *files* Colab creates (your `data/` folder, anything you write to disk) are wiped when the session ends, so download anything you want to keep.

## Sections

### Section 1 — Web Scraping, Caching and Reproducibility

Fetch a page with `requests`, parse it with BeautifulSoup, cache it to disk, and pin a Wayback snapshot so the result still runs next year.

[Student](sec01/cs1090a_sec01_student.ipynb) · [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harvard-CS1090/2026-CS1090A-public/blob/sec02-2026d/sec01/cs1090a_sec01_student.ipynb)

Supplemental: [mediawiki api](sec01/supplemental/mediawiki_api.ipynb)

### Section 2 — Pandas and Plotting

Build a DataFrame, give each column the right dtype, audit it for duplicates and implausible values, and plot it — including how to recognise a chart that runs without error and still misleads.

[Student](sec02/cs1090a_sec02_student.ipynb) · [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Harvard-CS1090/2026-CS1090A-public/blob/sec02-2026d/sec02/cs1090a_sec02_student.ipynb)

Supplemental: [advanced visualization](sec02/supplemental/advanced_visualization.ipynb) · [duckdb sql on files](sec02/supplemental/duckdb_sql_on_files.ipynb) · [matplotlib seaborn reference](sec02/supplemental/matplotlib_seaborn_reference.ipynb) · [pandas quickstart](sec02/supplemental/pandas_quickstart.ipynb) · [polars intro](sec02/supplemental/polars_intro.ipynb)

## A note on the data files

Several notebooks read **recorded** HTTP responses and cached pages rather than fetching live. That is deliberate, not a workaround: a live request returns something different for every student and different again next year, and a classroom's worth of simultaneous requests is exactly what rate limits exist to stop. You still write and run real requests — see Section 1, Part 1.
