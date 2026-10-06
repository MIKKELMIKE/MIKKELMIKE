#!/usr/bin/env python3
"""Hoja simple de conceptos de LLM. Fondo blanco; el único color es el logo UTNA."""

from pathlib import Path

from reportlab.lib.colors import black, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
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

PAGE_W, PAGE_H = letter
INK = black
RULE = black


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Sans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))


def styles() -> dict[str, ParagraphStyle]:
    return {
        "school": ParagraphStyle(
            "School",
            fontName="Sans",
            fontSize=9,
            leading=12,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=1,
        ),
        "title": ParagraphStyle(
            "Title",
            fontName="Sans-Bold",
            fontSize=14,
            leading=17,
            textColor=INK,
            alignment=TA_CENTER,
            spaceBefore=8,
            spaceAfter=2,
        ),
        "subject": ParagraphStyle(
            "Subject",
            fontName="Sans",
            fontSize=11,
            leading=14,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "meta": ParagraphStyle(
            "Meta",
            fontName="Sans",
            fontSize=10,
            leading=13,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=1,
        ),
        "intro": ParagraphStyle(
            "Intro",
            fontName="Sans",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
            alignment=TA_LEFT,
            spaceBefore=8,
            spaceAfter=8,
        ),
        "th": ParagraphStyle(
            "Th",
            fontName="Sans-Bold",
            fontSize=10,
            leading=13,
            textColor=INK,
            alignment=TA_LEFT,
        ),
        "name": ParagraphStyle(
            "Name",
            fontName="Sans-Bold",
            fontSize=10,
            leading=13,
            textColor=INK,
        ),
        "td": ParagraphStyle(
            "Td",
            fontName="Sans",
            fontSize=10,
            leading=13,
            textColor=INK,
        ),
    }


def concepts_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Concepto", "En español", "Qué es"]
    rows = [
        [
            "Token",
            "Pedazo de texto",
            "Parte el texto en pedazos para que el modelo lo lea. Puede ser una palabra, un trozo o un signo. «Jugando» a veces queda como «jug» y «ando».",
        ],
        [
            "Embedding",
            "Vector",
            "Convierte cada pedazo en números que guardan su significado. «Perro» y «gato» quedan cerca. «Perro» y «teclado» quedan lejos.",
        ],
        [
            "Transformer",
            "Transformador",
            "Es la estructura del modelo. Relaciona las partes del texto entre sí, en lugar de leerlas solo una por una.",
        ],
        [
            "Encoder",
            "Codificador",
            "Lee toda la entrada y arma lo que significa. BERT trabaja así. Sirve para entender o clasificar, no para escribir la respuesta.",
        ],
        [
            "Decoder",
            "Decodificador",
            "Escribe la respuesta pedazo por pedazo. GPT trabaja así. Solo puede ver lo que ya escribió.",
        ],
        [
            "Attention",
            "Atención",
            "Decide qué palabras mirar más. En «la llave del carro», al leer «llave» se fija en «carro» para saber de cuál se habla.",
        ],
        [
            "Fine-Tuning",
            "Ajuste fino",
            "Se entrena un poco más un modelo que ya sabe, con ejemplos de una tarea. No es lo mismo que solo ponerle una instrucción.",
        ],
    ]
    data = [[Paragraph(header, s["th"]) for header in headers]]
    for concept, spanish, meaning in rows:
        data.append(
            [
                Paragraph(concept, s["name"]),
                Paragraph(spanish, s["name"]),
                Paragraph(meaning, s["td"]),
            ]
        )
    table = Table(data, colWidths=[88, 108, 326])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), white),
                ("TEXTCOLOR", (0, 0), (-1, -1), INK),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("LINEBELOW", (0, 0), (-1, 0), 1, RULE),
                ("LINEBELOW", (0, 1), (-1, -2), 0.3, RULE),
                ("LINEBELOW", (0, -1), (-1, -1), 0.6, RULE),
                ("LINEABOVE", (0, 0), (-1, 0), 0.6, RULE),
            ]
        )
    )
    return table


def build_story(s: dict[str, ParagraphStyle]) -> list:
    logo = Image(
        str(ASSETS / "logo-utna.png"),
        width=188,
        height=188 * (126 / 350),
        mask="auto",
    )
    logo.hAlign = "CENTER"
    return [
        Spacer(1, 6),
        logo,
        Spacer(1, 8),
        Paragraph("UNIVERSIDAD TECNOLÓGICA DEL NORTE DE AGUASCALIENTES", s["school"]),
        Paragraph("Rincón de Romos, Aguascalientes", s["school"]),
        Paragraph("Conceptos relacionados con LLM", s["title"]),
        Paragraph("Fundamentos de Inteligencia Artificial", s["subject"]),
        Paragraph("Alumno: Sergio Michell Carreón López", s["meta"]),
        Paragraph("Docente: Mtro. Gerardo Martínez", s["meta"]),
        Paragraph("Grupo 7A · Carrera ITIID · 6 de octubre de 2026", s["meta"]),
        Paragraph(
            "Un LLM es un programa que aprendió con mucho texto y puede contestar o redactar. "
            "En la tabla están los conceptos de la clase, el nombre en español y qué hace cada uno.",
            s["intro"],
        ),
        concepts_table(s),
    ]


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
        leftMargin=42,
        rightMargin=42,
        topMargin=32,
        bottomMargin=32,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        PAGE_W - doc.leftMargin - doc.rightMargin,
        PAGE_H - doc.topMargin - doc.bottomMargin,
        id="sheet",
        showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="sheet", frames=[frame])])
    doc.build(build_story(s))
    print(OUT)


if __name__ == "__main__":
    main()
