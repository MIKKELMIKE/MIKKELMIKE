#!/usr/bin/env python3
"""Investigación de conceptos de LLM para Fundamentos de Inteligencia Artificial."""

from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "Conceptos_LLM_Fundamentos_IA.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")

GREEN_DARK = HexColor("#1B4D32")
GREEN = HexColor("#246041")
GOLD = HexColor("#C4892A")
GOLD_DARK = HexColor("#8C5E12")
INK = HexColor("#1C1C1C")
MUTED = HexColor("#5C564C")
CREAM = HexColor("#F7F3EA")
LINE = HexColor("#E3D9C8")
PANEL = HexColor("#FBF8F2")

PAGE_W, PAGE_H = letter


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("LibSans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif", str(FONT_DIR / "LiberationSerif-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Bold", str(FONT_DIR / "LiberationSerif-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Italic", str(FONT_DIR / "LiberationSerif-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-BoldItalic", str(FONT_DIR / "LiberationSerif-BoldItalic.ttf")))
    registerFontFamily(
        "LibSerif",
        normal="LibSerif",
        bold="LibSerif-Bold",
        italic="LibSerif-Italic",
        boldItalic="LibSerif-BoldItalic",
    )


def styles() -> dict[str, ParagraphStyle]:
    body = ParagraphStyle(
        "Body",
        fontName="LibSerif",
        fontSize=11.5,
        leading=16,
        textColor=INK,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    )
    return {
        "h1": ParagraphStyle(
            "H1",
            fontName="LibSerif-Bold",
            fontSize=16,
            leading=20,
            textColor=GREEN_DARK,
            spaceAfter=4,
        ),
        "lead": ParagraphStyle(
            "Lead",
            fontName="LibSerif-Italic",
            fontSize=10.5,
            leading=14,
            textColor=MUTED,
            spaceAfter=12,
        ),
        "sec": ParagraphStyle(
            "Sec",
            fontName="LibSans-Bold",
            fontSize=13,
            leading=16,
            textColor=GREEN_DARK,
            spaceBefore=2,
            spaceAfter=6,
        ),
        "body": body,
        "note": ParagraphStyle(
            "Note",
            fontName="LibSerif-Italic",
            fontSize=9.5,
            leading=12.5,
            textColor=MUTED,
            spaceBefore=3,
            spaceAfter=8,
        ),
        "th": ParagraphStyle(
            "Th",
            fontName="LibSans-Bold",
            fontSize=9,
            leading=12,
            textColor=white,
        ),
        "td_name": ParagraphStyle(
            "TdName",
            fontName="LibSans-Bold",
            fontSize=9.5,
            leading=12.5,
            textColor=GREEN_DARK,
        ),
        "td": ParagraphStyle(
            "Td",
            fontName="LibSerif",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
        ),
        "ref": ParagraphStyle(
            "Ref",
            fontName="LibSerif",
            fontSize=10,
            leading=13.5,
            textColor=INK,
            alignment=TA_LEFT,
            leftIndent=14,
            firstLineIndent=-14,
            spaceAfter=6,
        ),
        "step": ParagraphStyle(
            "Step",
            fontName="LibSerif",
            fontSize=11.5,
            leading=14.5,
            textColor=INK,
            spaceAfter=1,
        ),
    }


def draw_cover(canvas, doc) -> None:
    canvas.saveState()
    width, height = PAGE_W, PAGE_H

    canvas.setFillColor(GREEN_DARK)
    canvas.rect(0, height - 18, width, 18, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, height - 24, width, 6, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 18, width, 6, fill=1, stroke=0)
    canvas.setFillColor(GREEN_DARK)
    canvas.rect(0, 0, width, 18, fill=1, stroke=0)

    logo_w = 228
    logo_h = 228 * (126 / 350)
    logo = ImageReader(str(ASSETS / "logo-utna.png"))
    canvas.drawImage(
        logo,
        (width - logo_w) / 2,
        height - 118,
        logo_w,
        logo_h,
        mask="auto",
        preserveAspectRatio=True,
    )

    y = height - 138
    canvas.setFillColor(GREEN_DARK)
    canvas.setFont("LibSans-Bold", 10.5)
    canvas.drawCentredString(
        width / 2,
        y,
        "UNIVERSIDAD TECNOLÓGICA DEL NORTE DE AGUASCALIENTES",
    )
    y -= 15
    canvas.setFillColor(MUTED)
    canvas.setFont("LibSerif-Italic", 9.5)
    canvas.drawCentredString(width / 2, y, "Rincón de Romos, Aguascalientes")

    y -= 16
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.1)
    canvas.line(width / 2 - 78, y, width / 2 + 78, y)

    y -= 34
    canvas.setFillColor(GOLD_DARK)
    canvas.setFont("LibSans-Bold", 8.5)
    canvas.drawCentredString(width / 2, y, "ACTIVIDAD DE INVESTIGACIÓN")

    y -= 22
    canvas.setFillColor(GREEN_DARK)
    canvas.setFont("LibSerif-Bold", 18)
    canvas.drawCentredString(width / 2, y, "Conceptos relacionados con LLM")

    y -= 22
    canvas.setFillColor(GOLD_DARK)
    canvas.setFont("LibSans-Bold", 8)
    canvas.drawCentredString(width / 2, y, "ASIGNATURA")
    y -= 16
    canvas.setFillColor(INK)
    canvas.setFont("LibSerif", 12.5)
    canvas.drawCentredString(width / 2, y, "Fundamentos de Inteligencia Artificial")

    y -= 18
    canvas.setFillColor(MUTED)
    canvas.setFont("LibSerif-Italic", 9.5)
    canvas.drawCentredString(
        width / 2,
        y,
        "Token  ·  Embedding  ·  Transformer  ·  Encoder  ·  Decoder",
    )
    y -= 13
    canvas.drawCentredString(width / 2, y, "Attention  ·  Fine-Tuning")

    bloques = [
        ("ALUMNO", "Sergio Michell Carreón López"),
        ("DOCENTE", "Mtro. Gerardo Martínez"),
        ("GRUPO", "7A"),
        ("CARRERA", "ITIID"),
        ("FECHA DE ENTREGA", "6 de octubre de 2026"),
    ]
    panel_top = y - 28
    panel_bottom = 58
    panel_x = 118
    panel_w = width - 236
    canvas.setFillColor(PANEL)
    canvas.setStrokeColor(GREEN_DARK)
    canvas.setLineWidth(1.2)
    canvas.roundRect(panel_x, panel_bottom, panel_w, panel_top - panel_bottom, 8, fill=1, stroke=1)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.8)
    canvas.roundRect(
        panel_x + 5,
        panel_bottom + 5,
        panel_w - 10,
        panel_top - panel_bottom - 10,
        6,
        fill=0,
        stroke=1,
    )

    inner_top = panel_top - 26
    inner_bottom = panel_bottom + 22
    step = (inner_top - inner_bottom) / len(bloques)
    for index, (label, value) in enumerate(bloques):
        label_y = inner_top - index * step
        canvas.setFillColor(GREEN_DARK)
        canvas.setFont("LibSans-Bold", 8)
        canvas.drawCentredString(width / 2, label_y, label)
        canvas.setFillColor(INK)
        canvas.setFont("LibSerif", 12.5)
        canvas.drawCentredString(width / 2, label_y - 16, value)

    canvas.restoreState()


