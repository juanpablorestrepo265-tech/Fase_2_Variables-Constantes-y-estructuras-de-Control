# ==========================
# PROGRAMA: Panadería 
# Autor: Juan Pablo restrepo
# Curso: Fundamentos de Programacion
# ==========================
 
# Fecha de creación del programa: 2026-02-26

# Diccionario de productos y precios
productos = {
    "Integral": 2000,
    "Frances": 3000,
    "Queso": 1000,
    "Chocolate": 6000,
    "Manzana": 5000,
}

carrito = []  # aquí guardaremos lo que compra el usuario (producto, cantidad, total)
subtotal = 0

print("===================================")
print("        PANADERÍA - MENÚ")
print("===================================")
print("Panes:")
print(" - Integral:  $2.000")
print(" - Frances:   $3.000")
print(" - Queso:     $1.000")
print("Pasteles:")
print(" - Chocolate: $6.000")
print(" - Manzana:   $5.000")
print("===================================")
print("Escribe el producto para comprar.")
print("Escribe 'salir' para terminar y ver la factura.")
print("===================================\n")

while True:
    # Pedir producto
    producto = input("Producto: ").strip().title()

    # Salir
    if producto == "Salir":
        break

    # Validar que no esté vacío
    if producto == "":
        print("⚠️ No puedes dejar el producto vacío. Intenta de nuevo.\n")
        continue

    # Validar que exista
    if producto not in productos:
        print("❌ Producto no disponible. Intenta de nuevo.\n")
        continue

    # Pedir cantidad con validación
    while True:
        cantidad_txt = input("Cantidad: ").strip()

        if cantidad_txt.isdigit():
            cantidad = int(cantidad_txt)
            if cantidad > 0:
                break
            else:
                print("⚠️ La cantidad debe ser mayor que 0.")
        else:
            print("⚠️ Debes ingresar un número entero (ej: 1, 2, 3...).")

    # Calcular total por ese producto
    precio_unitario = productos[producto]
    total_producto = precio_unitario * cantidad

    # Guardar en el carrito
    carrito.append((producto, cantidad, precio_unitario, total_producto))
    subtotal += total_producto

    print(f"✅ Agregado: {producto} x{cantidad} = ${total_producto:,}".replace(",", "."))
    print(f"Subtotal actual: ${subtotal:,}".replace(",", "."))
    print("-----------------------------------\n")

# Si no compró nada
if subtotal == 0:
    print("\nNo se realizó ninguna compra.")
    input("Presiona Enter para finalizar...")
    exit()

# Aplicar descuento si corresponde
descuento = 0
if subtotal > 10000:
    descuento = subtotal * 0.20

total_final = int(subtotal - descuento)

# Imprimir factura
print("\n===================================")
print("            FACTURA")
print("===================================")

for item in carrito:
    prod, cant, unit, totalp = item
    unit_str = f"${unit:,}".replace(",", ".")
    total_str = f"${totalp:,}".replace(",", ".")
    print(f"{prod:<10} x{cant:<3}  (Unit: {unit_str:<8})  Total: {total_str}")

print("-----------------------------------")
print(f"SUBTOTAL:  ${subtotal:,}".replace(",", "."))
if descuento > 0:
    print("DESCUENTO: 20% (por compras > $10.000)")
    print(f"AHORRAS:   ${int(descuento):,}".replace(",", "."))
print(f"TOTAL:     ${total_final:,}".replace(",", "."))
print("===================================")

input("\nPresiona Enter para finalizar la compra...")