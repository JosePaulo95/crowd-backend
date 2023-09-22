from app.contexts.config_contexts import contexts_config


def get_all_contexts():
    data = contexts_config()
    return data
