## High-throughput Generative Inference of Large Language Models with a Single GPU

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
