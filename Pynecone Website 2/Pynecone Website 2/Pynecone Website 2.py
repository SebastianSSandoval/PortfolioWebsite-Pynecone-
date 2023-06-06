"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from .navbar import navbar
from .about import about

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


style = {
    "::selection": {
        "background_color": "rgb(86, 77, 209)",
    },
    pc.Text: {
        "font_family": "Inter",
        "font_size": 16,
    },
    pc.Divider: {"margin_bottom": "1em", "margin_top": "0.5em"},
    pc.Code: {
        "color": "rgb(86, 77, 209)",
    },
}

class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            navbar(),
            pc.heading("Still Working on this (send help)", font_size="2em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )




app = pc.App(state=State, style = style)
app.add_page(index)
app.add_page(about, style = style)
app.compile()
