# GeneTuring

**GeneTuring** is a benchmarking suite for evaluating genomic reasoning in large language models (LLMs). It accompanies the manuscript:

> Shang, X., Ji, Z., and Hou, W.*, 2025. _Benchmarking large language models for genomic knowledge with GeneTuring_. bioRxiv.  
> 📄 [Read the paper](https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2)

---

## 📁 Contents

### 🔹 1. Benchmark Q&A Dataset

This repo includes a supplementary table with **48,303 Q&A pairs**:  
`16 genomic modules × 10 LLMs × 3 replicates`

**16 Modules**: Gene name extraction, Gene alias, Gene name conversion, Gene location, SNP location, Gene–SNP association, Protein–coding genes, Gene–disease association, Gene ontology, TF regulation, Human/Multi-species DNA alignment (basic & programming), Amino acid translation, DNA sequence extraction.

**10 LLM settings**: BioGPT, BioMedLM, GPT-3.5, GPT-4o, Claude 3.5 Sonnet, Gemini Advanced, GPT-4o (web), GeneGPT (slim), GeneGPT (full), SeqSnap

---

### 🌟 2. [SeqSnap](https://chatgpt.com/g/g-67c52efdc210819190a9532f264ec9c0-seqsnap)

A GPT-based tool built using OpenAI’s GPT Builder to showcase **API-driven execution** for sequence alignment. Instead of relying only on training data, the app integrates the **NCBI BLAST and E-utilities APIs** to:

- Accept and submit DNA alignment queries  
- Retrieve and explain results from the NCBI database  
- Decide when external tools are needed


This GPT-s app can be accessed here: [link](https://chatgpt.com/g/g-67c52efdc210819190a9532f264ec9c0-seqsnap).
The primary idea of this design has been demonstrated in [GeneGPT](https://doi.org/10.1093/bioinformatics/btae075) (Jin et al., 2024), but we build it on our own based on the more advanced GPT-4o model (thanks to Xinyi Shang) to validate this idea.

---

## ❓ Questions or Issues

Please contact **Dr. Wenpin Hou** at 📧 wp.hou3@gmail.com or open an issue.

---

## 📖 Citation

> Shang, X., Xu, L., Ji, Z., and Hou, W.*, 2025. _Benchmarking large language models for genomic knowledge with GeneTuring_. bioRxiv.  
> [https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2](https://www.biorxiv.org/content/10.1101/2023.03.11.532238v2)
