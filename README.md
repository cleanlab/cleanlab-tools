# cleanlab-tools

Cookbooks showcasing various applications of Cleanlab, as well as code shared for education, reproducibility, transparency.


## Detecting LLM Errors with Cleanlab's Trustworthy Language Model

| Example                                                                                | Description                                                                                                                               |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [TLM-Demo-Notebook](TLM-Demo-Notebook/TLM-Demo.ipynb) | Demo-ing various applications of the Trustworthy Language Model, particularly in customer support |
| [tlm_call_api_directly](tlm_call_api_directly/tlm_api_directly.ipynb) | Call the TLM REST API directly. You can use any programming language (eg. Typescript) with http lib/tools by providing the necessary payload and headers. |
| [TLM-PII-Detection](TLM-PII-Detection/TLM-PII-Detection.ipynb) | Find and mask PII with the Trustworthy Language Model |
| [Detecting GDPR Violations with TLM](gdpr_tlm_blog_post/gdpr_tlm_blog_post.ipynb) | Analyze application logs using TLM to detect GDPR violations |   
| [Customer Support AI Agent with NeMo Guardrails](NeMo-Guardrails-Customer-Support/README.md) | Reliable customer support AI Agent with Guardrails and trustworthiness scoring ([Nvidia Blogpost](https://developer.nvidia.com/blog/prevent-llm-hallucinations-with-the-cleanlab-trustworthy-language-model-in-nvidia-nemo-guardrails/)) |
| [Better LLM Evals in MLFlow](TLM-MLflow-Integration/evaluating_traces_TLM_mlflow_dl.ipynb) | Automatically find the bad LLM responses lurking in your production logs/traces via trustworthiness scoring in MLFlow |
| [Trustworthy RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/evaluation/Cleanlab/) | Run Cleanlab in RAG apps built with LlamaIndex for real-time detection of incorrect responses and root cause analysis. |
| [Trustworthy RAG with MongoDB](trustworthyRAG_mongodb_cleanlab.ipynb) | Run Cleanlab in RAG apps built with MongoDB for real-time detection of incorrect responses and root cause analysis. |
| [TLM-Record-Matching](TLM-Record-Matching/data_enrichment_record_matching_tutorial.ipynb) | Using the Trustworthy Language Model to reliably match records between two different data tables |
| [fine_tuning_data_curation](fine_tuning_data_curation/fine_tuning_data_curation.ipynb) | Use Cleanlab TLM and Cleanlab Studio to detect bad data in instruction tuning LLM datasets | 



## Data Curation with Cleanlab Studio

| Example                                                                                | Description                                                                                                                               |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [few_shot_prompt_selection](few_shot_prompt_selection/few_shot_prompt_selection.ipynb) | Clean the pool of few-shot examples to improve prompt template for OpenAI LLM |
| [fine_tuning_classification](fine_tuning_classification/fine_tuning_LLM_with_noisy_labels.ipynb) | Use Cleanlab Studio to improve the accuracy of fine-tuned LLMs for classification tasks |
| [fine_tuning_mistral_beavertails](fine_tuning_mistral_beavertails/beavertails.ipynb) | Analyze human annotated AI-safety-related labels (like toxicity) using Cleanlab Studio, and thus generate safer responses from LLMs |
| [Evaluating_Toxicity_Datasets_Large_Language_Models](jigsaw_ai_safety_keras/Evaluating_Toxicity_Datasets_Large_Language_Models.ipynb) | Analyze toxicity annotations in the Jigsaw dataset using Cleanlab Studio |
| [time_series_automl](time_series_automl/cleanlab_time_series_automl.ipynb) | Model time series data in a tabular format and use Cleanlab Studio AutoML to achieve high prediction accuracy |



## Miscellaneous Code

| Example                                                                                | Description                                                                                                                               |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [TLM-SimpleQA-Benchmark](TLM-SimpleQA-Benchmark/) | Benchmarking TLM and OpenAI LLMs on the SimpleQA dataset |
| [benchmarking_hallucination_metrics](benchmarking_hallucination_metrics/benchmark_hallucination_metrics.ipynb) | Evaluate the performance of popular real-time hallucination detection methods on RAG benchmarks |
| [benchmarking_hallucination_model](benchmarking_hallucination_model/README.md) | Evaluate the performance of popular hallucination detection models on RAG benchmarks |  
| [gpt4-rag-logprobs](gpt4-rag-logprobs/gpt4-rag-logprobs.ipynb) | Obtaining logprobs from a GPT-4 based RAG system |
| [generate_llm_response](generate_llm_response/generate_llm_response.ipynb)             | Generate LLM responses for customer service requests using Llama 2 and OpenAI's API |
