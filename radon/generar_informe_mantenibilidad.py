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
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation"></script>
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
            var mi = Object.values(data).map(classInfo => classInfo.mi);

            // Configuración del gráfico
            var ctx = document.getElementById('complexityChart').getContext('2d');
              var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labelsModificados,
                    datasets: [{
                        label: 'Complejidad Ciclomática',
                        data: mi,
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
                            max: 100
                        }
                    },
                     plugins: { annotation: {
                        annotations: [{
                            type: 'line',
                            mode: 'horizontal',
                            scaleID: 'y',
                            value: 20,
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
                            value: 10,
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

with open('informe_mantenibilidad.json', 'r') as file:
    informe_json = json.load(file)

# Genera el informe HTML
html_report = generate_html_report(informe_json)

# Guarda el informe HTML en un archivo
with open('informe_mantenibilidad.html', 'w') as html_file:
    html_file.write(html_report)
