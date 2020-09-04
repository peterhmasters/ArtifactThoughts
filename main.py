from dummy_data import generate_data
from classifier import generate_classifier
from ask_gaben import ask_gaben

# Training data is generated from simulated games
train_data = generate_data(100)

# A simple classifier is trained on the training data
clf = generate_classifier(train_data)

# Then using the classifier, ask gaben outputs which of the four choices have the highest probability of winning
print(ask_gaben(clf, {"R5", "B4", "G5", "U3"}, {"U9", "U1"}, {"R2", "G3"}))
