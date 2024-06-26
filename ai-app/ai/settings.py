from pydantic_settings import BaseSettings


class AISettings(BaseSettings):
    """LLM settings that can be set using environment variables.

    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    gpt_4: str = "gpt-4-1106-preview"
    gpt_4_vision: str = "gpt-4-vision-preview"
    gpt_3_5: str = "gpt-3.5-turbo-1106"
    llama3: str = "llama3"
    nomic_embed_text: str = "nomic-embed-text"
    embedding_model: str = "llama3"
    default_max_tokens: int = 1024
    default_temperature: float = 0


# Create AISettings object
ai_settings = AISettings()
