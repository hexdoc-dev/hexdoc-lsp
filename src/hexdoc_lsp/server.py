from lsprotocol.types import (
    NotebookDocumentSyncOptions,
    NotebookDocumentSyncOptionsNotebookSelectorType2,
    NotebookDocumentSyncOptionsNotebookSelectorType2CellsType,
)
from pygls.server import LanguageServer

from hexdoc_lsp.__version__ import VERSION

LANGUAGE_ID = "hexcasting"

SERVER = LanguageServer(
    name="hexdoc",
    version=VERSION,
    max_workers=5,
    notebook_document_sync=NotebookDocumentSyncOptions(
        notebook_selector=[
            NotebookDocumentSyncOptionsNotebookSelectorType2(
                cells=[
                    NotebookDocumentSyncOptionsNotebookSelectorType2CellsType(
                        language=LANGUAGE_ID
                    )
                ]
            )
        ],
        save=True,
    ),
)


def start():
    SERVER.start_io()


if __name__ == "__main__":
    start()
