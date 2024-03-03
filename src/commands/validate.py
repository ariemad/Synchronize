from src.check_config import check_config
from src.create_folders import create_folders


def validate():
    check_config()
    create_folders()
