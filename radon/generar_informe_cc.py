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
            canvas { max-width: 800px; margin: 20px auto; }
        </style>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation"></script>

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
            <div id="contenedorCanvas" style="overflow: auto; width: 100%; height: 500px;">
                    <canvas id="complexityChart"></canvas>
                </div>

        <script>
            document.getElementById('complexityChart').width = document.getElementById('contenedorCanvas').clientWidth;
            document.getElementById('complexityChart').height = document.getElementById('contenedorCanvas').clientHeight;
            // Datos para el gráfico
            var data = ''' + json.dumps(data) + ''';
            var filenames = Object.keys(data);
            var rutaBase = "/home/dparrilla/development/ude_proyecto_grado/geneva/";

            // Utiliza map para modificar cada elemento en el array filenames
            var labelsModificados = filenames.map(function (rutaCompleta) {
                // Reemplaza la parte específica de la ruta con una cadena vacía
                return rutaCompleta.replace(rutaBase, "");
            });
            var complexities = Object.values(data).map(classInfo => classInfo[0].complexity);

            // Configuración del gráfico
            var ctx = document.getElementById('complexityChart').getContext('2d');
              var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labelsModificados,
                    datasets: [{
                        label: 'Complejidad Ciclomática',
                        data: complexities,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    },
                    ]
                },
                 options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 21
                        }
                    },
                     plugins: { annotation: {
                        annotations: [{
                            type: 'line',
                            mode: 'horizontal',
                            scaleID: 'y',
                            value: 5,
                            borderColor: 'green',
                            borderWidth: 2,
                            label: {
                                content: 'Rango A',
                                enabled: true,
                                position: 'right'
                            }
                        },{
                            type: 'line',
                            mode: 'horizontal',
                            scaleID: 'y',
                            value: 10,
                            borderColor: 'yellow',
                            borderWidth: 2,
                            label: {
                                content: 'Rango B',
                                enabled: true,
                                position: 'right'
                            }
                        },{
                            type: 'line',
                            mode: 'horizontal',
                            scaleID: 'y',
                            value: 20,
                            borderColor: 'tomato',
                            borderWidth: 2,
                            label: {
                                content: 'Rango C',
                                enabled: true,
                                position: 'right'
                            }
                        }]
                    }}

                }

            });
        </script>
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
