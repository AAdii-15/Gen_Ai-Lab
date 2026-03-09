# Week-7 — Neural Style Transfer (NST)

Course: CSET419 – Introduction to Generative AI

## Objective
To implement Neural Style Transfer (NST) using a pretrained CNN and generate a stylized image by combining:
- Content of one image
- Style of another image

## Dataset
Students may use any images.

Examples:
- CIFAR-10 dataset for content images
- WikiArt dataset for style images

One image is chosen as the **content image** and another as the **style image**.

## Lab Tasks

### Data Preparation
- Load one content image
- Load one style image
- Load pretrained VGG19 model
- Freeze model weights
- Extract:
  - Content layer
  - Style layers

### Define Loss Functions
- Content loss
- Style loss
- Total loss

### Implement Style Transfer
- Feature-based style transfer
- Loss-based image optimization

## Expected Output

The generated image should show:

- Content structure preserved
- Style texture transferred
- Artistic appearance similar to the style image

## Files

Week-7
- Lab7_GAI.ipynb
- README.md
