# Week 4 — Text Generation (Generative AI Lab)

This week focuses on building text generation models using two deep learning approaches:

1. Character-level LSTM
2. Transformer-based model

---

## Component 1 — LSTM Text Generation

A character-level LSTM is trained on a small AI corpus to predict the next character.

### Key Steps
- Character tokenization
- Sequence creation
- LSTM training
- Temperature-based text generation

---

## Component 2 — Transformer Text Generation

A mini Transformer encoder model is trained for word-level text generation.

### Key Steps
- Word tokenization
- N-gram sequence creation
- Positional encoding
- Transformer encoder block
- Text generation

---

## Results Summary

| Model | Observation |
|---|---|
| LSTM | Learns character patterns, output partially readable |
| Transformer | Generates meaningful word-level sentences |

Transformers perform better due to self-attention and better context understanding.
