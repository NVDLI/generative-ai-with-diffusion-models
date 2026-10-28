#!/usr/bin/env bash
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

jupyter labextension disable "@jupyterlab/apputils-extension:announcements" || true

exec jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --allow-root \
    --no-browser \
    --ServerApp.root_dir=/dli/tutorials \
    --IdentityProvider.token="${JUPYTER_TOKEN:-}"