def draw_body(canvas, doc) -> None:
    canvas.saveState()
    width, height = PAGE_W, PAGE_H

    canvas.setFillColor(GREEN_DARK)
    canvas.rect(0, 0, 11, height, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(11, 0, 3.5, height, fill=1, stroke=0)

    canvas.setFillColor(GREEN_DARK)
    canvas.setFont("LibSans", 8.5)
    canvas.drawString(56, height - 34, "Fundamentos de Inteligencia Artificial")
    canvas.setFillColor(MUTED)
    canvas.drawRightString(width - 46, height - 34, "Conceptos relacionados con LLM")
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1.15)
    canvas.line(56, height - 42, width - 46, height - 42)

    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(56, 36, width - 46, 36)
    canvas.setFillColor(MUTED)
    canvas.setFont("LibSans", 8)
    canvas.drawString(56, 22, "Sergio Michell Carreón López   ·   ITIID   ·   Grupo 7A")
    canvas.setFillColor(GREEN_DARK)
    canvas.setFont("LibSans-Bold", 9)
    canvas.drawRightString(width - 46, 22, str(canvas.getPageNumber()))
    canvas.restoreState()


def glossary_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Concepto", "En español", "Qué hace"]
    rows = [
        ["Token", "Pedazo de texto", "Parte el texto en unidades que el modelo puede leer. No siempre es una palabra completa."],
        ["Embedding", "Vector o incrustación", "Convierte cada token en una lista de números que representa su significado."],
        ["Transformer", "Transformador", "Es la arquitectura, el diseño de red, con el que están hechos los LLM actuales."],
        ["Encoder", "Codificador", "Lee la entrada completa y arma una representación de lo que el texto quiere decir."],
        ["Decoder", "Decodificador", "Genera la respuesta de un token a la vez."],
        ["Attention", "Atención", "Decide qué partes del texto pesan más en cada momento."],
        ["Fine-Tuning", "Ajuste fino", "Sigue entrenando un modelo que ya sabe, para dejarlo mejor en una tarea concreta."],
    ]
    data = [[Paragraph(h, s["th"]) for h in headers]]
    for row in rows:
        data.append(
            [
                Paragraph(row[0], s["td_name"]),
                Paragraph(row[1], s["td_name"]),
                Paragraph(row[2], s["td"]),
            ]
        )
    table = Table(data, colWidths=[88, 118, 300], repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_DARK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, GREEN_DARK),
    ]
    for index in range(1, len(data)):
        if index % 2 == 1:
            commands.append(("BACKGROUND", (0, index), (-1, index), CREAM))
        else:
            commands.append(("BACKGROUND", (0, index), (-1, index), white))
    table.setStyle(TableStyle(commands))
    return table


