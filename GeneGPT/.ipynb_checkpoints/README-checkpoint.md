# GeneGPT Implementation

GeneGPT is one of the large language models (LLMs) evaluated in the **GeneTuring** benchmarking project. This implementation is based on the original GeneGPT framework developed by NCBI. Original code can be found in https://github.com/ncbi/GeneGPT.

## Implementation Details

Original GeneGPT was using code-davinci model from OpenAI, but now it is deprecated. Therefore, in Geneturing project, GeneGPT was implemented using **GPT-3.5 Turbo** (gpt-3.5-turbo-16k, https://platform.openai.com/docs/models/gpt-3.5-turbo-16k-0613). The implementation includes two variants:

- **Slim Model**: Uses Dm.1 and Dm.4 documents for in-context learning
- **Full Model**: Uses all available documents and demonstrations.

This GeneGPT implementation was specifically adapted for the GeneTuring benchmarking suite to evaluate genomic reasoning capabilities across multiple tasks.

## Usage

The main implementation is provided in `demo_GeneGPT.ipynb` notebook. To use the implementation:

### Setup
1. **Configure OpenAI API Key:**
   ```python
   client = openai.OpenAI(api_key='YOUR_KEY') # Please put your OpenAI key here
   ```

2. **Select Model Variant:**
   ```python
   str_mask = '111111' # full model is 111111, slim model is 001001
   ```

### Key Components:
- **String Mask System**: Six-digit binary string controls which in-context learning components are used (Dc.1-2, Dm.1-4)
- **Prompt Engineering**: Uses `get_prompt_header()` function to generate appropriate prompts based on selected components
- **Batch Processing**: Processes questions from `Q&A_dataset.csv` across multiple genomic modules
- **API Management**: Includes safe API calling with proper error handling and rate limiting
- 
## Reference

> Jin, Q., Yang, Y., Chen, Q., & Lu, Z. (2024). Genegpt: Augmenting large language models with domain tools for improved access to biomedical information. *Bioinformatics*, 40(2), btae075.
