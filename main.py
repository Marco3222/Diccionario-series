generos = {
    "drama medico":"los eventos de la serie se situan en un hospital y se centran en el personal y sus vidas, ya sea en el hospital y personal", 
    "thriller":"busca generar tension, intriga y a veces miedo, emocionando al espectador conforme aumenta el suspenso, nomralmente incluyen crimenes y misterios", 
    "drama politico":"serie con componenets politicos, ficticios o no", 
    "documentas":"representa eventos reales con fines informativos"
}

pregunta = input("Ingresa un genero de serie:")
pregunta = pregunta.lower()

if pregunta in generos.keys():
    print(generos[pregunta])
else:
    print("Genero no encontrado")
