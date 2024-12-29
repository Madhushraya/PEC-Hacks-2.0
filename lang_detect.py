import fasttext

model = fasttext.load_model('lid.176.bin')

text = "మధు ఒక మేధావి"
predicted_language, probability = model.predict(text)

print(f"Predicted language: {predicted_language[0].split('__label__')[1]}")
print(f"Probability: {round(probability[0],3)}")

