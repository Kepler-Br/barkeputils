import os
from typing import Callable, Iterable


def walk_files(
        start_folder: str,
        file_filter: Callable[[str], bool] = None,
        folder_filter: Callable[[str], bool] = None
) -> tuple[str, tuple[str], tuple[str]]:
    for root, folders, files in os.walk(start_folder, topdown=True):
        if file_filter is None:
            filtered_files = files
        else:
            filtered_files = *filter(lambda x: file_filter(x), files),

        if folder_filter is not None:
            folders[:] = *filter(lambda x: folder_filter(x), folders),

        yield root, folders, filtered_files
