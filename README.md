# MLAI PDF Pipeline Extractor

[![GitHub stars](https://img.shields.io/github/stars/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.svg?style=social&label=Star)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![GitHub forks](https://img.shields.io/github/forks/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.svg?style=social&label=Fork)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![GitHub issues](https://img.shields.io/github/issues/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main/issues)
[![GitHub license](https://img.shields.io/github/license/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/badge/PyPI-docx2pdf-green.svg)](https://pypi.org/project/docx2pdf/)
[![PyPI](https://img.shields.io/badge/PyPI-PyYAML-green.svg)](https://pypi.org/project/PyYAML/)
[![PyPI](https://img.shields.io/badge/PyPI-tqdm-green.svg)](https://pypi.org/project/tqdm/)
[![PyPI](https://img.shields.io/badge/PyPI-rich-green.svg)](https://pypi.org/project/rich/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main/graphs/commit-activity)
[![Made with Love](https://img.shields.io/badge/Made%20with-Love-red.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main#readme)
[![Code Quality](https://img.shields.io/badge/Code%20Quality-Excellent-blue.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Multithreading](https://img.shields.io/badge/Multithreading-Supported-orange.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Logging](https://img.shields.io/badge/Logging-Comprehensive-yellow.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)
[![Error Handling](https://img.shields.io/badge/Error%20Handling-Robust-red.svg)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)

## 📊 Repository Metrics

| Metric | Value |
|--------|-------|
| **Total Files** | 5 |
| **Lines of Code** | ~500+ |
| **Python Files** | 2 |
| **Configuration Files** | 1 |
| **Documentation** | Complete |
| **Dependencies** | 5 |
| **Supported Formats** | .doc, .docx → PDF |
| **Threading Support** | ✅ |
| **Error Handling** | ✅ |
| **Logging** | ✅ |

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Configuration Parameters](#configuration-parameters)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Output](#output)
- [Logging and Reports](#logging-and-reports)
- [Crawler Statistics](#crawler-statistics)
- [Crawler Performance](#crawler-performance)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## Introduction

**MLAI PDF Pipeline Extractor** is a robust and efficient tool designed to convert Word documents (`.doc` and `.docx`) into PDF files. Leveraging Python's powerful libraries, this extractor automates the conversion process, ensuring high-quality outputs with proper logging and error handling. Whether you're managing large volumes of documents or integrating this tool into a larger workflow, MLAI PDF Pipeline Extractor offers flexibility and reliability.

## Features

- **Batch Conversion**: Convert multiple `.doc` and `.docx` files in bulk.
- **Multithreading**: Utilize multiple threads for faster processing.
- **Configurable Settings**: Manage all configurations via an external YAML file.
- **Robust Logging**: Comprehensive logging to both console and log files.
- **Error Handling**: Gracefully handles errors and logs them for review.
- **Future-Proof Architecture**: Easily extendable to integrate additional functionalities like LLM processing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Operating System**: Windows, macOS, or Linux.
- **Python**: Python 3.7 or higher installed. Download from [Python.org](https://www.python.org/downloads/).
- **Git**: For cloning the repository. Download from [Git-SCM.com](https://git-scm.com/downloads).
- **Microsoft Word**: Required by `docx2pdf` for conversion. Ensure Word is installed on your system.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.git
   cd MLAI_PIPELINE_DOC2PDF-main
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **Windows**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Verify Microsoft Word Installation**

   Ensure that Microsoft Word is installed and accessible, as `docx2pdf` relies on it for conversions.

## Configuration

The extractor utilizes a YAML configuration file (`config.yaml`) to manage its settings. This allows for easy adjustments without modifying the core code.

### Configuration Parameters

**`config.yaml`**

```yaml
# Configuration for DocumentConverter

# Directories
input_dir: "path/to/your/input_documents"    # Replace with the path to your input Word documents
output_dir: "path/to/output_pdfs"           # Replace with the path where you want to save the converted PDFs

# Conversion Settings
max_workers: 4                              # Number of threads for parallel processing

# Logging Settings
logging:
  log_file: "document_converter.log"        # Log file name
  log_level: "INFO"                         # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# LLM (GPT-4) Configuration (Future Integration)
llm:
  model: "gpt-4"                             # LLM model to use
  system_prompt: |
    You are a document conversion expert. Your task is to:
    1. Ensure that all converted PDFs maintain the original formatting of the Word documents.
    2. Optimize the PDF files for readability and accessibility.
  temperature: 0                             # Temperature setting for LLM
  max_tokens: 4000                           # Maximum tokens for LLM response
  top_p: 1                                   # Top-p sampling for LLM
  frequency_penalty: 0                       # Frequency penalty for LLM
  presence_penalty: 0                        # Presence penalty for LLM

# Chunking Settings (Future Integration)
chunk_split: 4000                              # Maximum length of each text chunk for LLM processing

# Additional Settings (If Needed)
# You can add more settings here as your project grows.
```

**Notes:**

- **`input_dir`**: Directory containing the `.doc` and `.docx` files you wish to convert.
- **`output_dir`**: Directory where the converted PDF files will be saved.
- **`max_workers`**: Number of threads to use for concurrent conversions. Adjust based on your system's capabilities.
- **Logging**:
  - **`log_file`**: Name of the log file.
  - **`log_level`**: Determines the verbosity of logs. Options include `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
- **LLM Configuration**: Reserved for future integrations with language models like GPT-4 for advanced processing tasks.
- **Chunking Settings**: Prepares the framework for splitting text into manageable chunks for LLM processing.

### 2. Update Paths and Parameters

- **`input_dir`**: Replace `"path/to/your/input_documents"` with the actual path to your Word documents.
- **`output_dir`**: Replace `"path/to/output_pdfs"` with the desired output directory path.
- **`max_workers`**: Adjust based on your system's capabilities for optimal performance.

## Usage

After completing the installation and configuration, you can start the converter using the provided `main.py` script.

```bash
python main.py
```

### Steps Performed by the Converter

1. **Load Configuration**: Reads settings from `config.yaml`.
2. **Initialize Converter**: Sets up directories and logging based on configurations.
3. **Document Conversion**: Iterates through each Word document in the input directory and converts them to PDF.
4. **Logging**: Records all actions, successes, and errors to the log file and console.
5. **Completion**: Notifies upon completion of all conversions.

## Project Structure

```
MLAI_PIPELINE_DOC2PDF-main/
├── config.yaml
├── main.py
├── document_converter.py
├── requirements.txt
├── README.md
├── api_keys.txt                      # Your OpenAI API keys, one per line (future use)
├── logs/                             # Created after running the converter
│   └── document_converter.log
├── output_pdfs/                      # Created based on config.yaml
│   ├── Document1.pdf
│   ├── Document2.pdf
│   └── ...                            # Other converted PDF files
└── input_documents/                  # Your input Word documents
    ├── sample1.doc
    ├── sample2.docx
    └── ...
```

**Notes:**

- **`api_keys.txt`**: Reserved for future integration with language models like GPT-4.
- **`logs/`**: Contains the `document_converter.log` file detailing the conversion process.
- **`output_pdfs/`**: Contains the converted PDF files.
- **`input_documents/`**: Place all your `.doc` and `.docx` files here for conversion.

## Output

Upon running the converter, the following outputs are generated based on your `config.yaml`:

- **Converted PDF Files**: Located in the `output_dir` directory, maintaining the original document names with a `.pdf` extension.
- **Logs**: Detailed logs are maintained in `logs/document_converter.log`, recording all actions, successes, and errors.

## Logging and Reports

- **Logging**: All actions, warnings, and errors are logged both to the console and to the `document_converter.log` file in the `logs/` directory.
  
  **Example Log Entries:**
  
  ```
  2023-10-05 12:00:00 - INFO - 📢 Début de la conversion de 10 fichiers.
  2023-10-05 12:00:01 - INFO - 🔄 Conversion de sample1.docx en PDF.
  2023-10-05 12:00:02 - INFO - ✅ Conversion réussie: sample1.pdf
  ...
  2023-10-05 12:05:00 - INFO - 🎉 Toutes les conversions sont terminées.
  ```

- **Reports**: Currently, the converter focuses on logging. Future integrations may include automated reports summarizing conversion statistics.

## Crawler Statistics

Here are example statistics showcasing the performance of your Document Converter. These metrics should be updated based on actual usage.

| Metric                    | Value               |
|---------------------------|---------------------|
| Total Documents Converted | 100                 |
| Success Rate              | 98%                 |
| Conversion Failures       | 2%                  |
| Total Duration            | 3 hours             |

*Note: Update these metrics based on your actual usage.*

## Crawler Performance

![Crawler Performance](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main/assets/performance-chart.png)

*Replace the above URL with the actual path to your performance chart image.*

## Troubleshooting

- **Microsoft Word Not Found Error**:
  - Ensure that Microsoft Word is installed on your system, as `docx2pdf` relies on it for conversions.
  - Verify that Word is accessible and not running in a restricted mode.

- **Permission Errors**:
  - Ensure the script has read permissions for the `input_dir` and write permissions for the `output_dir` and log files.

- **Invalid Configurations**:
  - Double-check the `config.yaml` file for correct paths and parameter values.
  - Ensure that all necessary directories exist or are correctly specified in the configuration.

- **High CPU or Memory Usage**:
  - Adjust the `max_workers` parameter in `config.yaml` based on your system's capabilities to prevent resource exhaustion.

## Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Simon Pierre Boucher**
- GitHub: [@simonpierreboucher02](https://github.com/simonpierreboucher02)
- Repository: [MLAI_PIPELINE_DOC2PDF-main](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)

## Acknowledgements

- Thanks to the `docx2pdf` library for providing the core conversion functionality
- PyYAML for configuration management
- The Python community for excellent documentation and support
- All contributors and users of this project

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main.svg?style=social&label=Star)](https://github.com/simonpierreboucher02/MLAI_PIPELINE_DOC2PDF-main)

</div>

