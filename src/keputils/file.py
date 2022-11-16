import os
from typing import Callable


def walk_files(start_folder: str, file_filter: Callable = None) -> tuple[str, tuple[str], tuple[str]]:
    for root, folders, files in os.walk(start_folder):
        if file_filter is None:
            filtered_files = files
        else:
            filtered_files = *map(lambda x: file_filter(root, x), files),
        yield root, folders, filtered_files
