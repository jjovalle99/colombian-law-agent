#### Constitucion
```python
python scripts/scraper.py --output_path ./data/constitucion/html \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr001.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr002.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr003.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr004.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr005.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr006.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr007.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr008.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr009.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr010.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr011.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr013.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr014.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/constitucion_politica_1991_pr015.html"
```

```python
python scripts/html-to-txt.py --input_path ./data/constitucion/html --output_path ./data/constitucion/text

```