# app-runner-test

## Run Locally

```bash
../venv/bin/python -m pip install -r requirements.txt
PORT=8080 ../venv/bin/python server.py
```

## Run In Production Style

```bash
../venv/bin/python -m pip install -r requirements.txt
PORT=8080 ../venv/bin/gunicorn --bind 0.0.0.0:${PORT} server:app
```
