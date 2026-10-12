"""Genera un dataset academico y ficticio de opiniones de clientes.

No contiene comentarios reales ni datos personales. Es determinista.
"""
from pathlib import Path
import csv

POSITIVOS = [
    ("Me atendieron muy r\u00e1pido y con mucha amabilidad.", "atencion"),
    ("El pedido lleg\u00f3 completo y antes de la hora prevista.", "entrega"),
    ("Las promociones de hoy me ayudaron a ahorrar.", "promociones"),
    ("Encontr\u00e9 todos los productos que necesitaba.", "inventario"),
    ("La aplicaci\u00f3n es sencilla y pude pagar sin problemas.", "app"),
    ("La cajera fue muy amable durante toda la compra.", "atencion"),
    ("Los productos frescos llegaron en excelente estado.", "entrega"),
    ("Me gust\u00f3 que respetaran el descuento anunciado.", "promociones"),
    ("Hab\u00eda suficiente mercanc\u00eda y todo estaba ordenado.", "inventario"),
    ("El chatbot resolvi\u00f3 mi duda en pocos segundos.", "atencion"),
    ("Recib\u00ed mi compra a tiempo y bien empacada.", "entrega"),
    ("Los precios fueron mejores de lo que esperaba.", "precios"),
    ("Fue f\u00e1cil encontrar la leche y el pan en la tienda.", "inventario"),
    ("La p\u00e1gina carg\u00f3 r\u00e1pido y termin\u00e9 mi compra.", "app"),
    ("El personal me explic\u00f3 con paciencia c\u00f3mo facturar.", "atencion"),
    ("Me encant\u00f3 la calidad de las frutas que recib\u00ed.", "entrega"),
    ("El cup\u00f3n funcion\u00f3 y obtuve un buen descuento.", "promociones"),
    ("La tienda estaba limpia y la atenci\u00f3n fue excelente.", "atencion"),
    ("El seguimiento del pedido fue claro y muy \u00fatil.", "app"),
    ("Estoy satisfecho con el servicio y volver\u00e9 a comprar.", "atencion"),
]
NEGATIVOS = [
    ("Mi pedido lleg\u00f3 incompleto y no me dieron soluci\u00f3n.", "entrega"),
    ("La aplicaci\u00f3n se cerr\u00f3 justo cuando iba a pagar.", "app"),
    ("La promoci\u00f3n anunciada no se respet\u00f3 en caja.", "promociones"),
    ("El producto estaba caducado y tuve que devolverlo.", "inventario"),
    ("Esper\u00e9 demasiado para recibir ayuda del personal.", "atencion"),
    ("Hab\u00eda mucha fila y solo una caja estaba abierta.", "atencion"),
    ("El repartidor lleg\u00f3 muy tarde y sin avisar.", "entrega"),
    ("Me cobraron dos veces el mismo art\u00edculo.", "precios"),
    ("El sistema dec\u00eda disponible pero no hab\u00eda producto.", "inventario"),
    ("La devoluci\u00f3n fue complicada y tardaron en atenderme.", "atencion"),
    ("El chatbot no entendi\u00f3 mi pregunta y respondi\u00f3 mal.", "atencion"),
    ("La atenci\u00f3n por tel\u00e9fono fue muy mala.", "atencion"),
    ("Los precios del anaquel no coincidieron con el cobro.", "precios"),
    ("Me enviaron un producto equivocado en mi pedido.", "entrega"),
    ("No me avisaron que hab\u00edan cambiado el horario.", "atencion"),
    ("La entrega se retras\u00f3 por segunda ocasi\u00f3n.", "entrega"),
    ("La p\u00e1gina no me dej\u00f3 finalizar la compra.", "app"),
    ("Un empleado fue grosero cuando ped\u00ed informaci\u00f3n.", "atencion"),
    ("El cup\u00f3n nunca funcion\u00f3 y perd\u00ed el descuento.", "promociones"),
    ("Las verduras llegaron da\u00f1adas y no pude usarlas.", "entrega"),
]
NEUTROS = [
    ("Quiero saber a qu\u00e9 hora abre la tienda.", "atencion"),
    ("\u00bfD\u00f3nde puedo consultar las promociones vigentes?", "promociones"),
    ("Mi pedido est\u00e1 programado para ma\u00f1ana.", "entrega"),
    ("Necesito solicitar la factura de mi compra.", "atencion"),
    ("\u00bfTienen servicio a domicilio en mi zona?", "entrega"),
    ("El horario publicado es de nueve de la ma\u00f1ana a ocho.", "atencion"),
    ("Quisiera saber si tienen arroz disponible.", "inventario"),
    ("El paquete aparece como en preparaci\u00f3n.", "entrega"),
    ("\u00bfCu\u00e1l es la pol\u00edtica de devoluciones?", "atencion"),
    ("La tienda est\u00e1 cerca de la avenida principal.", "atencion"),
    ("El costo de env\u00edo aparece en el resumen.", "precios"),
    ("\u00bfPuedo cambiar la fecha de entrega?", "entrega"),
    ("El pago se registr\u00f3 con tarjeta de d\u00e9bito.", "precios"),
    ("Quisiera informaci\u00f3n sobre la tarjeta de puntos.", "promociones"),
    ("El chatbot me mostr\u00f3 las opciones de ayuda.", "atencion"),
    ("La promoci\u00f3n termina el domingo por la noche.", "promociones"),
    ("Recib\u00ed un mensaje con el n\u00famero de pedido.", "entrega"),
    ("\u00bfEn qu\u00e9 pasillo est\u00e1n los cereales?", "inventario"),
    ("El servicio de atenci\u00f3n est\u00e1 disponible en la p\u00e1gina.", "atencion"),
    ("Necesito actualizar la direcci\u00f3n de entrega.", "entrega"),
]


def generar_filas():
    filas = []
    n = 1
    for etiqueta, grupo in [("POS", POSITIVOS), ("NEG", NEGATIVOS), ("NEU", NEUTROS)]:
        for texto, tema in grupo:
            filas.append({
                "id": f"C{n:03d}",
                "texto": texto,
                "etiqueta": etiqueta,
                "tema": tema,
                "origen": "simulado",
            })
            n += 1
    return filas


def guardar_csv(destino=None):
    if destino is None:
        destino = Path(__file__).resolve().parents[1] / "data" / "comentarios_clientes.csv"
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["id", "texto", "etiqueta", "tema", "origen"])
        escritor.writeheader()
        escritor.writerows(generar_filas())
    return destino


if __name__ == "__main__":
    ruta = guardar_csv()
    print(f"Dataset generado: {ruta} ({len(generar_filas())} filas)")
