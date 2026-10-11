# hr-analytics

A tiny Python package that reads an `employees` Delta table from Databricks
and prints a summary. Built to teach **CI/CD with dev / UAT / prod environments**.

The catalog is chosen by the `APP_ENV` variable:

| APP_ENV | Catalog   |
|---------|-----------|
| `dev`   | `hrb_dev` |
| `uat`   | `hrb_uat` |
| `prod`  | `hrb_prod`|

> Commands below are **Windows / PowerShell first** (the default VS Code terminal on
> Windows). The **macOS/Linux** equivalent is in a `#` comment on each line.

## Run locally (PowerShell)

```powershell
python -m venv .venv                       # macOS/Linux: python3 -m venv .venv
.venv\Scripts\Activate.ps1                 # macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"                    # same on both

# credentials (never commit these)
$env:DATABRICKS_HOST="adb-xxxx.azuredatabricks.net"    # macOS/Linux: export DATABRICKS_HOST="adb-xxxx.azuredatabricks.net"
$env:DATABRICKS_HTTP_PATH="/sql/1.0/warehouses/xxxx"   # macOS/Linux: export DATABRICKS_HTTP_PATH="/sql/1.0/warehouses/xxxx"
$env:DATABRICKS_TOKEN="dapi..."                        # macOS/Linux: export DATABRICKS_TOKEN="dapi..."

$env:APP_ENV="dev"                         # macOS/Linux: export APP_ENV=dev   (reads hrb_dev)
hr-analytics
```

> If activating the venv fails on Windows with a script-execution error, run once in
> the same terminal: `Set-ExecutionPolicy -Scope Process -Bypass`

## Test (no Databricks needed)

```powershell
ruff check src tests                       # same on both
pytest -v                                  # same on both
```

## CI/CD

- **CI** (`.github/workflows/ci.yml`) runs on every pull request: lint + unit tests.
- **CD** (`.github/workflows/cd.yml`) runs on merge to `main`: run against
  dev automatically, then UAT and prod behind manual approval gates.

Both workflows run on GitHub's **Linux** runners (`runs-on: ubuntu-latest`),
so they're the same no matter whether you develop on Windows or macOS.
