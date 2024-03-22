# DVC
## Setup
```bash
# Create an S3 bucket
aws s3api create-bucket --bucket legal-colombia --region us-east-1

# Initialize DVC
dvc init

# Configure S3 remote storage
dvc remote add -d s3-remote s3://legal-colombia/

# Commit changes to Git
dvc add data/

# Commit changes to Git
git add .gitignore data.dvc
git commit -m "Add data directory to DVC tracking"

# Push data to S3 remote storage
dvc push

# Commit and push changes to Git
git add data.dvc
git commit -m "Update DVC file with S3 remote storage"
git push
```
## Downloading files
```bash
# Pull the data files from the S3 bucket
dvc pull
```

# Scraping Codes
## Constitución Política de la República de Colombia
#### Get .htmls
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
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/constitucion/html --output_path ./data/constitucion/text
```

## Código Penal - LEY 599 DE 2000
#### Get .htmls
```python
python scripts/scraper.py --output_path ./data/codigo_penal/html \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr001.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr002.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr003.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr004.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr005.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr006.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr007.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr008.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr009.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr010.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr011.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr013.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr014.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr015.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr016.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr017.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr018.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_0599_2000_pr019.html"
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_penal/html --output_path ./data/codigo_penal/text
```


## Código General del Proceso - LEY 1564 DE 2012
#### Get .htmls
```python
python scripts/scraper.py --output_path ./data/codigo_general_del_proceso/html \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr001.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr002.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr003.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr004.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr005.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr006.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr007.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr008.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr009.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr010.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr011.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr013.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr014.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/ley_1564_2012_pr015.html" 
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_general_del_proceso/html --output_path ./data/codigo_general_del_proceso/text
```


## Código Civil - LEY 84 DE 1873
#### Get .htmls
```python 
python scripts/scraper.py --output_path ./data/codigo_civil/html \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr001.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr002.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr003.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr004.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr005.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr006.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr007.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr008.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr009.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr010.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr011.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr013.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr014.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr015.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr016.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr017.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr018.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr019.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr020.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr021.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr022.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr023.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr024.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr025.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr026.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr027.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr028.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr029.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr030.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr031.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr032.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr033.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr034.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr035.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr036.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr037.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr038.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr039.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr040.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr041.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr042.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr043.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr044.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr045.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr046.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr047.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr048.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr049.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr050.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr051.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr052.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr053.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr054.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr055.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr056.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr057.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr058.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr059.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr060.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr061.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr062.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr063.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr064.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr065.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr066.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr067.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr068.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr069.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr070.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr071.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr072.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr073.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr074.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr075.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr076.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr077.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr078.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr079.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr080.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr081.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr082.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_civil_pr083.html"
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_civil/html --output_path ./data/codigo_civil/text
```

## Código Sustantivo del Trabajo
#### Get .htmls
```python
python scripts/scraper.py --output_path ./data/codigo_sustantivo_trabajo/html \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr001.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr002.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr003.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr004.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr005.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr006.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr007.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr008.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr009.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr010.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr011.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr012.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr013.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr014.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr015.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr016.html" \
    --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr017.html" 
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_sustantivo_trabajo/html --output_path ./data/codigo_sustantivo_trabajo/text
```

## Codigo Procesal Laboral
#### Get .htmls
```python
python scripts/scraper.py --output_path ./data/codigo_procedimental_laboral/html \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_procedimental_laboral.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_procedimental_laboral_pr001.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_procedimental_laboral_pr002.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_procedimental_laboral_pr003.html" 
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_procedimental_laboral/html --output_path ./data/codigo_procedimental_laboral/text
```

##  Código de Comercio
#### Get .htmls
```python
python scripts/scraper.py --output_path ./data/codigo_comercio/html \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr001.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr002.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr003.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr004.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr005.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr006.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr007.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr008.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr009.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr010.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr011.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr012.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr013.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr014.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr015.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr016.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr017.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr018.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr019.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr020.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr021.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr022.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr023.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr024.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr025.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr026.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr027.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr028.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr029.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr030.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr031.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr032.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr033.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr034.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr035.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr036.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr037.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr038.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr039.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr040.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr041.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr042.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr043.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr044.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr045.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr046.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr047.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr048.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr049.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr050.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr051.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr052.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr053.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr054.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr055.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr056.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr057.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr058.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr059.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr060.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr061.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr062.html" \
   --webpage "http://www.secretariasenado.gov.co/senado/basedoc/codigo_comercio_pr063.html" 
```
#### Transform .htmls to cleaned .txts
```python
python scripts/html-to-txt.py --input_path ./data/codigo_comercio/html --output_path ./data/codigo_comercio/text
```