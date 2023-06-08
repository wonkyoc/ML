---
title: "High-throughput Generative Inference of Large Language Models with a Single GPU"
authors: "Ying Sheng, ..., Ion Stoica, Ce Zhang"
affiliation: "ETH Zurich/UC Berkeley"
conf: ICML
year: 2023
url: 
---


Contribution
* offloading strategies: computation schedule, tensor placement, and computation delegation
* Compression for the weights and KV cache for LLMs (4bits)
* allows a batch size that is orders of magnitude larger

Problem formulation
* a GPU, a CPU, and a disk form a three-level memory hierarchy where the GPU has the smallest but fastest memory and the disk has the largest but slowest memory.
    * When a LLM cannot fit entirely within the GPU, the system needs to offload it to secondary storage and perform computation part-by-part by partially loading the LLM.

Existing Problem
* Every two contiguous squares do not share weights, this schedule has to repeatedly load the weights and incurs huge I/O costs.


Key Idea
* a zig-zag block schedule: all squares in a column share weights, so we can let the weights stay on GPU for reusing and only load/unload the activations and KV cache.
* But, processing a row comes in when KV cache fills the GPU and disk memory 


Another technique:
* Overlapping: overlaps the weights load of the next layer
* tensor placement: layar granularity for weights, and tensor granularity for activations and the KV cache
* group-wise quantization: both the weights and KV cache can be directly quantized into 4-bit integers

Generative Inference
(1) prefix stage: takes a prompt sequence to generate the key-value cache for each transformer layer
(2) decoding stage: utilizes and updates the KV cache to generate tokens step-by-step

Memory analysis
* The memory footprint of LLM inference mainly comes from two components: the model weights and the KV cache

* The latency t is defined as the total number of seconds spent to process the prompts and generate all the bn tokens
* The generation throughput is defined as bn/t token/s


Group-wise quantization
* Given a tensor, we choose g contiguous elements along a certain dimension as a group. For each group, we Comput the min and max of the group elements and quantize each element x into b-bit integers by x_quant = round(something)

* FlexGen turns off the CPU delegation when enabling quantization

Sparse Attention
* FlexGen loads the top 10% attention value cache on OPT-175B.
* After computing the attention matrices, for each query, FlexGen calculates the indices of its Top-K tokens from the K cache. Then, it simple drops the other tokens and only load a subset of the V cache according to the indices.
