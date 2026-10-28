# Generative AI with Diffusion Models
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue)](https://creativecommons.org/licenses/by/4.0/) [![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)


Generative AI with Diffusion Models is an open-source, hands-on NVIDIA Deep
Learning Institute course. Learners build diffusion models from foundational
U-Net components, improve them with modern architectural techniques, add
classifier-free guidance, and connect image generation with CLIP.

Explore the full catalog of NVIDIA DLI courses and training opportunities on our [![training catalogue](https://www.nvidia.com/en-us/training/?ncid=progr-251837-vt07)]

## Learning outcomes

In these labs, learners will:

- Build a U-Net and train it to remove noise from FashionMNIST images
- Implement the forward and reverse diffusion processes
- Improve generation with group normalization, GELU, rearrange pooling, and
  sinusoidal timestep embeddings
- Condition a diffusion model with classifier-free guidance
- Use CLIP embeddings to connect text prompts and generated images
- Apply the complete conditional diffusion workflow to MNIST in an optional
  capstone

## Course modules

| # | Module | Notebook |
|---|---|---|
| 00 | JupyterLab introduction | [00_jupyterlab.ipynb](./course_content/tutorials/00_jupyterlab.ipynb) |
| 01 | From U-Net to Diffusion | [01_UNets.ipynb](./course_content/tutorials/01_UNets.ipynb) |
| 02 | Diffusion Models | [02_Diffusion_Models.ipynb](./course_content/tutorials/02_Diffusion_Models.ipynb) |
| 03 | Optimizations | [03_Optimizations.ipynb](./course_content/tutorials/03_Optimizations.ipynb) |
| 04 | Classifier-Free Diffusion Guidance | [04_Classifier_Free_Diffusion.ipynb](./course_content/tutorials/04_Classifier_Free_Diffusion.ipynb) |
| 05 | CLIP | [05_CLIP.ipynb](./course_content/tutorials/05_CLIP.ipynb) |
| 06 | Optional MNIST diffusion capstone | [06_MNIST_Diffusion.ipynb](./course_content/tutorials/06_MNIST_Diffusion.ipynb) |

## Getting started

### Run with Docker

Prerequisites are Docker, an NVIDIA GPU, the NVIDIA driver, and NVIDIA
Container Toolkit.

~~~bash
cd course_content
docker build -t oss-genai .
docker run --rm -it --gpus all -p 8888:8888 oss-genai
~~~

Open http://localhost:8888 and select a notebook in the tutorials directory.
Module 04 downloads TensorFlow Flowers automatically the first time it reaches
Section 4.3.

### Run locally

Python 3.10 and a CUDA-capable NVIDIA GPU are recommended.

~~~bash
cd course_content
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
jupyter lab tutorials
~~~

FashionMNIST and MNIST are downloaded automatically by the notebooks. Modules
04 and 05 use three classes from the TensorFlow Flowers dataset. The download
helper installs the public TensorFlow archive under
`tutorials/data/flower_photos`. Modules 04 and 05 invoke this helper
automatically, and it can also be run manually to prefetch the data.

## Repository layout

The repository is organized as follows:

- course_content/Dockerfile defines the shared GPU notebook runtime.
- course_content/environment contains runtime dependencies and startup logic.
- course_content/tutorials contains notebooks, shared utilities, data setup,
  and educational images.
- LICENSES, REUSE.toml, and THIRD_PARTY_NOTICES.md contain licensing metadata.

All course modules share one environment because they use the same dependency
set.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Keep notebook outputs cleared and do
not commit downloaded datasets or generated artifacts.

## License

This repository uses a mixed licensing model:

- Source-code files and code cells in Jupyter notebooks:
  [Apache License 2.0](LICENSES/Apache-2.0.txt)
- Documentation, Markdown and raw notebook cells, and NVIDIA-created
  educational media:
  [Creative Commons Attribution 4.0 International](LICENSES/CC-BY-4.0.txt)
- - Third-party material: its original license, as documented in
  [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Third-party
  license texts are in [LICENSES/MIT.txt](LICENSES/MIT.txt) and
  [LICENSES/BSD-3-Clause.txt](LICENSES/BSD-3-Clause.txt).

Each complete Jupyter notebook is dual-licensed: code cells under Apache-2.0
and non-code cells under CC-BY-4.0. The combined dual-license terms are in
[LICENSES/CC-BY-4.0-Apache2_Dual_License.txt](LICENSES/CC-BY-4.0-Apache2_Dual_License.txt).

NVIDIA names, logos, and trademarks are not licensed for general reuse.
