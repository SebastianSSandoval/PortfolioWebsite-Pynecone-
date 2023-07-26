"""Welcome to Reflex! This file outlines the steps to create a basic app."""


from rxconfig import config
import reflex as rx
from .navbar import navbar
from .about import about


docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"
# this still doesn;'t fucking work
style = {
    "::selection": {
        "background_color": "#a3273c",
    },
    rx.Divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.Heading: {
        "font_weight": "500",
    },
    rx.Code: {
        "color": "#f81ce5",
    },
}

class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        
        rx.vstack(
            navbar(),
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State, style = style)
app.add_page(index)
app.add_page(about)
app.compile()


"""light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)"""