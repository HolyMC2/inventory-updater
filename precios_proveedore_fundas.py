#!/usr/bin/env python3

import csv


precios_fundas = {
    "case colors": 160,
    "universal colores": 160,
    "universal brillos": 160,
    "holster": 180,
    "guess": 220,
    "calvinklein": 220,
    "superstar": 230,
    "otter": 250,
    "camera protect": 200,
    "cartera brillos": 150,
    "funda velcro": 150,
    "macaron matte": 250,
    "space collection": 160,
    "magsafe transparente": 260,
    "magnetica": 240,
    "alto impacto": 250,
    "nike madera": 120,
    "jordan madera": 120,
    "acrilico sencillo": 180,
    "fosforescentes": 240,
    "silicone cover": 200,
    "anillo humo": 240,
    "colors 360": 220,
}

with open(
    "/home/holymc2/negocio-celulares/inventario/inventario fundas.csv",
    "+",
    encoding="latin-1",
) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            for k, v in precios_fundas.items():
                if k == row[7]:
                    precio = csv.writer(csv_file)
                    precio.writerow(row[4])

            print(
                f"\tReferencia: {row[0]} compra: ${row[3]} venta: ${row[4]} categoria: {row[6]} modelo_funda: {row[7]}"
            )
            line_count += 1
    print(f"Processed {line_count} lines.")


# def precios(x, y):
# "le pone el precio a las fundas dependiendo del modelo"
# if x.get(key) == y:
