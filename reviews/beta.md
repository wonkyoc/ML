---
title: "Beta: Statistical Multiplexing with Model Parallelism for Deep Learning Serving"
authors: "Zhuohan Li, Joseph E. Gonzalez, Ion Stoica"
affiliation: "UC Berkeley"
conf: "OSDI"
year: 2023
url: "https://www.usenix.org/system/files/osdi23-li-zhuohan.pdf"
--- 

* introduce a taxonomy and quantify the tradeoffs between different parallelization strategies in model serving

Intra-operator parallelism
* is when a single operator is partitioned across multiple devices
* benefit (1) it can expand the total amount of computation available to the target model, reducing its end-to-end latency
* benefit (2) it can expand the total memory available to the model for storing its inputs, weights, and intermediate values.

Inter-operator parallelism (pipeline parallelism)
* assigns different operators of the model's execution graph to execute on distributed devices in a pipeline fashion
* incurs the exec time due to modest amounts of commu. latency between pipeline stages
