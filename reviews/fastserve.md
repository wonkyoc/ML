---
title: "Fast Distributed Inference Serving for Large Language Models"
authors: "Bingyang Wu, Xin Jin"
affiliation: "Peking University"
conf: None
year: None
url: "https://arxiv.org/pdf/2305.05920.pdf"
--- 

* FastServe exploits the autoregressive pattern of LLM inference to enable preemption at the granularity of each output token
* Job Completion Time (JCT): the length of the time interval between a job's arrival to its completion.
* Inference serving is critical to interactive AI applications based on LLMs.
* autoregressive pattern: LLM inference job contains multipler iterations
    * execution time depends on both the input time and the output length
* Existing inference serving solutions are designed for deterministic model inference jobs (Clockwork / Shepherd)
* Problem: execution time is unknown in LLM (autoregressive)
* Multi-Level Feedback Queue (MLFQ)

Methodology
* AWS EC2 p4d.24xlarge + 8 NVIDIA A100 40GB
