# GeneGPT Implementation

GeneGPT is one of the large language models (LLMs) evaluated in the **GeneTuring** benchmarking project. This implementation is based on the original GeneGPT framework developed by NCBI. Original code can be found in https://github.com/ncbi/GeneGPT.

## Implementation Details

Original GeneGPT was using code-davinci model from OpenAI, but now it is deprecated. Therefore, in Geneturing project, GeneGPT was implemented using **GPT-3.5 Turbo** (gpt-3.5-turbo-16k, https://platform.openai.com/docs/models/gpt-3.5-turbo-16k-0613). The implementation includes two variants:

- **Slim Model**: Uses Dm.1 and Dm.4 documents for in-context learning
- **Full Model**: Uses all available documents and demonstrations.

This GeneGPT implementation was specifically adapted for the GeneTuring benchmarking suite to evaluate genomic reasoning capabilities across multiple tasks.

## Reference

Jin, Q., Yang, Y., Chen, Q., & Lu, Z. (2024). Genegpt: Augmenting large language models with domain tools for improved access to biomedical information. *Bioinformatics*, 40(2), btae075.