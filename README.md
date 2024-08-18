
# Chatbot RAG

Chatbot RAG is a Python-based Retrieval-Augmented Generation (RAG) chatbot that leverages the power of document retrieval and generation models to provide contextually accurate and enriched responses. This project combines cutting-edge natural language processing (NLP) techniques with retrieval-based methods to enhance the chatbot's ability to understand and generate human-like responses.

## Features

- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval with language model generation for more accurate responses.
- **Contextual Memory**: Builds a memory of conversations to maintain context across interactions.
- **Multi-Model Support**: Supports multiple models optimized for local execution.
- **GPU Acceleration**: Capable of running on GPU for faster processing and inference.
- **Customizable Retrieval Strategies**: Offers different strategies for document retrieval and response synthesis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Anonymous3017/chatbot_rag.git
   cd chatbot_rag
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment:
   - Ensure you have the required models and data available.
   - Configure any environment variables as needed.

4. Run the application:
   ```bash
   python app/main.py
   ```

## Usage

- The chatbot can be customized for various applications, including customer support, personal assistants, and more.
- You can modify the retrieval strategies and models in the configuration files to suit your specific needs.
- The utility functions in `utils.py` help manage data processing, model interactions, and other essential tasks.

## File Structure

- `app/main.py`: Entry point for running the chatbot application.
- `app/main/utils.py`: Utility functions used throughout the application.
- `app/config/`: Configuration files for setting up models, retrieval strategies, etc.
- `data/`: Directory for storing data and model files.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
