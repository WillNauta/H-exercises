# H-exercise
Jobs a excersies to Edgar

# Information
Exercises are performed for edgar

-take into account and read the readme to understand what problems within the program

# Do clone to this Repository 🛠️
- - - - - - - - - - - - - - - - - - - - - - - - -
-Hacer clone del repositorio
```
https://github.com/WilliamQuinteroT/H-exerces.git
```
# Explanation 🚀

You have a confusion between total and goals that has neither head nor tail.

Let's clarify:

-total is the number of goals of the best collector to date. This starts at zero at the beginning of the program.
-goals is the amount of goals of the collector that we examine now. It is reset with each new iteration.
Code

```
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
 ```

 After pitting the collector against all the goalkeepers, we see if his goals exceed the total of the best to date. In this case, we update
 ``` 
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

 ```

Test
 ```
♞¥¥¥ØØ♞ØØØØ¥♞ØØØ¥¥♞Ø¥¥¥¥♞
ES PALINDROMO
4

Process finished with exit code 0
 ```