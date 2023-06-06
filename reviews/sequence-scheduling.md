* Our approach begins by tapping into the potential of LLMs to accurately perceive and predict the response length with minimal overhead
* Problem: when performing LLM inference in batches, the inclusion of sequences with differing response lengths leads to inefficiencies.
    * When instructions with highly disparate response lengths are batched together, significant and redundant computations occurs, resulting in reduced inference throughput
* Leveraging the response length perception ability of LLMs, we can employ it to enhance the scheduling of instructions within micro-batches
* Perception in Advance (PiA): a modification to the original prompt by including an instruction to estimate the response length in advance.
* Error(w) measures the difference between the estimated number of words and the actual word number
* Side effect: the model can perceive the setimated length as a constraint and attempt to tailor its response to fit the predicted length.


* Instruction tuning:
* What's throughput? samples?
