import json

def generate_html_report(data):

    # Inicia el contenido del informe HTML
    html_report = '''
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { text-align: center; }
            table { width: 80%; margin: auto; border-collapse: collapse; }
            th, td { padding: 12px; text-align: left; border: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            tr:hover { background-color: #f5f5f5; }
        </style>
        <title>Informe de Mantenibilidad</title>
    </head>
    <body>
        <h1>Informe de Mantenibilidad</h1>
        <table>
            <tr>
                <th>Archivo</th>
                <th>Mantenibilidad (%)</th>
                <th>Rango</th>
            </tr>
    '''

    # Agrega filas al informe HTML
    for key, value in data.items():
        html_report += f'''
            <tr>
                <td>{key}</td>
                <td>{value["mi"]}</td>
                <td>{value["rank"]}</td>
            </tr>
    '''
    # Finaliza el informe HTML
    html_report += '''
        </table>
    </body>
    </html>
    '''

    return html_report

with open('informe_mantenibilidad.json', 'r') as file:
    informe_json = json.load(file)

# Genera el informe HTML
html_report = generate_html_report(informe_json)

# Guarda el informe HTML en un archivo
with open('informe_mantenibilidad.html', 'w') as html_file:
    html_file.write(html_report)
