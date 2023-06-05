# Opening up ChatGPT: Surveying open-source instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI&#39;s ChatGPT, a proprietary text generator trained using human feedback to simulate instruction-following. We survey 13 open-source projects of comparable architecture and functionality: large language-models with reinforcement learning from human feedback (RLHF), made for prompt-based text and code generation. The main contribution of this paper is to offer scientific documentation of the fast-moving field of large language models of the instruction-following variety. We review prior work on the importance of openness for transparent and trustworthy AI, and evaluate each project with regards to openness, scientific documentation, and access methods. The paper is accompanied by a version-controlled list that will be updated as new alternatives emerge.

![Open source software survey](./osi-logo.png)

## Contents

- [Overview](#overview)
- [Survey criteria](#survey-criteria)
- [List of Projects](#list-of-projects)

## Overview

Overview of open-source instruction-following text generators surveyed for availability, documentation, and access methods with ChatGPT (bottom) as reference. Key: 1 Base LLM training data, 2 Base LLM model weights 3 RLHF training data, 4 RLHF model weights.

| Project                  |   | Availability                                                                     |            |               |             |                |         | Documentation |              |          |       |            | Access methods |                                                   |
|--------------------------|---|----------------------------------------------------------------------------------|------------|---------------|-------------|----------------|---------|---------------|--------------|----------|-------|------------|----------------|---------------------------------------------------|
| (maker, base model, URL) |   | Open code                                                                        | LLM data ¹ | LLM weights ² | RLHF data ³ | RLHF weights ⁴ | License | Code          | Architecture | Preprint | Paper | Data sheet | Package        | API                                               |
| xmtf                     |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🟢            | 🟢           | 🟢       | 🔴    | 🔴         | 🟢             | 🟢                                                |
| bigscience-workshop      |   | Base: BLOOMZ, mT0                                                                |            |               |             |                |         |               |              |          |       |            |                | https://github.com/bigscience-workshop/xmtf       |
| Open-Assistant           |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🟢            | 🟢           | 🔴       | 🔴    | 🔴         | 🟢             | 🟢                                                |
| LAION-AI                 |   | Base: oasst1 (own)                                                               |            |               |             |                |         |               |              |          |       |            |                | https://github.com/LAION-AI/Open-Assistant        |
| BELLE                    |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🟢            | 🟢           | 🟢       | 🔴    | 🔴         | 🔴             | 🔴                                                |
| LianjiaTech              |   | Base:  LLaMA, BLOOMZ                                                             |            |               |             |                |         |               |              |          |       |            |                | https://github.com/LianjiaTech/BELLE              |
| CharRWKV                 |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🟢            | 🟢           | 🔴       | 🔴    | 🔴         | 🟢             | 🟢                                                |
| BlinkDL                  |   | Base: RWKV-LM (own)                                                              |            |               |             |                |         |               |              |          |       |            |                | https://github.com/BlinkDL/ChatRWKV               |
| dolly                    |   | 🟢                                                                               | 🟢         | 🟢            | 🟡          | 🔴             | 🟢      | 🟢            | 🟢           | 🟡       | 🔴    | 🔴         | 🟢             | 🔴                                                |
| databrickslabs           |   | Base: EleutherAI pythia                                                          |            |               |             |                |         |               |              |          |       |            |                | https://github.com/databrickslabs/dolly           |
| OpenChatKit              |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🟢            | 🔴           | 🟡       | 🔴    | 🔴         | 🟢             | 🔴                                                |
| togethercomputer         |   | Base: EleutherAI pythia                                                          |            |               |             |                |         |               |              |          |       |            |                | https://github.com/togethercomputer/OpenChatKit   |
| Cerebras-GPT             |   | 🟢                                                                               | 🟢         | 🟢            | 🔴          | 🔴             | 🟢      | 🟢            | 🟢           | 🟢       | 🔴    | 🔴         | 🔴             | 🔴                                                |
| Cerebras                 |   | Base: not open                                                                   |            |               |             |                |         |               |              |          |       |            |                | https://huggingface.co/cerebras/Cerebras-GPT-6.7B |
| stanford_alpaca          |   | 🟢                                                                               | 🟢         | 🟢            | 🟡          | 🔴             | 🟡      | 🟢            | 🟢           | 🔴       | 🔴    | 🔴         | 🔴             | 🔴                                                |
| Tatsu labs               |   | Base: LLaMA                                                                      |            |               |             |                |         |               |              |          |       |            |                | https://github.com/tatsu-lab/stanford_alpaca      |
| trlx                     |   | 🟢                                                                               | 🟢         | 🟢            | 🟡          | 🔴             | 🟢      | 🟢            | 🟡           | 🔴       | 🔴    | 🔴         | 🟡             | 🟢                                                |
| carperai                 |   | Base: various models including EleutherAI pythia, Google flan and Facebook OPT   |            |               |             |                |         |               |              |          |       |            |                | https://github.com/carperai/trlx                  |
| minChatGPT               |   | 🟢                                                                               | 🟢         | 🟢            | 🟡          | 🔴             | 🟢      | 🟢            | 🟡           | 🔴       | 🔴    | 🔴         | 🔴             | 🟢                                                |
| ethanyanjiali            |   | Base:  GPT2                                                                      |            |               |             |                |         |               |              |          |       |            |                | https://github.com/ethanyanjiali/minChatGPT       |
| Vicuna                   |   | 🟢                                                                               | 🟢         | 🟢            | 🟢          | 🟢             | 🟢      | 🔴            | 🔴           | 🔴       | 🔴    | 🔴         | 🔴             | 🔴                                                |
| Facico                   |   | Base:  LLaMA                                                                     |            |               |             |                |         |               |              |          |       |            |                | https://github.com/Facico/Chinese-Vicuna          |
| text-generation-webu     |   | 🟢                                                                               | 🟢         | 🟢            | 🔴          | 🔴             | 🟢      | 🟢            | 🔴           | 🔴       | 🔴    | 🔴         | 🔴             | 🔴                                                |
| oobabooga                |   | Base: EleutherAI pythia                                                          |            |               |             |                |         |               |              |          |       |            |                | https://github.com/Akegarasu/ChatGLM-webui        |
| PaLM-rlhf-pytorch        |   | 🟢                                                                               | 🔴         | 🔴            | 🔴          | 🔴             | 🟢      | 🟢            | 🔴           | 🔴       | 🔴    | 🔴         | 🟢             | 🔴                                                |
| lucidrains               |   | Base:  no model                                                                  |            |               |             |                |         |               |              |          |       |            |                | https://github.com/lucidrains/PaLM-rlhf-pytorch   |
| chatGPT                  |   | 🔴                                                                               | 🔴         | 🔴            | 🔴          | 🔴             | 🔴      | 🔴            | 🔴           | 🔴       | 🔴    | 🔴         | 🔴             | 🟡                                                |
| OpenAI                   |   | Base: GPT3.5, GPT4                                                               |            |               |             |                |         |               |              |          |       |            |                | https://chat.openai.com                           |



## Survey Criteria

### Availabity

#### Open code
Is the code of the project openly available for inspection? (green)

#### LLM training data:
 Is the training data of the base large language model (LLM) fully open for inspection (green)? We find that text generators often build on existing base LLMs and often inherit access and documentations restrictions from these models (yellow). % but actually there are no yellow cells in Fig 1 in this column

#### LLM model weights:
 Is the fully trained base model made openly available including model weights (green)?

#### RLHF training data:
 Is the dataset for the reinforcement-learning from human feedback (RLHF) component fully available for inspection? (green)

#### RLHF model weights:
 Is the model including RLHF component fully available for inspection (green)?

#### License:
 Is the software fully covered by any Open Source Initiatve (OSI)-approved license (green)? Does the license only cover part of the software or model or are additional usage restrictions in place (yellow)?

### Documentation

#### Code:
 Does the software come with professional and comprehensive documentation (green)? Are only parts of the software documented, e.g. API access or higher-order functions (yellow)?

#### Architecture:
 Is the neural network architecture (base model and fine-tuning steps) fully documented (green)? Are only parts of the process documented? (yellow)?

#### Preprint:
 Are archived preprint(s) available that cover all parts of the software including base models, fine-tuning, and RLHF components?

#### Paper:
 Is a peer-reviewed paper available that covers all parts of the software?

#### Datasheets:
 Are datasheets available for all training data used in all models and fine-tuning steps  (green), only for some data (yellow), or not at all (red)?

### Access methods

#### Package:
 A software package has been publically indexed (e.g. Python Package Index, Homebrew) (green)? Is the package shared via a hosting service (e.g. Github) (yellow)?


#### API:
 Is an open API available that provides unrestricted access to the text generator (other than security and CDN restrictions) (green)? Is API access limited or monetized in any way (yellow)?

## List of Projects

- [bigscience-workshop xmtf](https://github.com/bigscience-workshop/xmtf)

- [LAION-AI Open-Assistant](https://github.com/LAION-AI/Open-Assistant)

- [BELLE LianjiaTech](https://github.com/LianjiaTech/BELLE)		

- [BlinkDL CharRWKV](https://github.com/BlinkDL/ChatRWKV)

- [databrickslabs dolly](https://github.com/databrickslabs/dolly)

- [togethercomputer OpenChatKit](https://github.com/togethercomputer/OpenChatKit)

- [Cerebras Cerebras-GPT](https://github.com/bigscience-workshop/xmtf)

- [Tatsu labs stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)

- [carperai trlx](https://github.com/carperai/trlx)

- [ethanyanjiali minChatGPT](https://github.com/ethanyanjiali/minChatGPT)

- [Facico Vicuna](https://github.com/Facico/Chinese-Vicuna)

- [oobabooga text-generation-webu](https://github.com/Akegarasu/ChatGLM-webui)

- [lucidrainsPaLM-rlhf-pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch)		

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
