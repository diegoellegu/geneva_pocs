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
        <title>Informe de Complejidad Ciclomática</title>
    </head>
    <body>
        <h1>Informe de Complejidad Ciclomática</h1>
        <table>
            <tr>
                <th>Archivo</th>
                <th>Tipo</th>
                <th>Rango</th>
                <th>Complejidad</th>
                <th>Métodos</th>
            </tr>
    '''

    # Agrega filas al informe HTML
    for filename, class_info in data.items():
        for class_data in class_info:
            methods = [method.get("name", "") for method in class_data.get("methods", [])]
            html_report += f'''
                <tr>
                    <td>{filename}</td>
                    <td>{class_data["type"]}</td>
                    <td>{class_data["rank"]}</td>
                    <td>{class_data["complexity"]}</td>
                    <td>{", ".join(methods)}</td>
                </tr>
            '''

    # Finaliza el informe HTML
    html_report += '''
        </table>
    </body>
    </html>
    '''

    return html_report

# Lee el contenido del archivo JSON
with open('informe_cc.json', 'r') as file:
    informe_json = json.load(file)

# Genera el informe HTML
html_report = generate_html_report(informe_json)

# Guarda el informe HTML en un archivo
with open('informe_cc.html', 'w') as html_file:
    html_file.write(html_report)
