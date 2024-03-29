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
        <div id="contenedorCanvas" style="overflow: auto; width: 100%; height: 100%;">
            <canvas id="chart"></canvas>
        </div>

        <script>
            document.getElementById('chart').width = document.getElementById('contenedorCanvas').clientWidth;
            document.getElementById('chart').height = document.getElementById('contenedorCanvas').clientHeight;
            // Datos para el gráfico
            var data = ''' + json.dumps(data) + ''';
            var filenames = Object.keys(data);

            // Ordena los datos por el valor de 'mi' en orden descendente
            var sortedData = Object.entries(data).sort((a, b) => a[1].mi - b[1].mi);
            var top10Data = sortedData.slice(0, 10);
            var top10Filenames = top10Data.map(entry => entry[0]);
            var top10Mi = top10Data.map(entry => entry[1].mi);
            var labelsModificados = top10Filenames.map(function (rutaCompleta) {
                var indice_geneva = rutaCompleta.indexOf("/geneva/");
                var fileName = rutaCompleta.substring(indice_geneva);
                return fileName
            });


            // Configuración del gráfico
            var ctx = document.getElementById('chart').getContext('2d');
              var chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labelsModificados,
                    datasets: [{
                        label: 'Complejidad Ciclomática',
                        data: top10Mi,
                        backgroundColor: top10Mi.map(value => getColor(value)),
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
                                display: true,
                                position: 'right',
                                backgroundColor: 'transparent',
                                color: 'black'
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
                                display: true,
                                position: 'right',
                                backgroundColor: 'transparent',
                                color: 'black'
                            }
                        }]
                    }}

                }

            });
            // Función para determinar el color de cada barra
            function getColor(value) {
                if (value > 20) {
                    // Calcular el tono de verde en un degradado de 20 a 100
                    var hue = 120; // Verde
                    var saturation = 100; // Saturación al máximo
                    var lightness = value - 5;// La luminosidad sera igual a value (vlaor de 20 a 100) restandole 5% para que no quede transparente
                    return 'hsl(' + hue + ', ' + saturation + '%, ' + lightness + '%)';
                } else if (value >= 10 && value <= 20) {
                    // Calcular el tono de amarillo en un degradado de 10 a 20
                    var hue = 60 + ((value - 10)); // 60° a 120°
                    return 'hsl(' + hue + ', 100%, 50%)'; // Amarillo con saturación y luminosidad al 100%
                } else {
                    // Calcular el tono de rojo en un degradado de 0 a 10
                    var hue = 0; // Rojo
                    var saturation = 100; // Saturación al máximo
                    var lightness = 50 + value ; // 50% a 100% de luminosidad
                    return 'hsl(' + hue + ', ' + saturation + '%, ' + lightness + '%)';
                }
            }
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
with open('informe_mantenibilidad_iteracion.html', 'w') as html_file:
    html_file.write(html_report)
