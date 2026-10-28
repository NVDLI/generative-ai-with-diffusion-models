# Third-Party Notices

This file identifies third-party software, datasets, model artifacts, and
media included in or used by this project. Third-party material retains its
original license and is not relicensed by the repository's Apache-2.0 and
CC-BY-4.0 terms.

---

## Third-party OSS dependencies

The following direct dependencies are declared in
`course_content/environment/requirements.txt` and installed into the course
container. They are not committed to this repository as source code. Their
transitive dependencies retain their respective upstream licenses.

| Package | Version or revision | License | Source |
|---------|---------------------|---------|--------|
| einops | 0.6.1 | MIT | https://github.com/arogozhnikov/einops |
| graphviz (Python package) | 0.20.1 | MIT | https://github.com/xflr6/graphviz |
| ipywidgets | 8.1.0 | BSD-3-Clause | https://github.com/jupyter-widgets/ipywidgets |
| JupyterLab | 4.6.4 | BSD-3-Clause | https://github.com/jupyterlab/jupyterlab |
| Matplotlib | 3.8.4 | Matplotlib License (PSF-based) | https://github.com/matplotlib/matplotlib |
| NumPy | 1.26.4 | BSD-3-Clause | https://github.com/numpy/numpy |
| Pillow | 13.0.0 | HPND / PIL-Pillow license | https://github.com/python-pillow/Pillow |
| torchview | 0.2.6 | MIT | https://github.com/mert-kurttutan/torchview |
| OpenAI CLIP | `ded190a052fdf4585bd685cee5bc96e0310d2c93` | MIT | https://github.com/openai/CLIP |

The OpenAI CLIP dependency is pinned to the full upstream commit shown above
for reproducible installation.

### Container base image and operating-system packages

The Dockerfile uses:

- Image: `pytorch/pytorch:2.7.1-cuda11.8-cudnn9-runtime`
- Registry: https://hub.docker.com/r/pytorch/pytorch
- Base operating system: Ubuntu 22.04

PyTorch (2.7.1) and TorchVision are included in the base image and are BSD-3-Clause. CUDA, cuDNN, and other NVIDIA components in the base
image remain governed by their included NVIDIA terms, including the NVIDIA
Deep Learning Container License where applicable:

https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

The Dockerfile also installs these Ubuntu packages at build time:
`build-essential`, `ca-certificates`, `git`, `graphviz`, `libglib2.0-0`, and
`libgl1`. Each package and its dependencies retain the licenses recorded by
Ubuntu under `/usr/share/doc/<package>/copyright` in the built image.

Before distributing a built derivative container image, preserve all license
files from the base image and installed packages and generate an SBOM from the
final image. This repository does not commit or distribute a prebuilt image.

---

## Adapted source code

### Conditional Diffusion MNIST implementation

Portions of `course_content/tutorials/04_Classifier_Free_Diffusion.ipynb`,
`course_content/tutorials/utils/UNet_utils.py`, and
`course_content/tutorials/utils/ddpm_utils.py` are adapted from:

https://github.com/TeaPearce/Conditional_Diffusion_MNIST/blob/main/script.py

Copyright (c) 2022 Tim Pearce. Licensed under the MIT License; see
[`LICENSES/MIT.txt`](LICENSES/MIT.txt).

NVIDIA modified the material for this course, including reorganizing the
implementation into notebook and utility modules and adapting the model,
training, sampling, and visualization workflow. NVIDIA's modifications are
licensed under Apache-2.0; the combined files are marked `MIT AND Apache-2.0`.

The TeaPearce repository states that its implementation was modified from
`cloneofsimo/minDiffusion`:

https://github.com/cloneofsimo/minDiffusion

The upstream repository does not include a license file.

---

## Runtime-downloaded datasets

The repository does not host or bundle the complete datasets below. Learners
download them directly at runtime into their local course environment.

### TensorFlow Flowers

Modules 04 and 05 download the public TensorFlow Flowers archive from:

