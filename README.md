# GeneTuring

**GeneTuring** is a benchmarking suite and resource for evaluating the genomic reasoning capabilities of large language models (LLMs). This repository contains supplementary materials and tools associated with the manuscript:

> Shang, X., Ji, Z., and Hou, W.*, 2025. _Benchmarking large language models for genomic knowledge with GeneTuring_. bioRxiv, January 5, 2025.  
> [https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2](https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2)

---

## 📁 Contents

### 1. GeneTuring Benchmark Q&A Dataset

This repository includes a supplementary table with **33,600 Q&A pairs** generated and manually scored across:

- **16 genomic modules**  
  - Gene name extraction  
  - Gene alias  
  - Gene name conversion  
  - Gene location  
  - SNP location  
  - Gene SNP association  
  - Protein–coding genes  
  - Gene disease association  
  - Gene ontology  
  - TF regulation  
  - Human genome DNA alignment  
  - Multi–species DNA alignment  
  - Human genome DNA alignment programming  
  - Multi–species DNA alignment programming  
  - Amino acid translation  
  - DNA sequence extraction

- **7 LLMs (or variants)**  
  - BioGPT  
  - BioMedLM  
  - GPT-3.5  
  - GPT-4o  
  - Claude 3.5 Sonnet  
  - Gemini Advanced  
  - GPT-4o (web)

- **3 replicates per LLM per module**

This dataset enables granular comparison of model behavior across a wide range of genomic tasks.

---

### 2. GPT-s App: Genetic Alignment BLAST

This repository also includes a GPT-based application, **Genetic Alignment BLAST**, which demonstrates the feasibility of **API-driven execution** for sequence alignment tasks.

The app integrates the **NCBI BLAST API** using GPT Actions. It allows the model to:
- Recognize when an external database query is needed
- Submit and track BLAST jobs via NCBI
- Retrieve and present alignment results programmatically

> The concept of integrating NCBI API with LLMs was previously described in  
> GeneGPT (Jin, Qiao, et al., *Bioinformatics* 40.2 (2024): btae075).

---

## ❓ Questions or Issues

For questions or feedback, please contact:

**Dr. Wenpin Hou**  
📧 wp.hou3@gmail.com

Or open an issue in this repository.

---

## 📖 Citation

If you use the GeneTuring benchmark or the Genetic Alignment BLAST app, please cite:

> Shang, X., Ji, Z., and Hou, W.*, 2025. _Benchmarking large language models for genomic knowledge with GeneTuring_. bioRxiv, January 5, 2025.  
> [https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2](https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2)

