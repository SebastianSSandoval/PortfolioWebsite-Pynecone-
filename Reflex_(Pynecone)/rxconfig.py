import reflex as rx

class ReflexpyneconewebsiteConfig(rx.Config):
    pass

config = ReflexpyneconewebsiteConfig(
    app_name="Reflex_(Pynecone)_Website",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)