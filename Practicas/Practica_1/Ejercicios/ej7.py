
horas = float(input("Introduce las Horas Trabajadas: "))
precio_hora = float(input("Introduce el Precio de la Hora: "))
retencion = float(input("Introduce la retencion aplicable en %: "))

salario_b = horas * precio_hora
salario_n = salario_b - (salario_b * (retencion/100))

print("El Salario Bruto es: ", salario_b)
print("El Salario Neto es: ", salario_n)