# Week 3 – Variational Autoencoder (VAE)

This week focuses on implementing Variational Autoencoders (VAEs) as part of  
**CSET419 – Introduction to Generative AI**.

Two experiments are performed to understand how VAEs learn latent
representations and generate new data samples.

---

## Experiment 1: VAE on Fashion-MNIST
- Dataset: Fashion-MNIST (28×28 grayscale clothing images)
- Objective: Learn latent representations and generate new clothing samples
- Observation: Generated images are slightly blurry, which is expected behavior
  of VAEs due to probabilistic decoding and KL-divergence regularization.

---

## Experiment 2: VAE on MNIST
- Dataset: MNIST handwritten digit dataset
- Objective: Clearly demonstrate the working of a Variational Autoencoder on
  simpler image data
- Observation: Generated digit images are sharper and more interpretable,
  showing effective latent space learning.

---

## Key Concepts Covered
- Encoder–Decoder architecture
- Latent mean and log-variance
- Reparameterization trick
- KL-divergence loss
- Sample generation from latent space

---

## Tools and Frameworks
- Python
- PyTorch
- Google Colab
# Week 3 – Variational Autoencoder (VAE)

This experiment implements a Variational Autoencoder (VAE) as part of  
**CSET419 – Introduction to Generative AI**.

## Objective
- Learn latent representations of image data  
- Generate new samples from a learned probability distribution  

## Dataset
- Fashion-MNIST (28×28 grayscale images of clothing items)

## Methodology
- Encoder–Decoder architecture  
- Latent mean and log-variance estimation  
- Reparameterization trick  
- Reconstruction loss and KL-divergence loss  

## Results
- Successful reconstruction of input images  
- Generation of new Fashion-MNIST samples  
- Slight blurriness observed, which is expected behavior for VAEs  

## Tools & Framework
- Python  
- PyTorch  
- Google Colab