def model_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Tipo de modelo", "Qué parte usa", "Ejemplo", "Para qué sirve más"]
    rows = [
        ["Solo encoder", "Encoder", "BERT", "Entender, clasificar o buscar en un texto."],
        ["Solo decoder", "Decoder", "GPT", "Redactar, conversar y completar texto."],
        ["Encoder y decoder", "Las dos", "T5 y el Transformer de traducción", "Pasar de un texto a otro, como traducir."],
    ]
    data = [[Paragraph(h, s["th"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(cell, s["td"] if i else s["td_name"]) for i, cell in enumerate(row)])
    table = Table(data, colWidths=[100, 78, 150, 178], repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_DARK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, GREEN_DARK),
    ]
    for index in range(1, len(data)):
        color = CREAM if index % 2 == 1 else white
        commands.append(("BACKGROUND", (0, index), (-1, index), color))
    table.setStyle(TableStyle(commands))
    return table


def quiz_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Si preguntan esto", "Concepto", "En español"]
    rows = [
        ["En qué pedazos se parte el texto", "Token", "Pedazo de texto"],
        ["Cómo se guarda el significado con números", "Embedding", "Vector o incrustación"],
        ["Cuál es el diseño de la red", "Transformer", "Transformador"],
        ["Qué parte lee la entrada", "Encoder", "Codificador"],
        ["Qué parte escribe la respuesta", "Decoder", "Decodificador"],
        ["Cómo se decide qué palabras mirar", "Attention", "Atención"],
        ["Cómo se especializa en una tarea", "Fine-Tuning", "Ajuste fino"],
    ]
    data = [[Paragraph(header, s["th"]) for header in headers]]
    for row in rows:
        data.append(
            [
                Paragraph(row[0], s["td"]),
                Paragraph(row[1], s["td_name"]),
                Paragraph(row[2], s["td_name"]),
            ]
        )
    table = Table(data, colWidths=[250, 110, 146], repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_DARK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, GREEN_DARK),
    ]
    for index in range(1, len(data)):
        color = CREAM if index % 2 == 1 else white
        commands.append(("BACKGROUND", (0, index), (-1, index), color))
    table.setStyle(TableStyle(commands))
    return table


