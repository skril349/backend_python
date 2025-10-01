import clases

persona = clases.Persona()

persona.setNombre("Victor")
persona.setApellidos("Robles")
persona.setAltura("190cm")
persona.setEdad("800 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("-----------------------------------------")

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Manuel")
informatico.setAltura("160cm")
informatico.setEdad("26 años")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.experiencia)

print("-----------------------------------------")

tecnico = clases.TecnicoRedes()
informatico.setNombre("Toni")
informatico.setApellidos("Vives")

print(tecnico.getLenguajes())