meme_dict = {
    "AESTHETIC" : "Hace referencia a la estética o estilo visual, especialmente cuando es agradable o de moda",
    "BFF" : "Best Friends Forever o Mejores amigos para siempre.",
    "DOXEAR" : "Publicar o revelar información personal de alguien en internet sin su consentimiento.",
    "F" : "Se usa para expresar respeto o condolencias en situaciones tristes o desafortunadas.",
    "GHOSTEAR" : "Dejar de hablar con alguien de manera repentina sin explicación, ignorando todos sus intentos de contacto.",
    "HYPE" : "Emoción o expectación excesiva hacia algo, como una película, evento o producto. Estar hypeado significa estar muy emocionado por algo.",
    "RANDOM" : "Algo o alguien inesperado o sin relación clara con lo que está sucediendo. ¡Qué random! se usa para expresar sorpresa ante algo fuera de lugar.",
    "SIMP" : "Mostrar una devoción excesiva por alguien, generalmente por una celebridad o alguien que no corresponde.",
    "ZZZ" : "Usado para indicar que algo es aburrido o para sugerir que alguien está dormido o desinteresado.",
}

word = input('Que palabra deseas saber?\n')

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('No se conoce sobre esa palabra')
