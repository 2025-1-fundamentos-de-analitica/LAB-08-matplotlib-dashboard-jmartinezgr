# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    archivo_csv = "files/input/shipping-data.csv"
    carpeta_docs = "docs"

    # Verificar si la carpeta 'docs' existe, si no, crearla
    os.makedirs(carpeta_docs, exist_ok=True)

    # Leer los datos desde el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Crear contenido base del HTML
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shipping Dashboard</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            h1 {
                text-align: center;
                margin-top: 40px;
                font-size: 2.5em;
                color: #2c3e50;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px;
            }
            .dashboard-cards {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin-top: 40px;
            }
            .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin: 20px;
                padding: 20px;
                width: 300px;
                text-align: center;
            }
            .card img {
                max-width: 100%;
                border-radius: 8px;
            }
            .card-title {
                font-size: 1.5em;
                color: #2c3e50;
                margin-top: 15px;
            }
            .card-description {
                font-size: 1em;
                color: #7f8c8d;
            }
            .footer {
                text-align: center;
                padding: 20px;
                background-color: #34495e;
                color: white;
                margin-top: 40px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Shipping Dashboard</h1>
            <div class="dashboard-cards">
    """

    # --- 1. Shipping per Warehouse ---
    plt.figure()
    df["Warehouse_block"].value_counts().plot(
        kind="bar", color="lightblue", title="Shipping per Warehouse"
    )
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.tight_layout()
    path1 = os.path.join(carpeta_docs, "shipping_per_warehouse.png")
    plt.savefig(path1)
    plt.close()
    html_content += f"""
        <div class="card">
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse">
            <div class="card-title">Shipping per Warehouse</div>
            <div class="card-description">Graph showing the distribution of shipments across different warehouse blocks.</div>
        </div>"""

    # --- 2. Mode of Shipment ---
    plt.figure()
    df["Mode_of_Shipment"].value_counts().plot(
        kind="bar", color="lightgreen", title="Mode of Shipment"
    )
    plt.xlabel("Mode of Shipment")
    plt.ylabel("Count")
    plt.tight_layout()
    path2 = os.path.join(carpeta_docs, "mode_of_shipment.png")
    plt.savefig(path2)
    plt.close()
    html_content += f"""
        <div class="card">
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
            <div class="card-title">Mode of Shipment</div>
            <div class="card-description">Graph showing the count of each mode of shipment used.</div>
        </div>"""

    # --- 3. Average Customer Rating ---
    plt.figure()
    df["Customer_rating"].plot(
        kind="hist",
        color="salmon",
        bins=10,
        title="Average Customer Rating Distribution",
    )
    plt.xlabel("Customer Rating")
    plt.ylabel("Frequency")
    plt.tight_layout()
    path3 = os.path.join(carpeta_docs, "average_customer_rating.png")
    plt.savefig(path3)
    plt.close()
    html_content += f"""
        <div class="card">
            <img src="average_customer_rating.png" alt="Customer Rating">
            <div class="card-title">Average Customer Rating</div>
            <div class="card-description">Distribution of customer ratings for the products.</div>
        </div>"""

    # --- 4. Weight Distribution ---
    plt.figure()
    df["Weight_in_gms"].plot(
        kind="hist", color="lightcoral", bins=20, title="Weight Distribution"
    )
    plt.xlabel("Weight (gms)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    path4 = os.path.join(carpeta_docs, "weight_distribution.png")
    plt.savefig(path4)
    plt.close()
    html_content += f"""
        <div class="card">
            <img src="weight_distribution.png" alt="Weight Distribution">
            <div class="card-title">Weight Distribution</div>
            <div class="card-description">Histogram showing the distribution of product weights.</div>
        </div>"""

    # --- Finalizar HTML ---
    html_content += """
            </div>
        </div>
        <div class="footer">
            <p>&copy; 2024 Shipping Dashboard. All Rights Reserved.</p>
        </div>
    </body>
    </html>
    """

    # Guardar el archivo HTML
    with open(os.path.join(carpeta_docs, "index.html"), "w", encoding="utf-8") as file:
        file.write(html_content)
