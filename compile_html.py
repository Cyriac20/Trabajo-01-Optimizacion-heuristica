import markdown
import re

def build_html():
    with open('Reporte_Final_Blog.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # Función para convertir carruseles en grids de CSS
    def parse_carousel(match):
        content = match.group(1)
        slides = content.split('<!-- slide -->')
        html = '<div class="gallery-grid">'
        for slide in slides:
            html += '<div class="gallery-item">\n' + slide.strip() + '\n</div>'
        html += '</div>'
        return html

    text = re.sub(r'````carousel\n(.*?)\n````', parse_carousel, text, flags=re.DOTALL)

    # Convertir a HTML
    html_content = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Corregir imágenes dentro de gallery-grid que no fueron convertidas por el parser de markdown
    # (markdown no procesa contenido dentro de bloques HTML de forma predeterminada)
    def fix_md_images(match):
        inner_content = match.group(1)
        # Reemplazar ![alt](url) por <img src="url" alt="alt">
        fixed = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', inner_content)
        return f'<div class="gallery-grid">{fixed}</div>'

    html_content = re.sub(r'<div class="gallery-grid">(.*?)</div>', fix_md_images, html_content, flags=re.DOTALL)

    # Estilo académico (Tipo "Paper" de investigación o Scientific Blog, fondo blanco, tabla estilo Booktabs)
    template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Técnico: Optimización Heurística</title>
    <!-- Google Fonts: Merriweather para aspecto académico, Inter para soporte de legibilidad -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #ffffff;
            --text-color: #222222;
            --accent-color: #1a4f8f; /* Un azul académico profundo */
            --border-color: #aaaaaa;
        }}

        body {{
            font-family: 'Merriweather', serif;
            background-color: #f7f9fa; /* Fondo externo */
            color: var(--text-color);
            line-height: 1.8;
            margin: 0;
            padding: 40px 20px;
            font-size: 16px;
        }}

        .container {{
            max-width: 850px;
            margin: 0 auto;
            background: var(--bg-color);
            padding: 70px 90px;
            border-radius: 4px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            border-top: 6px solid var(--accent-color);
        }}

        /* Typography */
        h1, h2, h3, h4 {{
            color: var(--accent-color);
            line-height: 1.3;
        }}

        h1 {{
            font-size: 2.2em;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 700;
        }}

        h2 {{
            font-size: 1.5em;
            margin-top: 50px;
            margin-bottom: 20px;
            border-bottom: 1px solid #dddddd;
            padding-bottom: 8px;
        }}

        h3 {{
            font-size: 1.25em;
            margin-top: 40px;
        }}

        p {{
            text-align: justify;
            margin-bottom: 20px;
        }}

        hr {{
            border: 0;
            height: 1px;
            background: #dddddd;
            margin: 40px 0;
        }}

        /* Tablas estilo LaTeX (Booktabs) */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 40px 0;
            font-family: 'Inter', sans-serif; /* Para legibilidad analítica */
            font-size: 0.9em;
        }}

        th, td {{
            padding: 12px 15px;
            text-align: left;
        }}

        table, th, td {{
            border: none;
        }}

        th {{
            border-top: 2px solid var(--text-color);
            border-bottom: 1px solid var(--text-color);
            font-weight: 600;
        }}

        tr:last-child td {{
            border-bottom: 2px solid var(--text-color);
        }}

        /* Images and Media */
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 40px auto 10px auto;
        }}

        .gallery-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
            margin: 40px 0;
        }}

        @media (min-width: 768px) {{
            .gallery-grid {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        .gallery-item img {{
            margin: 0;
            width: 100%;
            border: 1px solid #eeeeee;
        }}

        code {{
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9em;
        }}

        /* Print Styles: Imprime perfecto para PDFs */
        @media print {{
            body {{
                background-color: white;
                color: black;
                padding: 0;
                margin: 0;
            }}
            .container {{
                box-shadow: none;
                padding: 0;
                margin: 0;
                border-top: none;
            }}
            h1, h2, h3 {{ color: black; page-break-after: avoid; }}
            img {{ page-break-inside: avoid; }}
            table {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>"""

    with open('Reporte_Final_Blog.html', 'w', encoding='utf-8') as f:
        f.write(template)
    print("Reporte académico generado exitosamente.")

if __name__ == '__main__':
    build_html()
