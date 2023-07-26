import reflex as rx

email = "mailto: ssandoval2024@gmail.com"
resume = "https://docs.google.com/document/d/1BmoNPtsYkZg9DD2P7xYZ2eeE90nNUGhXOXWJXO6ttCw/edit?usp=sharing"
yt_vid = "https://youtu.be/QdnVT22LBBs"



def navbar():
    return rx.box(
            rx.hstack(
                rx.heading("My Purgatory: The Sequel", ),
                rx.spacer(),
                rx.spacer(),
                rx.spacer(),
                rx.button_group(
                    rx.link(rx.button("About",bg = "navy", color = "white"),href = "/about",button = True), 
                    rx.link(rx.button("Resume",bg = "lightblue", color = "white"),href = resume , button = True, is_external = True),
                    rx.link(rx.button("yt vid",bg = "black", color = "white"),href = yt_vid, button = True, is_external = True),
                    rx.link(rx.button("Email",bg = "red", color = "white"),href = email, button = True),
                    rx.link(rx.button(rx.icon(tag="moon"),on_click=rx.toggle_color_mode)), # 7/21/2023 had to make this a "link" so that it stays within line
                    is_attached = False
                    )
                    )
    )