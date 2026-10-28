# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# PyTorch 2.7.1 + CUDA 11.8 + cuDNN 9. Requires NVIDIA Container Toolkit.
FROM pytorch/pytorch:2.7.1-cuda11.8-cudnn9-runtime

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        graphviz \
        libglib2.0-0 \
        libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY environment/requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

ENV SHELL=/bin/bash
ENV PYTHONPATH=/dli/tutorials
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /dli
COPY . .

WORKDIR /dli/tutorials

# Fail the image build if the runtime data bootstrap was not packaged.
RUN python -c "from data.download_flowers import main as download_flowers; assert callable(download_flowers)"

EXPOSE 8888

ENTRYPOINT ["/dli/environment/entrypoint.sh"]
