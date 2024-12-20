# Benchmark hallucination detection models on RAG datasets

This folder contains notebooks used to evaluate popular hallucination detection models on various RAG (Context, Question, LLM Response) datasets.

The datasets used in the benchmark include:
- [Halubench](https://huggingface.co/datasets/PatronusAI/HaluBench):
    - CovidQA
    - PubmedQA
    - DROP
    - FinanceBench
- [ELI5](https://huggingface.co/datasets/explodinggradients/ELI5)


The following table lists the models evaluated:

| Notebook                                                                                | Description                                                                                                                               |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [Patronus Lynx](Lynx.ipynb) | Evaluates [Patronux Lynx 70B](https://huggingface.co/PatronusAI/Llama-3-Patronus-Lynx-70B-Instruct) model
| [Vectara HHEM](HHEM.ipynb) | Evaluates [Vectara's HHEM v2.1](https://huggingface.co/vectara/hallucination_evaluation_model) model
| [Prometheus 2](Prometheus.ipynb) | Evaluates [Prometheus2 8x7B](https://huggingface.co/prometheus-eval/prometheus-8x7b-v2.0) model
| [LLM as judge and TLM](LLM_as_judge_and_TLM.ipynb) | Evaluates LLM-as-judge and the Trustworthy Language Model on ELI5 dataset
| [LLM as judge and TLM](../benchmarking_hallucination_metrics/benchmark_hallucination_metrics.ipynb) | Evaluates LLM-as-judge and the Trustworthy Language Model on Halubench datasets |
