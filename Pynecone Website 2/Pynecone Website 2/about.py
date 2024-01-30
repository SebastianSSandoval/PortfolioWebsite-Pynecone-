import reflex as rx
from .navbar import navbar
def about(): 
    return rx.center(
            rx.vstack(
                
                navbar(),
                rx.text("About Thingy"),
                rx.text("this is gonna be the about page soon enough")))
