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
        "# Model Evaluation Results\n",
        "\n",
        "## Dataset\n",
        "- Custom cat species dataset\n",
        "- Images organized by breed folders\n",
        "- Used for both pretrained and custom models\n",
        "\n",
        "## Model 1: ResNet-50 (Pretrained on ImageNet)\n",
        "- Task: Proxy cat detection\n",
        "- Evaluation method: ImageNet label keyword matching\n",
        "- Accuracy: 100%\n",
        "\n",
        "## Model 2: Custom CNN\n",
        "- Task: Cat breed classification\n",
        "- Training/Test split: 80% / 20%\n",
        "- Accuracy: 100%\n",
        "\n",
        "## Notes\n",
        "- ResNet model was not trained for fine-grained breed classification\n",
        "- Custom CNN was trained directly on the dataset\n"
      ],
      "metadata": {
        "id": "cAQztdRTT7rW"
      }
    }
  ]
}