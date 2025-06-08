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

### 🌟 GPT-s App: Genetic Alignment BLAST

**We developed a GPT-based tool, [Genetic Alignment BLAST](https://chatgpt.com/g/g-67c52efdc210819190a9532f264ec9c0-genetic-alignment-blast), using OpenAI’s GPT Builder platform.**

This app was created to **demonstrate the feasibility of using API-driven execution** to tackle sequence alignment questions more effectively. It can recognize when to call external genomic databases (e.g., the **National Center for Biotechnology Information (NCBI)** database) rather than attempting to generate answers purely from its training data.

To build this GPT, we created an **Action to integrate the NCBI BLAST API**, enabling the GPT to:
- Submit BLAST queries
- Check query status
- Retrieve BLAST results programmatically


**What it does**:

It integrates the NCBI BLAST API into a GPT interface. This means it can:

- Accept DNA sequence alignment queries

- Submit them to the NCBI BLAST service

- Retrieve and explain the results

- Decide when to use external APIs instead of relying on internal training data

The concept of integrating external APIs follows the same approach described in **GeneGPT**:   [Jin, Qiao, et al. _Bioinformatics_ 40.2 (2024): btae075](https://doi.org/10.1093/bioinformatics/btae075).

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

