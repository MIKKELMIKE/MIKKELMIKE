#!/usr/bin/env python3
"""Dos hojas: portada en blanco y una tabla de conceptos. El único color es el logo UTNA."""

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
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
OUT = ROOT / "Portada_y_tabla_LLM.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")

PAGE_W, PAGE_H = letter


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Sans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))


def styles() -> dict[str, ParagraphStyle]:
    return {
        "school": ParagraphStyle(
            "School",
            fontName="Sans",
            fontSize=10,
            leading=13,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "Title",
            fontName="Sans-Bold",
            fontSize=16,
            leading=20,
            textColor=black,
            alignment=TA_CENTER,
            spaceBefore=16,
            spaceAfter=4,
        ),
        "subject": ParagraphStyle(
            "Subject",
            fontName="Sans",
            fontSize=12,
            leading=15,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "meta": ParagraphStyle(
            "Meta",
            fontName="Sans",
            fontSize=12,
            leading=18,
            textColor=black,
            alignment=TA_CENTER,
        ),
        "sheet_title": ParagraphStyle(
            "SheetTitle",
            fontName="Sans-Bold",
            fontSize=14,
            leading=18,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "sheet_sub": ParagraphStyle(
            "SheetSub",
            fontName="Sans",
            fontSize=10,
            leading=13,
            textColor=black,
            alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "th": ParagraphStyle(
            "Th",
            fontName="Sans-Bold",
            fontSize=12,
            leading=15,
            textColor=black,
            alignment=TA_LEFT,
        ),
        "name": ParagraphStyle(
            "Name",
            fontName="Sans-Bold",
            fontSize=12,
            leading=15,
            textColor=black,
        ),
        "td": ParagraphStyle(
            "Td",
            fontName="Sans",
            fontSize=12,
            leading=15,
            textColor=black,
        ),
    }


def concepts_table(s: dict[str, ParagraphStyle]) -> Table:
    headers = ["Concepto", "Palabra en español", "Qué quiere decir"]
    rows = [
        [
            "Token",
            "Pedazo de texto",
            "Parte el texto en pedazos para que el modelo pueda leerlo. Un pedazo puede ser una palabra, un trozo o un signo.",
        ],
        [
            "Embedding",
            "Vector",
            "Convierte cada pedazo en números que guardan su significado. Palabras parecidas, como perro y gato, quedan cerca.",
        ],
        [
            "Transformer",
            "Transformador",
            "Es la estructura del modelo. Relaciona las partes del texto entre sí, en lugar de leerlas solo una por una.",
        ],
        [
            "Encoder",
            "Codificador",
            "Es la parte que lee toda la entrada y entiende de qué trata. No se encarga de escribir la respuesta.",
        ],
        [
            "Decoder",
            "Decodificador",
            "Es la parte que escribe la respuesta, pedazo por pedazo. Solo puede ver lo que ya escribió.",
        ],
        [
            "Attention",
            "Atención",
            "Decide qué palabras mirar más en cada momento. En «la llave del carro», al leer «llave» se fija en «carro».",
        ],
        [
            "Fine-Tuning",
            "Ajuste fino",
            "Es entrenar un poco más un modelo que ya sabe, con ejemplos de una tarea. No es lo mismo que solo ponerle una instrucción.",
        ],
    ]
    data = [[Paragraph(header, s["th"]) for header in headers]]
    for concept, word, meaning in rows:
        data.append(
            [
                Paragraph(concept, s["name"]),
                Paragraph(word, s["name"]),
                Paragraph(meaning, s["td"]),
            ]
        )
    table = Table(data, colWidths=[110, 150, 268])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), white),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 14),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
                ("LINEABOVE", (0, 0), (-1, 0), 1, black),
                ("LINEBELOW", (0, 0), (-1, 0), 1, black),
                ("LINEBELOW", (0, 1), (-1, -2), 0.4, black),
                ("LINEBELOW", (0, -1), (-1, -1), 1, black),
            ]
        )
    )
    return table


def build_story(s: dict[str, ParagraphStyle]) -> list:
    logo = Image(
        str(ASSETS / "logo-utna.png"),
        width=210,
        height=210 * (126 / 350),
        mask="auto",
    )
    logo.hAlign = "CENTER"
    return [
        Spacer(1, 150),
        logo,
        Spacer(1, 14),
        Paragraph("UNIVERSIDAD TECNOLÓGICA DEL NORTE DE AGUASCALIENTES", s["school"]),
        Paragraph("Rincón de Romos, Aguascalientes", s["school"]),
        Paragraph("Conceptos relacionados con LLM", s["title"]),
        Paragraph("Fundamentos de Inteligencia Artificial", s["subject"]),
        Paragraph("Alumno: Sergio Michell Carreón López", s["meta"]),
        Paragraph("Docente: Mtro. Gerardo Martínez", s["meta"]),
        Paragraph("Grupo: 7A", s["meta"]),
        Paragraph("Carrera: ITIID", s["meta"]),
        Paragraph("6 de octubre de 2026", s["meta"]),
        PageBreak(),
        Spacer(1, 28),
        Paragraph("Conceptos relacionados con LLM", s["sheet_title"]),
        Paragraph("Sergio Michell Carreón López · Grupo 7A", s["sheet_sub"]),
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
        topMargin=36,
        bottomMargin=36,
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
