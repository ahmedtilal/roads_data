from airflow.plugins_manager import AirflowPlugin


class CustomPlugin(AirflowPlugin):
    name = 'custom_plugin'
    operators = []
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []