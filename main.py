import sys
import yaml  # Ensure PyYAML is installed
from document_converter import DocumentConverter  # Ensure document_converter.py is in the same directory or Python path
import logging
from pathlib import Path

def load_config(config_path="config.yaml"):
    """
    Charge et analyse le fichier de configuration YAML.

    Args:
        config_path (str): Chemin vers le fichier de configuration.

    Returns:
        dict: Dictionnaire contenant les paramètres de configuration.
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        print(f"✅ Configuration chargée depuis {config_path}")
        return config
    except FileNotFoundError:
        print(f"✘ Fichier de configuration {config_path} introuvable.")
        sys.exit(1)
    except yaml.YAMLError as exc:
        print(f"✘ Erreur lors de l'analyse du fichier YAML: {exc}")
        sys.exit(1)

def setup_logging(log_file, log_level):
    """
    Configure le système de logging.

    Args:
        log_file (str): Chemin vers le fichier de log.
        log_level (str): Niveau de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL).

    Returns:
        logging.Logger: Instance du logger configuré.
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        print(f"✘ Niveau de logging invalide: {log_level}")
        sys.exit(1)

    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger('DocumentConverter')
    return logger

def main():
    """
    Fonction principale pour initialiser et exécuter le DocumentConverter.
    """
    # Charger la configuration depuis config.yaml
    config = load_config("config.yaml")

    # Configurer le logging
    log_file = config.get('logging', {}).get('log_file', 'document_converter.log')
    log_level = config.get('logging', {}).get('log_level', 'INFO')
    logger = setup_logging(log_file, log_level)

    # Vérifier que le répertoire d'entrée existe
    input_dir = Path(config['input_dir'])
    if not input_dir.exists():
        logger.error(f"📁 Le répertoire d'entrée {input_dir} n'existe pas.")
        sys.exit(1)

    # Initialiser le DocumentConverter
    converter = DocumentConverter(
        config=config,
        logger=logger
    )

    # Exécuter la conversion
    converter.convert_documents()

if __name__ == "__main__":
    main()
