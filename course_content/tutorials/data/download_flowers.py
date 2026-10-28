# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Download the TensorFlow Flowers data used by Modules 04 and 05."""

from __future__ import annotations

import shutil
import tarfile
import tempfile
from pathlib import Path
from urllib.request import urlopen


DATA_URL = (
    "https://storage.googleapis.com/download.tensorflow.org/"
    "example_images/flower_photos.tgz"
)
DATA_DIR = Path(__file__).resolve().parent
TARGET_DIR = DATA_DIR / "flower_photos"


def _safe_extract(archive: tarfile.TarFile, destination: Path) -> None:
    destination = destination.resolve()
    for member in archive.getmembers():
        if member.issym() or member.islnk():
            raise RuntimeError(f"Archive links are not allowed: {member.name}")
        member_path = (destination / member.name).resolve()
        if destination not in member_path.parents and member_path != destination:
            raise RuntimeError(f"Unsafe archive path: {member.name}")
    archive.extractall(destination)


def main() -> None:
    if TARGET_DIR.exists():
        print(f"Dataset already exists at {TARGET_DIR}")
        return

    with tempfile.TemporaryDirectory(prefix="oss-genai-flowers-") as temp:
        temp_dir = Path(temp)
        archive_path = temp_dir / "flower_photos.tgz"

        print(f"Downloading {DATA_URL}")
        with urlopen(DATA_URL) as response, archive_path.open("wb") as output:
            shutil.copyfileobj(response, output)

        with tarfile.open(archive_path, mode="r:gz") as archive:
            _safe_extract(archive, temp_dir)

        extracted = temp_dir / "flower_photos"
        if not extracted.is_dir() or not (extracted / "LICENSE.txt").is_file():
            raise RuntimeError("The downloaded archive has an unexpected layout.")

        shutil.move(str(extracted), TARGET_DIR)

    print(f"Installed TensorFlow Flowers at {TARGET_DIR}")


if __name__ == "__main__":
    main()
