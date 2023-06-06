import pynecone as pc

email = "mailto: ssandoval2024@gmail.com"
resume = "https://docs.google.com/document/d/1BmoNPtsYkZg9DD2P7xYZ2eeE90nNUGhXOXWJXO6ttCw/edit?usp=sharing"
yt_vid = "https://youtu.be/QdnVT22LBBs"



def navbar():
    return pc.box(
            pc.hstack(
                pc.heading("My Purgatory: The Sequel"),
                pc.spacer(),
                pc.spacer(),
                pc.spacer(),
                pc.button_group(
                    pc.link(pc.button("About",bg = "navy", color = "white"),href = "/about",button = True),
                    pc.link(pc.button("Resume",bg = "lightblue", color = "white"),href = resume , button = True, is_external = True),
                    pc.link(pc.button("yt vid",bg = "black", color = "white"),href = yt_vid, button = True, is_external = True),
                    pc.link(pc.button("Email",bg = "red", color = "white"),href = email, button = True),
                    is_attached = False
                    )
                    )
    )
    