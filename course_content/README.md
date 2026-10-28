# Generative AI with Diffusion Models Course Content

This directory contains the complete shared runtime and instructional material.
All course modules use the same environment and dependency set.

## Contents

~~~text
.
├── Dockerfile
├── environment/
│   ├── entrypoint.sh
│   └── requirements.txt
├── slides/
│   ├── FOR_OSRB_REVIEW.md
│   └── THIRD_PARTY_NOTICES.md
└── tutorials/
    ├── 00_jupyterlab.ipynb
    ├── 01_UNets.ipynb
    ├── 02_Diffusion_Models.ipynb
    ├── 03_Optimizations.ipynb
    ├── 04_Classifier_Free_Diffusion.ipynb
    ├── 05_CLIP.ipynb
    ├── 06_MNIST_Diffusion.ipynb
    ├── data/
    ├── images/
    └── utils/
~~~

Module 06 is provided as an optional MNIST diffusion capstone tutorial.

## Prepare the data

FashionMNIST and MNIST download automatically when a relevant notebook runs.
Module 04 and Module 05 also download TensorFlow Flowers automatically when
needed. To prefetch the flowers, run:

~~~bash
python tutorials/data/download_flowers.py
~~~

The script downloads the public TensorFlow Flowers archive and retains its
LICENSE.txt alongside the images. It is safe to run repeatedly, and downloaded
files are ignored by Git.

## Run with Docker

~~~bash
docker build -t oss-genai .
docker run --rm -it --gpus all -p 8888:8888 oss-genai
~~~

To preserve notebook edits, mount the tutorials directory:

~~~bash
docker run --rm -it --gpus all -p 8888:8888 \
  -v "$PWD/tutorials:/dli/tutorials" \
  oss-genai
~~~

## Run locally

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
jupyter lab tutorials
~~~

The notebooks are designed for GPU execution. Some introductory cells work on
CPU, but training later models will be slow without CUDA.
