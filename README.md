# Open AI utilities project

Small Python experiments against the [OpenAI API](https://platform.openai.com/docs/overview). The main flow generates short, alt-text-style descriptions for a list of **public image URLs** using a vision-capable model (`gpt-4o-mini`), with requests sent **concurrently** via `asyncio`.

## Requirements

- Python 3.10+
- An OpenAI API key with access to the Responses API and vision models

## Setup

1. Clone or copy this repository.

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install openai python-dotenv
   ```

   For the separate NLP-to-SQL script (`nlp_to_sql.py`), you also need:

   ```bash
   pip install pandas sqlalchemy
   ```

4. Create a `.env` file in the project root (do not commit it; it is listed in `.gitignore`):

   ```env
   OPENAI_API_KEY=sk-...
   ```

## Run the image alt generator

From the project root (so `.env` and imports resolve correctly):

```bash
python3 main.py
```

This loads URLs from `input_images.py`, calls `generate_image_alts()` in `oai_image_alt.py`, and prints a list of description strings.

To try other images, edit the `IMAGE_URLS` list in `input_images.py`. URLs must be reachable by OpenAI’s servers (e.g. HTTPS, publicly accessible).

## Project layout

| File | Role |
|------|------|
| `main.py` | Entry point; intended to grow into a small “display” orchestrator. |
| `oai_image_alt.py` | Async OpenAI Responses API calls, prompt text, and `generate_image_alts()`. |
| `input_images.py` | List of image URLs used as input. |
| `nlp_to_sql.py` | Course-style example: natural language → SQL over sample CSV data (separate script). |
| `sales_data_sample.csv` | Sample data for `nlp_to_sql.py`. |

## Notes

- **Async:** `generate_image_alts` uses `asyncio.gather` so multiple images are processed in parallel (overlapping network I/O), not strictly one-after-another.
- **Security:** Never commit API keys or paste them into source files; use `.env` locally and rotate keys if they are exposed.
