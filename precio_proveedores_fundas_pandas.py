#!/usr/bin/env python3

import pandas as pd


proveedores_fundas = {
    "case colors": "cabocell",
    "universal colores": "cabocell",
    "universal brillos": "cabocell",
    "holster": "cellhit",
    "guess": "cellhit",
    "calvinklein": "cellhit",
    "superstar": "cabocell",
    "otter": "cabocell",
    "camera protect": "cabocell",
    "cartera brillos": "cabocell",
    "funda velcro": "cabocell",
    "macaron matte": "vlak",
    "space collection": "cellhit",
    "magsafe transparente": "vlak",
    "magnetica": "cellhit",
    "alto impacto": "cabocell",
    "nike madera": "cellhit",
    "jordan madera": "cellhit",
    "acrilico sencillo": "cabocell",
    "fosforescentes": "cabocell",
    "silicone cover": "cabocell",
    "anillo humo": "cabocell",
    "colors 360": "cabocell",
    "case cute": "cabocell",
}

compra_fundas = {
    "case colors": 10,
    "universal colores": 30,
    "universal brillos": 19,
    "holster": 25,
    "guess": 50,
    "calvinklein": 50,
    "superstar": 59,
    "otter": 85,
    "camera protect": 35,
    "cartera brillos": 49,
    "funda velcro": 52,
    "macaron matte": 70,
    "space collection": 45,
    "magsafe transparente": 85,
    "magnetica": 40,
    "alto impacto": 65,
    "nike madera": 10,
    "jordan madera": 10,
    "acrilico sencillo": 49,
    "fosforescentes": 64,
    "silicone cover": 10,
    "anillo humo": 60,
    "colors 360": 55,
    "case cute": 25,
}

venta_fundas = {
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
    "case cute": 200,
}


csv_fundas = pd.read_csv(
    "/home/holymc2/negocio-celulares/inventario/inventario fundas.csv"
)

data = pd.DataFrame(csv_fundas)

for k, v in venta_fundas.items():

    update_venta = data["modelo_funda"] == k
    data.loc[update_venta, "venta"] = v

for k, v in compra_fundas.items():

    update_compra = data["modelo_funda"] == k
    data.loc[update_compra, "compra"] = v

for k, v in proveedores_fundas.items():

    update_proveedor = data["modelo_funda"] == k
    data.loc[update_proveedor, "proveedores"] = v

    update_impuesto = data["impuesto"] == 0
    data.loc[update_impuesto, "impuesto"] = "000"

csv_fundas.to_csv("updated_fundas.csv")
print(csv_fundas)
