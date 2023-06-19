# Opening up ChatGPT: a curated list to track openness, transparency, and accountability in instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

# 🔥🔥🔥 [view live table](https://liesenf.github.io/awesome-open-chatgpt/) 🔥🔥🔥 

Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human annotation labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 


![Open source software survey](./osi-logo.png)

## Contents

- [Overview](#overview)
- [Criteria](#survey-criteria)
- [List of Projects](#list-of-projects)

## The template

Append the new project at the end of file

```markdown

1. Add entry to list of projects: 

## [{owner}/{project-name}]{https://github.com/link/to/project}

2. edit projects/newproject.md template
```

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

## Criteria

- Availability

    -  Open code
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


## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

List of contributors:

<a href="https://github.com/liesenf/awesome-open-chatgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liesenf/awesome-open-chatgpt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
