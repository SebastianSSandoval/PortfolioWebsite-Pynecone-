import reflex as rx
from .navbar import navbar



def sandbox(): 
    return rx.center(
            rx.vstack(
                navbar(),
                rx.text("Sandbox Thingy"),
                rx.text("this is gonna be where i fuck aronud and find out")))
            
