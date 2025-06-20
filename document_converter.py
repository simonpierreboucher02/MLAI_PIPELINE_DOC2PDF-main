import os
import re
import logging
import time
import hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue, Empty

from docx2pdf import convert
from pathlib import Path
import logging

class DocumentConverter:
    """
    Classe pour convertir des fichiers .doc et .docx en PDF.
    
    Cette classe gère la conversion de documents Word en fichiers PDF, 
    en traitant les conversions par lots et en enregistrant les résultats 
    dans un répertoire spécifié. Elle utilise le multithreading pour accélérer 
    le processus et intègre un système de logging pour suivre l'activité et 
    les erreurs.
    
    Attributes:
        input_dir (Path): Répertoire contenant les fichiers Word à convertir.
        output_dir (Path): Répertoire où les fichiers PDF convertis seront enregistrés.
        logger (logging.Logger): Logger pour enregistrer les informations et les erreurs.
        max_workers (int): Nombre maximal de threads pour le traitement concurrent.
    """

    def __init__(self, config, logger=None):
        """
        Initialise le DocumentConverter avec les répertoires d'entrée et de sortie 
        ainsi que d'autres configurations nécessaires.
        
        Args:
            config (dict): Dictionnaire contenant les paramètres de configuration chargés 
                           depuis config.yaml.
            logger (logging.Logger, optional): Logger pour enregistrer les logs. Defaults à None.
        """
        # Configure paths
        self.input_dir = Path(config['input_dir'])
        self.output_dir = Path(config['output_dir'])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Setup logger
        self.logger = logger or logging.getLogger(__name__)

        # Conversion settings
        self.max_workers = config.get('max_workers', 10)

    def convert_documents(self):
        """
        Convertit tous les fichiers .doc et .docx dans le répertoire d'entrée en PDF 
        et les enregistre dans le répertoire de sortie.
        """
        try:
            # Recherche des fichiers .doc et .docx
            doc_files = list(self.input_dir.glob('*.doc')) + list(self.input_dir.glob('*.docx'))
            total_files = len(doc_files)
            self.logger.info(f"📢 Début de la conversion de {total_files} fichiers.")

            if total_files == 0:
                self.logger.warning(f"Aucun fichier DOC ou DOCX trouvé dans le dossier : {self.input_dir}")
                return

            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                # Lancer toutes les tâches de conversion
                future_to_doc = {executor.submit(self.convert_single_document, doc_file): doc_file for doc_file in doc_files}

                for future in as_completed(future_to_doc):
                    doc_file = future_to_doc[future]
                    try:
                        success = future.result()
                        if success:
                            self.logger.info(f"✅ Conversion réussie: {doc_file.name}")
                        else:
                            self.logger.warning(f"⚠️ Conversion échouée: {doc_file.name}")
                    except Exception as e:
                        self.logger.error(f"❌ Exception lors de la conversion de {doc_file.name}: {str(e)}")

            self.logger.info("🎉 Toutes les conversions sont terminées.")

        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la recherche des fichiers: {str(e)}")

    def convert_single_document(self, doc_path):
        """
        Convertit un fichier .doc ou .docx en PDF.
        
        Args:
            doc_path (Path): Chemin vers le fichier Word à convertir.
        
        Returns:
            bool: True si la conversion a réussi, False sinon.
        """
        try:
            # Définir le chemin complet pour le fichier PDF de sortie
            output_pdf = self.output_dir / f"{doc_path.stem}.pdf"
            convert(str(doc_path), str(output_pdf))
            return True
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la conversion de {doc_path.name}: {str(e)}")
            return False
