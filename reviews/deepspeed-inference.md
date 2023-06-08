---
title: "DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale"
authors: "Reza Yazdani, ..., Yuxiong He"
affiliation: Microsoft
conf: "SC"
year: 2022
url: 
--- 


Motivation
* using a transformer based model for online scenarios in production requires meeting stringent latency requirements, and thus the batch sizes used are generally small

Key aspects
(1) a multi-GPU inference solution to minimize latency while maximizing the throughput of both dense and sparse transformer models when they fit in aggregate GPU memory
(2) a memory in addition to the GPU memory and compute to enable high inference throughput with large models which do not fit in aggregate GPU memory


* tensor and pipeline parallelism work only for dense transformers
* expert parallelism works only for sparse transformers

Three-layered system architecture (DeepSpeed Transformer)
(1) Single GPU transformer kernels optimized for memory bandwidth utilization at low batch / high tp at large batch
(2) many-GPU dense transformer layer => tensor slicing / interence-optimized pipeline parallelism
(3) massive-GPU scale sparse transformer

ZeRO-Inference: heterogeneous GPU+CPU+NVMe


Inference-optimized transformer kernels
* custom GeMM (General Matrix Multiply) kernel designed for improving the memory bandwidth utilization when the batch size is relatively small
