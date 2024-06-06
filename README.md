# local-llm-demo

## Installation
### One-time pre-requisites

Support for OCR (pdfs)

```shell
brew install tesseract 
brew install poppler
```

### Python environment

```shell
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run UI

```shell
chainlit run web.py -w
```