def attention_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Palabra", "Cuánta atención recibe", "Por qué"]
    rows = [
        ["carro", "Alta", "Aclara que se habla de la llave del carro."],
        ["mesa", "Alta", "Dice el lugar donde se quedó."],
        ["sobre", "Media", "Une la llave con el lugar."],
        ["Dejé", "Baja", "Dice la acción, pero no de qué llave se trata."],
    ]
    data = [[Paragraph(h, s["th"]) for h in headers]]
    for row in rows:
        data.append(
            [
                Paragraph(row[0], s["td_name"]),
                Paragraph(row[1], s["td"]),
                Paragraph(row[2], s["td"]),
            ]
        )
    table = Table(data, colWidths=[80, 130, 296], repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_DARK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 1.5, GOLD),
        ("LINEBELOW", (0, 1), (-1, -2), 0.3, LINE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, GREEN_DARK),
    ]
    for index in range(1, len(data)):
        color = CREAM if index % 2 == 1 else white
        commands.append(("BACKGROUND", (0, index), (-1, index), color))
    table.setStyle(TableStyle(commands))
    return table


def section(title: str, paragraphs: list[str], s: dict[str, ParagraphStyle]) -> list:
    flow = [Paragraph(title, s["sec"])]
    flow.extend(Paragraph(text, s["body"]) for text in paragraphs)
    return flow


