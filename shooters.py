cobradores = "*WT+$"
porteros = "*WT+$"
equipo = "amor a roma"

# Contador y Unicode. ME HACE FALTA HACER BIEN EL CONTADOR DE LOS GOLES
cobradores = list(cobradores)
porteros = list(porteros)
total = 0  # Goles del mejor cobrador
for cobrador in cobradores:
    goles = 0 # Goles del cobrador
    for portero in porteros:
        if cobrador > portero:
            goles += 1
            print("\u00D8", end="")
        elif cobrador == portero:
            print("\u265E", end="")
        else:
            print("\u00A5", end="")
    if goles > total:
        total = goles

# palindromo
equipo = equipo.lower()
equipo = equipo.strip()
equipo = equipo.replace(" ", "")
equipo = equipo.replace("í", "i")

if str(equipo) == str(equipo)[::-1]:
    print("\nES PALINDROMO")
else:
    print("\nNO ES PALINDROMO")

print(total)