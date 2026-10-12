# Actividad 4 - Modelos de sentimiento para Supermercados Miroslava

## 1. Descripcion

Prototipo academico de procesamiento de lenguaje natural (PLN) para clasificar comentarios ficticios de clientes como positivos (POS), negativos (NEG) o neutrales (NEU). Puede servir como apoyo a la atencion al cliente; no reemplaza a una persona ni toma decisiones sobre clientes reales.

## 2. Ecosistema Hugging Face

- **Models:** modelos preentrenados descargados desde https://huggingface.co/models
- **Datasets:** el CSV local se carga con la biblioteca `datasets`, documentada en https://huggingface.co/docs/datasets
- **Spaces:** aplicaciones demostrativas de modelos, disponibles en https://huggingface.co/spaces (no se necesita publicar un Space para esta actividad).

## 3. Modelos

1. `pysentimiento/robertuito-sentiment-analysis` (espanol).
2. `lxyuan/distilbert-base-multilingual-cased-sentiments-student` (multilingue, Apache-2.0).
3. `cardiffnlp/twitter-xlm-roberta-base-sentiment` (multilingue).

Se normalizan sus etiquetas a NEG/NEU/POS. La licencia de los modelos que no la declaran en su ficha debe revisarse antes de un uso comercial.

## 4. Entorno

Google Colab, preferentemente con GPU T4. Python 3, PyTorch y dependencias de `requirements.txt`. Se necesita Internet para descargar los modelos (aproximadamente 0.44, 0.54 y 1.11 GB de pesos, respectivamente). La GPU gratuita depende de disponibilidad.

## 5. Pasos de ejecucion en Google Colab

1. Entra a https://colab.research.google.com/ y abre `notebooks/Actividad4_Modelos_Miroslava.ipynb`.
2. Ve a **Entorno de ejecucion > Cambiar tipo de entorno de ejecucion > T4 GPU** (si aparece disponible).
3. Si deseas autenticarte, crea un token de lectura en https://huggingface.co/settings/tokens y guardalo en los secretos de Colab con nombre `HF_TOKEN`. Los modelos seleccionados son publicos y se pueden descargar sin token; el cuaderno incluye el paso de autenticacion.
4. Selecciona **Entorno de ejecucion > Ejecutar todas**. La primera vez se descargan los pesos de los modelos.
5. Al terminar, abre el enlace `resultados_colab.zip` que aparece al final y descargalo.
6. Revisa `results/metricas_modelos.csv` y el anexo Word generado. **No reportes cifras si no se ha ejecutado el notebook.**

## 6. Ejecucion local opcional

```bash
python -m pip install -r requirements.txt
python src/generar_dataset.py
python -m unittest discover -s tests -v
```

Las pruebas locales verifican el dataset y las funciones de metricas; la inferencia real de modelos se ejecuta en el notebook.

## 7. Archivos

- `notebooks/`: cuaderno de Colab.
- `data/`: dataset CSV y diccionario de campos.
- `src/`: script generador y calculo de metricas.
- `results/`: carpeta para resultados medidos.
- `tests/`: pruebas basicas.
- `requirements.txt`: dependencias.

## 8. Criterios y conclusion preliminar

Se compara accuracy, precision macro, recall macro, F1 macro, recall de la clase NEG, latencia por comentario y memoria GPU. Se recomienda provisionalmente probar primero DistilBERT por su licencia declarada y arquitectura compacta, pero **el modelo final se decide solo despues de medir resultados reales**. Se propone como minimo F1 macro >= 0.75, recall NEG >= 0.80 y latencia media <= 300 ms en GPU. Si no se cumple, no se recomienda desplegarlo.

El dataset es simulado y pequeno; las metricas sirven para practicar la comparacion, no para garantizar un desempeno comercial.

## 9. Fuentes

- https://huggingface.co/pysentimiento/robertuito-sentiment-analysis
- https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student
- https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment
- https://huggingface.co/docs/transformers/main_classes/pipelines