def build_story(s: dict[str, ParagraphStyle]) -> list:
    story: list = [
        Spacer(1, 1),
        NextPageTemplate("body"),
        PageBreak(),
        Paragraph("Conceptos relacionados con LLM", s["h1"]),
        Paragraph(
            "Investigación de los conceptos vistos en clase · Fundamentos de Inteligencia Artificial",
            s["lead"],
        ),
        Paragraph(
            "Un LLM, por sus siglas en inglés <i>Large Language Model</i>, es un modelo de lenguaje grande. "
            "En palabras simples, es un programa que se entrenó leyendo muchísimo texto y con eso aprendió "
            "a completar ideas, contestar preguntas o redactar. Cuando usamos una herramienta como ChatGPT, "
            "detrás está este tipo de modelo.",
            s["body"],
        ),
        Paragraph(
            "En clase nos pidieron investigar siete conceptos que explican cómo trabaja: Token, Embedding, "
            "Transformer, Encoder, Decoder, Attention y Fine-Tuning. Aquí los explico con mis palabras y "
            "con un ejemplo. La tabla junta el nombre en inglés, cómo se dice en español y qué hace cada uno, "
            "porque si solo se memoriza el nombre es fácil confundirlos.",
            s["body"],
        ),
        Paragraph(
            "El recorrido se puede contar así. El texto se parte en pedazos, esos pedazos se vuelven números "
            "y entran a una arquitectura llamada Transformer. Adentro, la atención decide qué partes del texto "
            "pesan más. El encoder sirve para entender la entrada y el decoder para ir escribiendo la respuesta. "
            "El fine-tuning no ocurre en cada pregunta: es un ajuste previo para dejar el modelo mejor en una "
            "tarea concreta.",
            s["body"],
        ),
        Spacer(1, 4),
        glossary_table(s),
        Paragraph(
            "La tabla es el mapa del trabajo. En las siguientes páginas desarrollo cada renglón.",
            s["note"],
        ),
    ]

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "1. Token",
            [
                "El token es el pedazo de texto con el que el modelo trabaja. No siempre coincide con una "
                "palabra. A veces es una palabra completa, a veces es solo un trozo y a veces es un signo, "
                "como una coma o un signo de interrogación.",
                "El modelo no trae guardadas todas las palabras del idioma. Cuando se entrena, aprende pedazos "
                "que se repiten mucho y con esos pedazos arma las palabras. Por ejemplo, «jugando» puede quedar "
                "en dos partes, algo parecido a «jug» y «ando», porque «ando» sale en muchos verbos: cantando, "
                "caminando, estudiando.",
                "El programa que hace este corte se llama tokenizador. Si escribo «¿Qué es un token?», el modelo "
                "no se queda con la pregunta completa. La corta, y a cada pedazo le pone un número que solo sirve "
                "para identificarlo. Ese número todavía no guarda el significado. De eso se encarga el embedding.",
                "También existe un límite. Cada modelo acepta cierta cantidad de tokens al mismo tiempo; a eso "
                "se le llama ventana de contexto. Si el texto se pasa de esa ventana, el modelo ya no alcanza "
                "a verlo completo.",
            ],
            s,
        )
    )

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "2. Embedding",
            [
                "El embedding es la lista de números que representa a un token. Esa lista se llama vector. "
                "El número de identificación solo dice cuál token es. El embedding intenta guardar cómo se usa "
                "y, con eso, algo de su significado.",
                "Se entiende mejor con un mapa. Las palabras que aparecen en situaciones parecidas quedan cerca: "
                "«perro», «gato» y «mascota» estarían en la misma zona. «Perro» y «teclado» quedarían lejos. "
                "El mapa de un LLM no es de dos dimensiones. Un embedding puede tener cientos o miles de números, "
                "y la cercanía se calcula entre esas listas.",
                "Con eso el modelo puede hacer operaciones con el lenguaje. No entiende como una persona, pero "
                "sí compara tokens y usa esa comparación para calcular qué podría seguir en la frase.",
                "Hay un detalle más. El Transformer ve varios tokens al mismo tiempo, así que necesita el orden. "
                "Por eso al embedding se le suma la posición de cada token. Sin la posición, «Ana ve a Luis» "
                "y «Luis ve a Ana» se parecerían demasiado, aunque no dicen lo mismo.",
            ],
            s,
        )
    )

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "3. Transformer",
            [
                "El Transformer es la arquitectura del modelo, o sea el diseño de la red neuronal. No es una "
                "pieza aparte de las demás: es la estructura donde viven la atención, el encoder y el decoder. "
                "Lo propusieron Vaswani y sus colegas en 2017, en el artículo <i>Attention Is All You Need</i>.",
                "Los modelos anteriores leían el texto en fila, una palabra y después la otra. En una frase "
                "larga se les debilitaba lo que iba al principio. El Transformer trabaja de otra manera: relaciona "
                "las partes del texto usando atención y puede tomar en cuenta varios tokens a la vez.",
                "GPT y BERT están construidos como Transformers. No hacen el mismo trabajo, pero comparten esta "
                "arquitectura. La diferencia fuerte está en si usan encoder, decoder o los dos.",
                "Por dentro, el Transformer repite varias capas. En cada capa ocurre la atención y después una "
                "red pequeña que mezcla la información de cada token. Con más capas, el modelo arma relaciones "
                "más complicadas. Por ejemplo, descubre quién hizo la acción, o qué palabra está negando a otra "
                "aunque estén separadas.",
            ],
            s,
        )
    )

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "4. Encoder",
            [
                "El encoder es el codificador. Su trabajo es leer la entrada y convertirla en una representación "
                "de lo que el texto quiere decir. No se encarga de escribir la respuesta.",
                "Para hacerlo ve el texto completo en las dos direcciones. Cuando analiza una palabra puede "
                "fijarse en lo que va antes y también en lo que va después. Por eso se dice que es bidireccional.",
                "BERT es el ejemplo más conocido de un modelo que usa solo encoder (Devlin y colaboradores, 2019). "
                "Sirve para tareas de entender: clasificar si una opinión es positiva, buscar un párrafo parecido "
                "o señalar qué parte de un texto contesta una pregunta. No está pensado para ir armando una "
                "conversación token por token.",
            ],
            s,
        )
    )

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "5. Decoder",
            [
                "El decoder es el decodificador. Es la parte que escribe. Genera la salida de un token a la vez. "
                "En cada paso calcula qué tokens pueden seguir y elige uno de los más probables. Ese token se "
                "agrega al texto y el paso se repite.",
                "Hay una regla importante. Cuando va a predecir el siguiente token, el decoder no puede ver la "
                "respuesta que todavía no existe. Solo ve lo que ya escribió. Si el modelo también tiene encoder, "
                "además puede usar la representación de la entrada, por ejemplo la frase que hay que traducir.",
                "La familia GPT funciona principalmente como decoder. El modelo descrito por Brown y colaboradores "
                "(2020) es de ese tipo. Por eso una respuesta se va formando pedazo por pedazo, aunque en pantalla "
                "la veamos de corrido.",
                "No todos los LLM traen encoder y decoder juntos. Esta tabla los separa para no mezclar los nombres:",
            ],
            s,
        )
    )
    story.append(Spacer(1, 2))
    story.append(model_table(s))
    story.append(Spacer(1, 8))

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "6. Attention",
            [
                "Attention quiere decir atención. Es el mecanismo con el que el modelo decide qué partes del "
                "texto importan más en cada momento. No todas las palabras pesan igual, y ese peso lo calcula "
                "la red: nadie lo escribe a mano.",
                "Sirve un ejemplo. En la frase «Dejé la llave del carro sobre la mesa», cuando el modelo trabaja "
                "la palabra «llave» le conviene mirar «carro» y «mesa». Así sabe que se habla de la llave de un "
                "carro y del lugar donde quedó, no de una llave de agua. «Dejé» aporta la acción, pero ayuda menos "
                "a distinguir de qué llave se trata.",
                "Se puede imaginar como un reparto. Para un token, el modelo reparte su atención entre los demás. "
                "Los que aportan al sentido reciben más y los que casi no cambian la idea reciben muy poco.",
                "Esto no se hace una sola vez. El Transformer repite la atención en paralelo, y cada repetición "
                "se llama cabeza. Una cabeza puede fijarse en quién realiza la acción, otra en el objeto y otra "
                "en una palabra corta que cambia el sentido, como «no». Por eso una frase larga no se le desarma "
                "tan fácil.",
                "La atención no es un programa separado del Transformer. Va por dentro del encoder y también por "
                "dentro del decoder. La tabla de abajo es solo una ilustración de la frase de la llave. No son "
                "porcentajes sacados de un modelo real.",
            ],
            s,
        )
    )
    story.append(attention_table(s))
    story.append(
        Paragraph(
            "Ejemplo armado para explicar la idea, cuando el modelo está leyendo la palabra «llave».",
            s["note"],
        )
    )

    story.append(CondPageBreak(100))
    story.extend(
        section(
            "7. Fine-Tuning",
            [
                "Fine-tuning es el ajuste fino. Primero el modelo se entrena con una cantidad enorme de texto "
                "general. Esa etapa se llama preentrenamiento. Ahí aprende cómo se arma el idioma y también datos "
                "que venían en esos textos, pero todavía no queda especializado en un oficio.",
                "El fine-tuning consiste en seguir entrenándolo un rato más, ahora con ejemplos de una tarea "
                "concreta. Pueden ser preguntas y respuestas de un tema, o mensajes ya marcados como spam y no "
                "spam. Con esos ejemplos se ajustan sus valores internos para que responda mejor en ese trabajo. "
                "Ese entrenamiento extra es mucho más corto que hacerlo desde cero.",
                "No es lo mismo que escribirle una instrucción en el chat. La instrucción, el prompt, orienta una "
                "respuesta sin cambiar lo que el modelo ya trae aprendido. El fine-tuning sí modifica el modelo. "
                "Por eso necesita ejemplos y un entrenamiento, no solo un mensaje bien redactado.",
                "Una forma sencilla de recordarlo: el preentrenamiento le enseña a usar el lenguaje. El "
                "fine-tuning le enseña la tarea.",
            ],
            s,
        )
    )

    story.append(CondPageBreak(100))
    story.append(Paragraph("Cómo se conectan", s["sec"]))
    story.append(
        Paragraph(
            "Los siete conceptos se entienden mejor si se ven en orden. Hay que tener cuidado con una cosa: "
            "no todos son un paso que ocurra cada vez que hacemos una pregunta.",
            s["body"],
        )
    )
    steps = [
        "<b>1. Token.</b> El texto se corta en pedazos.",
        "<b>2. Embedding.</b> Cada pedazo se convierte en un vector y se le agrega su posición.",
        "<b>3. Transformer.</b> Esos vectores entran a la arquitectura del modelo.",
        "<b>4. Attention.</b> Adentro del Transformer se decide qué pedazos pesan más.",
        "<b>5. Encoder.</b> Si el modelo lo trae, lee toda la entrada y la representa.",
        "<b>6. Decoder.</b> Si el modelo lo trae, escribe la salida token por token.",
        "<b>7. Fine-Tuning.</b> No pasa en cada pregunta. Es el ajuste que ya se hizo antes, con ejemplos de la tarea.",
    ]
    story.extend(Paragraph(step, s["step"]) for step in steps)
    story.append(Spacer(1, 6))
    story.append(
        Paragraph(
            "GPT, por ejemplo, no usa encoder: trabaja con decoder. BERT hace lo contrario. El Transformer "
            "original, el de Vaswani y colaboradores (2017), sí usa las dos partes. El encoder lee la frase "
            "de origen y el decoder escribe la frase de salida, como en una traducción.",
            s["body"],
        )
    )

    story.append(CondPageBreak(90))
    story.append(Paragraph("Conclusión", s["sec"]))
    story.append(
        Paragraph(
            "Token y embedding preparan el texto para que una computadora pueda trabajar con él. El Transformer "
            "lo procesa, y la atención es la pieza que relaciona unas palabras con otras aunque no estén juntas. "
            "El encoder se orienta a entender la entrada y el decoder a producir la salida. El fine-tuning llega "
            "cuando ese modelo general se quiere dejar listo para un trabajo concreto.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Vistos de esta forma, los nombres dejan de estar sueltos. Cada concepto responde una pregunta "
            "distinta: en qué se parte el texto, cómo se vuelve números, qué arquitectura lo procesa, qué parte "
            "entiende, qué parte escribe, cómo elige a qué mirar y cómo se especializa.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "Para ubicarlos rápido, esta tabla va al revés: primero la idea y después el nombre.",
            s["body"],
        )
    )
    story.append(quiz_table(s))
    story.append(Spacer(1, 10))

    story.append(CondPageBreak(90))
    story.append(Paragraph("Referencias", s["sec"]))
    references = [
        "Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., … Amodei, D. (2020). <i>Language models are few-shot learners</i>. https://arxiv.org/abs/2005.14165",
        "Devlin, J., Chang, M.-W., Lee, K. y Toutanova, K. (2019). <i>BERT: Pre-training of deep bidirectional transformers for language understanding</i>. https://arxiv.org/abs/1810.04805",
        "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł. y Polosukhin, I. (2017). Attention is all you need. <i>Advances in Neural Information Processing Systems, 30</i>. https://arxiv.org/abs/1706.03762",
    ]
    story.extend(Paragraph(ref, s["ref"]) for ref in references)
    return story


def main() -> None:
    register_fonts()
    s = styles()
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=letter,
        title="Conceptos relacionados con LLM",
        author="Sergio Michell Carreón López",
        subject="Fundamentos de Inteligencia Artificial",
        creator="Sergio Michell Carreón López",
    )
    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover", showBoundary=0)
    body_frame = Frame(
        56,
        50,
        PAGE_W - 56 - 46,
        PAGE_H - 58 - 50,
        id="body",
        showBoundary=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="body", frames=[body_frame], onPage=draw_body),
        ]
    )
    doc.build(build_story(s))
    print(OUT)


if __name__ == "__main__":
    main()