https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz

The archive contains 3,670 images across five classes. The notebooks use the
`daisy`, `sunflowers`, and `roses` classes. TensorFlow describes these images
as CC-BY and directs users to the `LICENSE.txt` contained in the archive for
the individual creator attribution and applicable terms:

https://www.tensorflow.org/guide/data

`course_content/tutorials/data/download_flowers.py` verifies that the archive
contains `LICENSE.txt` and keeps that file with the downloaded images. The
dataset is not committed to this repository.

### Fashion-MNIST

Modules 01 through 04 download and use Fashion-MNIST through TorchVision.

Source: https://github.com/zalandoresearch/fashion-mnist

Fashion-MNIST contains 60,000 training images and 10,000 test images. It is
Copyright (c) 2017 Zalando SE and licensed under the MIT License; see
[`LICENSES/MIT.txt`](LICENSES/MIT.txt).

The following NVIDIA-created educational figures committed to this repository
incorporate or depict Fashion-MNIST samples, transformations, or model outputs:

- `course_content/tutorials/images/FMUNet.png`
- `course_content/tutorials/images/rev_diffusion.png`
- `course_content/tutorials/images/shirt_shoe.png`
- `course_content/tutorials/images/shoe_maybe.png`
- `course_content/tutorials/images/time_nn.png`
- `course_content/tutorials/images/weighted_reverse_diffusion.png`

The Fashion-MNIST portions retain the MIT License. NVIDIA's figure composition,
annotations, and other original contributions are licensed under CC-BY-4.0.
The composite files are therefore marked `MIT AND CC-BY-4.0`.

### MNIST Database of Handwritten Digits

Module 06 downloads MNIST through `torchvision.datasets.MNIST`. TorchVision
first uses the PyTorch OSSCI mirror and falls back to the canonical MNIST site:

- https://ossci-datasets.s3.amazonaws.com/mnist/
- https://yann.lecun.com/exdb/mnist/

MNIST contains 60,000 training images and 10,000 test images. The dataset is
associated with Yann LeCun, Corinna Cortes, and Christopher J. C. Burges.
It is not committed to or redistributed by this repository.

---

## Runtime-downloaded model artifacts

### OpenAI CLIP software and ViT-B/32 checkpoint

Module 05 imports OpenAI CLIP and calls `clip.load("ViT-B/32")`. The CLIP
package downloads the checkpoint, if absent, from this OpenAI-hosted URL:

https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt

The package source is Copyright (c) 2021 OpenAI and licensed under MIT:

https://github.com/openai/CLIP/blob/ded190a052fdf4585bd685cee5bc96e0310d2c93/LICENSE

Neither the package source nor the checkpoint is committed to this repository.
The checkpoint is cached in the learner's environment. The repository's model
card describes the model's intended research use, limitations, and training
data provenance:

https://github.com/openai/CLIP/blob/ded190a052fdf4585bd685cee5bc96e0310d2c93/model-card.md

The upstream repository does not provide a separate license file expressly
scoped to the downloaded `.pt` checkpoint.

---

## Third-party media

### JupyterLab interface screenshot

`course_content/tutorials/images/jl_launcher.png` is an NVIDIA-created and
annotated screenshot of the JupyterLab interface. JupyterLab is Copyright (c)
2015-2025 Project Jupyter Contributors and licensed under BSD-3-Clause; see
[`LICENSES/BSD-3-Clause.txt`](LICENSES/BSD-3-Clause.txt). NVIDIA's annotations
and composition are licensed under CC-BY-4.0. The composite file is marked
`BSD-3-Clause AND CC-BY-4.0`.

Project Jupyter and NVIDIA names, logos, and trademark rights are not licensed.

---

## Referenced research and examples

The notebooks link to research papers, documentation, blog posts, and example
implementations for educational context. Linked works are not copied into this
repository and remain under their own licenses. Adapted source material is
identified separately above.

---
