"""Funciones sencillas para comparar modelos de sentimiento."""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def normalizar_etiqueta(etiqueta):
    """Convierte etiquetas publicadas por los modelos a POS/NEG/NEU."""
    texto = str(etiqueta).strip().upper()
    equivalencias = {
        "POS": "POS", "POSITIVE": "POS", "POSITIVO": "POS",
        "NEG": "NEG", "NEGATIVE": "NEG", "NEGATIVO": "NEG",
        "NEU": "NEU", "NEUTRAL": "NEU", "NEUTRO": "NEU",
    }
    if texto not in equivalencias:
        raise ValueError(f"Etiqueta desconocida: {etiqueta}. Revisar config.json del modelo.")
    return equivalencias[texto]


def calcular_metricas(reales, predichas):
    etiquetas = ["NEG", "NEU", "POS"]
    return {
        "accuracy": float(accuracy_score(reales, predichas)),
        "precision_macro": float(precision_score(reales, predichas, labels=etiquetas, average="macro", zero_division=0)),
        "recall_macro": float(recall_score(reales, predichas, labels=etiquetas, average="macro", zero_division=0)),
        "f1_macro": float(f1_score(reales, predichas, labels=etiquetas, average="macro", zero_division=0)),
        "recall_neg": float(recall_score(reales, predichas, labels=["NEG"], average="macro", zero_division=0)),
    }
