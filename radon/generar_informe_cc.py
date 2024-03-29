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
                <th>Nombre</th>
                <th>Métodos</th>
            </tr>
    '''

    # Agrega filas al informe HTML
    for filename_path, class_info in data.items():
        indice = filename_path.find("/geneva/")
        filename = filename_path[indice:]
        for class_data in class_info:
            methods = [method.get("name", "") for method in class_data.get("methods", [])]
            html_report += f'''
                <tr>
                    <td>{filename}</td>
                    <td>{class_data["type"]}</td>
                    <td>{class_data["rank"]}</td>
                    <td>{class_data["complexity"]}</td>
                    <td>{class_data["name"]}</td>
                    <td>{", ".join(methods)}</td>
                </tr>
            '''

    # Finaliza el informe HTML
    html_report += '''
        </table>
        <div id="contenedorCanvas" style="overflow: auto; width: 100%; height: 100%;">
            <canvas id="chart"></canvas>
        </div>

        <script>
            document.getElementById('chart').width = document.getElementById('contenedorCanvas').clientWidth;
            document.getElementById('chart').height = document.getElementById('contenedorCanvas').clientHeight;
            // Datos para el gráfico
            var data = ''' + json.dumps(data) + ''';
            var filenames = Object.keys(data);
            var rutaBase = "/home/dparrilla/development/ude_proyecto_grado/geneva/";

            var sortedData = Object.entries(data).sort((a, b) => b[1][0].complexity - a[1][0].complexity);
            var top10Data = sortedData.slice(0, 10);
                       var top10Labels = top10Data.map(([filename, classInfo]) => getFileName(filename) + " / " + classInfo[0].name);

            var top10Complexities = top10Data.map(([filename, classInfo]) => classInfo[0].complexity);

            function getFileName(rutaCompleta) {
                var indice_geneva = rutaCompleta.indexOf("/geneva/");
                var fileName = rutaCompleta.substring(indice_geneva);
                return fileName;
            }
            // Configuración del gráfico
            var ctx = document.getElementById('chart').getContext('2d');
              var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: top10Labels,
                    datasets: [{
                        label: 'Complejidad Ciclomática',
                        data: top10Complexities,
                        backgroundColor: top10Complexities.map(value => getColor(value)),
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
                                display: true,
                                position: 'right',
                                backgroundColor: 'rgba(0, 0, 0, 0)', // Color de fondo transparente
                                color: 'black' // Color del texto negro
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
                                display: true,
                                position: 'right',
                                backgroundColor: 'rgba(0, 0, 0, 0)', // Color de fondo transparente
                                color: 'black' // Color del texto negro
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
                                display: true,
                                position: 'right',
                                backgroundColor: 'rgba(0, 0, 0, 0)', // Color de fondo transparente
                                color: 'black' // Color del texto negro
                            }
                        }]
                    }}

                }

            });
            // Función para determinar el color de cada barra
            function getColor(value) {
                if (value > 10) {
                    // Calcular el tono de verde en un degradado de 20 a 100
                    var hue = 0; // Rojo
                    var saturation = 100; // Saturación al máximo
                    var lightness = 50 + value ; // 50% a 100% de luminosidad
                    return 'hsl(' + hue + ', ' + saturation + '%, ' + lightness + '%)';
                } else if (value >= 5 && value <= 10) {
                    // Calcular el tono de amarillo en un degradado de 10 a 20
                    var hue = 60 + ((value - 10)); // 60° a 120°
                    return 'hsl(' + hue + ', 100%, 50%)'; // Amarillo con saturación y luminosidad al 100%
                } else {
                    // Calcular el tono de rojo en un degradado de 0 a 10
                    var hue = 120; // Verde
                    var saturation = 100; // Saturación al máximo
                    var lightness = 50 + value;
                    return 'hsl(' + hue + ', ' + saturation + '%, ' + lightness + '%)';
                }
            }
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
with open('informe_cc_iteracion.html', 'w') as html_file:
    html_file.write(html_report)
