# TLM o1-preview Benchmark

This folder contains the dataset and the code to reproduce the TLM-o1 benchmark we published in our [blog post](https://cleanlab.ai/blog/tlm-o1/).

For SVAMP and TriviaQA, we specifically selected challenging examples that OpenAI’s GPT-4o model got wrong, as OpenAI’s o1-preview API is still slow and costly to benchmark across larger datasets. For our TriviaQA benchmark, we used 114 examples from the validation set which GPT-4o answered wrong, and we were able to manually confirm the answer listed as ground truth is actually correct. For our SVAMP benchmark, we used 49 examples which GPT-4o answered wrong, and we were able to manually confirm the answer listed as ground truth is actually correct. For our PII Detection benchmark, we specifically focused on identifying first-names present in the text, considering a dataset of 98 examples.

API keys:
- A `CLEANLAB_API_KEY` is required to run this project. Get a Cleanlab API key at https://app.cleanlab.ai/tlm
- An `OPENAI_API_KEY` is also required to run this project. Get an OpenAI key at https://platform.openai.com/api-keys

To reproduce the benchmarks:
- Use the `openai_o1_preview_benchmark_reproduce.ipynb` file to reproduce the OpenAI o1 benchmark.
- Use the `tlm_o1_preview_benchmark_reproduce.ipynb` file to reproduce the TLM o1-preview benchmark.
