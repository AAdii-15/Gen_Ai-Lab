# Week 8: DCGAN on CIFAR-10

## 🎯 Objective
The goal of this experiment is to generate realistic images using a Deep Convolutional Generative Adversarial Network (DCGAN) trained on the CIFAR-10 dataset.

---

## 📂 Dataset
- **CIFAR-10**
- 60,000 color images (32×32)
- 10 classes (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)

---

## 🧠 Model Architecture

### Generator (G)
- Input: Random noise vector (latent space)
- Layers:
  - ConvTranspose2D
  - Batch Normalization
  - ReLU activation
  - Final Tanh activation
- Output: Generated image (32×32×3)

### Discriminator (D)
- Input: Image (real or fake)
- Layers:
  - Convolutional layers
  - Batch Normalization
  - LeakyReLU activation
  - Final Sigmoid output
- Output: Probability (real vs fake)

---

## ⚙️ Training Details
- Latent Dimension: 100  
- Batch Size: 128  
- Learning Rate: 0.0002  
- Optimizer: Adam (β1=0.5, β2=0.999)  
- Loss Function: Binary Cross Entropy (BCE)

---

## 🖼️ Results

### Generated Samples
- Multiple images generated from random noise

### Latent Space Interpolation
- Smooth transition between two noise vectors

### Evaluation Image
- Single generated output for qualitative assessment

---

## 📁 Files

- `Lab_8.ipynb` → Main implementation
- `output/generated_samples.png` → Generated images
- `output/latent_interpolation.png` → Interpolation results
- `output/eval_image.png` → Single generated image
- `output/loss_plot.png` → Training loss curve (if trained)
- `output/training_log.txt` → Training logs

---

## 📌 Conclusion
The DCGAN model successfully learns to generate CIFAR-10-like images from random noise. The interpolation demonstrates that the latent space captures meaningful transitions between generated images.

---

## 🚀 Future Improvements
- Use deeper GAN architectures (e.g., StyleGAN)
- Train for more epochs for higher quality
- Apply techniques like label smoothing or gradient penalty
