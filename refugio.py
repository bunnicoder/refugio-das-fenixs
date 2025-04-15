import random
from datetime import datetime

print("🌈 Sentimentos que posso acolher: triste, ansiosa, feliz, sozinha")
print("🌸✨ Boas-vindas ao Refúgio da Fênix ✨🌸")
print("Como você está se sentindo hoje?\n")
sentimento = input("Digite seu sentimento: ").lower()

mensagens_personalizadas = {
    "triste": [
        "Está tudo bem chorar, sua luz ainda brilha. 🌧️",
        "A fênix também teve dias cinzas antes de renascer. 🔥",
    ],
    "ansiosa": [
        "Respira fundo, você está segura agora. 🌬️",
        "Passo a passo, tudo se acalma. 🍃",
    ],
    "feliz": [
        "Que essa alegria se espalhe por todo seu dia! ☀️",
        "A felicidade é sua natureza brilhando. ✨",
    ],
    "sozinha": [
        "Você nunca está só — estou aqui com você. 💖",
        "O universo sempre envia companhia no tempo certo. 🌌",
    ],
}

mensagens_gerais = [
    "Você é importante. 🌟",
    "Mesmo em silêncio, você vale muito. 🌙"
]

if sentimento in mensagens_personalizadas:
    resposta = random.choice(mensagens_personalizadas[sentimento])
else:
    resposta = random.choice(mensagens_gerais)

print(f"\n💌 Mensagem para você: {resposta}")

# Guardar no diário
with open("diario_da_fenix.txt", "a", encoding="utf-8") as diario:
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    diario.write(f"[{agora}] Sentimento: {sentimento}\nMensagem: {resposta}\n\n")

print("\n🪶 Suas palavras foram guardadas com carinho no diário da Fênix.")

