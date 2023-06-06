import pynecone as pc

config = pc.Config(
    app_name="Pynecone Website 2",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
