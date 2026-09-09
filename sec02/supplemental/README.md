# Supplemental Notebooks — Module 1

Self-paced, example-focused notebooks carrying the *syntax* depth the
(conceptual) lectures omit. Grouped by the section they support:

## Section 1 — `supplemental/`

| Notebook | Tier | Supports |
|---|---|---|
| `mediawiki_api.ipynb` | **Required** | HW1 Q6–Q8 — search → stable `pageid`, batched exact-title + batched wikitext lookups, guarded disk caching, infobox extraction, polite concurrency |

## Section 2 — `supplemental/`

| Notebook | Tier | Supports |
|---|---|---|
| `pandas_quickstart.ipynb` | Optional | The syntax floor: the four verbs in ~20 minutes, self-contained. Written as pre-reading for Lecture 2; read it after the fact if Section 2 Part 1 went quickly |
| `matplotlib_seaborn_reference.ipynb` | **Required** | HW1 Q5/Q8 — Figure/Axes anatomy, seaborn grammar, distribution chooser, accessibility, checklist |
| `polars_intro.ipynb` | Optional | Lec 2 thread — pandas vs. Polars, lazy queries, Parquet interop |
| `duckdb_sql_on_files.ipynb` | Optional (**AC209A: supports the HW1 SQL question**) | SQL as the third dialect; query DataFrames and files directly |
| `advanced_visualization.ipynb` | Optional | Lec 3 thread — faceting, pairplot, heatmaps, annotation, interactivity |

All notebooks execute top-to-bottom (`Restart Kernel and Run All`). Network:
`mediawiki_api` (Wikipedia API); seaborn datasets download on first run.
`data/` and `figures/` are runtime-generated and gitignored.
plotly degrades gracefully if not installed locally (it *is* in course requirements).
