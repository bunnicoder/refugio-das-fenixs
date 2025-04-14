import random
from datetime import datetime

mensagens_de_apoio = [
    "Você é mais forte do que pensa. 🌟",
    "A fênix renasce...e você também. 🔥",
    "Estou aqui com você. Sempre. 💖",
    "Respira fundo. Está tudo bem. 🕊️",
    "Seu coração é uma constelação de luz. ✨",
    "O mundo precisa do seu jeitinho único. 🌸"
]

print("🌸✨ Boas vindas ao Refúgio da Fênix ✨🌸")
print("Como você está se sentindo hoje?\n")

sentimento = input("Digite seu sentimento: ")

resposta = random.choice(mensagens_de_apoio)
print(f"\n💌 Mensagem para você: {resposta}")

# Guardar no diário
with open("diario_da_fenix.txt", "a", encoding="utf-8") as diario:
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    diario.write(f"[{agora}] Sentimento: {sentimento}\nMensagem: {resposta}\n\n")

print("\n🪶 Suas palavras foram guardadas com carinho no diário da Fênix.")

