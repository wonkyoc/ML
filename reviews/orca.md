---
title: "ORCA: A Distributed Serving System for Transformer-based Generative Models"
authors: ["Gyeong-In Yu", "Byun-Gon Chun"]
affiliation: "Seoul National University"
conf: "OSDI'23"
url: "https://www.usenix.org/system/files/osdi22-yu.pdf"

---

* iteration-level scheduling: a new scheduling mechanism that schedules execution at the granularity of iteration where the scheduler invokes the execution engine to run only a single iteration of the model on the batch.
    * selective batching + iteration-level scheduling
* Some systems use a separately-developed DNN execution engine to perform the actual tensor operations.
    * Triton / Tensorflow

Problem: running multiple iterations of the model 


Iteration-level scheduling
* Instead of batching all requests, Orca serves each request with a level of iteration

Selective batching
* Orca employees an unique batching strategy that manages the values of attention KV by splitting and merging the attention values, corresponding to each input

How they evaluate

## Background
* Model execution engine: TensorRT / TVM / Tensorflow / PyTorch..


