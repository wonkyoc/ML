---
title: "ORCA: A Distributed Serving System for Transformer-based Generative Models"
authors: "Gyeong-In Yu;Byun-Gon Chun"
affiliation: "Seoul National University"
conf: "OSDI"
year: 2022
url: "https://www.usenix.org/system/files/osdi22-yu.pdf"

---

* iteration-level scheduling: a new scheduling mechanism that schedules execution at the granularity of iteration where the scheduler invokes the execution engine to run only a single iteration of the model on the batch.
    * selective batching + iteration-level scheduling
* Some systems use a separately-developed DNN execution engine to perform the actual tensor operations.
    * Triton / Tensorflow

Problem:
* The existing systems serve inference requests as a whole. For instance, if clients request four different requests, the system processes them in a batch.
    * The problem is that one request may finish early and waits for completion of other requests; hence, one of clients experience delayed results.

Iteration-level scheduling
* Instead of batching all requests, Orca serves each request w.r.t a level of iteration
    * iteration: the run of all layers
    * autoregressive procedure: generating a single token is done by running all the layetrs of the model with the input

Selective batching
* Orca employees an unique batching strategy that manages the values of attention KV by splitting and merging the attention values, corresponding to each input
* Operations such as non-Attention matrix multiplication and layer normalization can be made to work with irregularly shaped tensors by flattening the tensors.

How they evaluate
* baseline: FasterTransformer
    * it does not allow injecting another batch before the finish of the current running batch

## Background
* Model execution engine: TensorRT / TVM / Tensorflow / PyTorch..


