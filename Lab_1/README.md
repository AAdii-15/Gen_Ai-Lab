{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Gen AI Lab – Cat Species Classification\n",
        "\n",
        "This project performs image classification using deep learning models.\n",
        "\n",
        "## Dataset\n",
        "- Cat species image dataset\n",
        "- Images organized in folder-per-class format\n",
        "- Dataset not included in the repository due to size constraints\n",
        "\n",
        "## Models Implemented\n",
        "\n",
        "### 1. ResNet-50 (Pretrained)\n",
        "- Pretrained on ImageNet\n",
        "- Used for proxy cat-detection accuracy\n",
        "\n",
        "### 2. Custom CNN\n",
        "- Built and trained from scratch\n",
        "- Used for cat breed classification\n",
        "\n",
        "## Files in this Repository\n",
        "- `resnet_accuracy.ipynb` – ResNet inference and accuracy calculation\n",
        "- `custom_cnn.ipynb` – CNN training and evaluation\n",
        "- `results.md` – Summary of results\n",
        "- `accuracy.txt` – Final accuracy values\n"
      ],
      "metadata": {
        "id": "quQuZGrCTyua"
      }
    }
  ]
}