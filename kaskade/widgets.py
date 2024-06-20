from pyfiglet import Figlet
from rich.table import Table
from rich.text import Text
from textual.app import ComposeResult, RenderResult
from textual.keys import Keys
from textual.widget import Widget
from textual.widgets import Static

from kaskade import APP_NAME, APP_VERSION
from kaskade.colors import PRIMARY, SECONDARY
from kaskade.models import Cluster


class Shortcuts(Widget):
    def __init__(self, cluster: Cluster):
        super().__init__()
        self.cluster = cluster

    def render(self) -> RenderResult:
        table = Table(box=None, show_header=False, padding=(0, 0, 0, 1))
        table.add_column(style=f"bold {PRIMARY}", justify="right")
        table.add_column(style=f"bold {SECONDARY}")

        table.add_row("cluster id:", self.cluster.id)
        table.add_row("controller:", str(self.cluster.controller))
        table.add_row("nodes:", str(len(self.cluster.nodes)))
        table.add_row("help:", "?")
        table.add_row("quit:", Keys.ControlC)

        return table


class KaskadeBanner(Widget):
    def __init__(self, include_version: bool = False, include_slogan: bool = False):
        super().__init__()
        self.include_slogan = include_slogan
        self.include_version = include_version

    def render(self) -> Text:
        figlet = Figlet(font="standard")
        text = Text(figlet.renderText(APP_NAME).rstrip(), style=f"{PRIMARY} bold")

        if self.include_version:
            text.append(f"\nv{APP_VERSION}", style=f"{SECONDARY}")

        if self.include_slogan:
            text.append("\na kafka text user interface", style=f"{SECONDARY}")

        return text


class Header(Static):
    def __init__(self, cluster: Cluster):
        super().__init__()
        self.cluster = cluster

    def compose(self) -> ComposeResult:
        yield KaskadeBanner(include_version=True)
        yield Shortcuts(self.cluster)
