import torch
import torch.nn as nn
import torch.optim as optim
import os

# Configuración del modelo
CONTEXT_SIZE = 3
EMBEDDING_DIM = 64
HIDDEN_DIM = 128
LEARNING_RATE = 0.01
EPOCHS = 100

class MiniTransformer(nn.Module):
    def __init__(self, vocab_size, embedding_dim, context_size, hidden_dim):
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        # Capa lineal para procesar los embeddings concatenados
        self.fc1 = nn.Linear(embedding_dim * context_size, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, x):
        # Convertimos los índices en vectores, los aplanamos y pasamos por la red
        embeds = self.embeddings(x).view(x.size(0), -1)
        out = self.fc1(embeds)
        out = self.relu(out)
        return self.fc2(out)

def load_data():
    """Carga y limpia los datos de entrenamiento."""
    if not os.path.exists("training_data.txt"):
        return ["hola", "mundo", "inteligencia", "artificial", "es", "genial"]
    with open("training_data.txt", "r", encoding="utf-8") as f:
        return [w.lower() for w in f.read().split() if w.isalnum()]

def build_and_train():
    """Construye el vocabulario y entrena el modelo desde cero."""
    words = load_data()
    vocab = sorted(list(set(words)))
    word_to_idx = {w: i for i, w in enumerate(vocab)}
    idx_to_word = {i: w for i, w in enumerate(vocab)}
    
    if len(words) <= CONTEXT_SIZE:
        # Modelo mínimo de fallback
        return None, word_to_idx, idx_to_word, len(vocab), 0.0
    
    # Preparación de tensores
    X = torch.tensor([ [word_to_idx[words[j]] for j in range(i, i+CONTEXT_SIZE)] 
                       for i in range(len(words)-CONTEXT_SIZE)], dtype=torch.long)
    y = torch.tensor([word_to_idx[words[i+CONTEXT_SIZE]] 
                      for i in range(len(words)-CONTEXT_SIZE)], dtype=torch.long)
    
    model = MiniTransformer(len(vocab), EMBEDDING_DIM, CONTEXT_SIZE, HIDDEN_DIM)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    loss_fn = nn.CrossEntropyLoss()
    
    # Entrenamiento
    model.train()
    for _ in range(EPOCHS):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        optimizer.step()
        
    return model, word_to_idx, idx_to_word, len(vocab), loss.item()

def predict(model, context, w2i, i2w):
    """Predice las 3 palabras más probables."""
    if model is None: return [{"word": "error", "prob": 0}]
    
    # Tomamos los últimos N tokens definidos en CONTEXT_SIZE
    context = context[-CONTEXT_SIZE:]
    indices = [w2i.get(w.lower(), 0) for w in context]
    
    if len(indices) < CONTEXT_SIZE:
        return [{"word": "escribe", "prob": 100}, {"word": "más", "prob": 100}]
    
    model.eval()
    with torch.no_grad():
        probs = torch.softmax(model(torch.tensor(indices).unsqueeze(0)), dim=1)
        top_p, top_i = torch.topk(probs, 3)
        return [{"word": i2w[i.item()], "prob": round(p.item()*100, 1)} 
                for p, i in zip(top_p[0], top_i[0])]