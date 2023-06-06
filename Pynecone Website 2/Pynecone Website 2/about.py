import pynecone as pc
from .navbar import navbar
def about(): 
    return pc.center(
            pc.vstack(
                pc.text("About Thingy"),
                navbar()))