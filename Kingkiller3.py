import markovify

# Get raw text as string.
with open("KKC1.txt") as f:
    text_a = f.read()
with open("KKC2.txt") as f:
    text_b = f.read()
# Build the model.
text_model_a = markovify.Text(text_a, state_size=4)
text_model_b = markovify.Text(text_b, state_size=4)
#combine Models
model_combo=markovify.combine([text_model_a, text_model_b], [1, 1])


#Print five randomly-generated sentences
#for i in range(10):
#    print(model_combo.make_sentence())

#Print three randomly-generated sentences of no more than 140 characters
for i in range(10):
    print(model_combo.make_short_sentence(160))
