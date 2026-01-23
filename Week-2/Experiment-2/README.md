## CSET419 – Introduction to Generative AI
### Week 2 – Experiment 2

**Title:** GAN for Fashion-MNIST Image Generation

**Objective:**  
To implement and train a Generative Adversarial Network (GAN) on the Fashion-MNIST dataset to generate synthetic clothing images and evaluate the generated samples using a trained classifier.

**Dataset:**  
Fashion-MNIST (28×28 grayscale images of clothing items)

**Methodology:**  
- A Generator network learns to create Fashion-MNIST–like images from random noise.  
- A Discriminator network distinguishes between real and generated images.  
- Both networks are trained adversarially.  
- A simple classifier is trained on Fashion-MNIST to evaluate the generated images by predicting their labels.

**Contents:**
- `experiment2.ipynb` — GAN implementation for Fashion-MNIST  
- `final_100_fashion_images.png` — 10×10 grid of 100 generated clothing images


