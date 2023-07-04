# [![logo](docs/logos/openchatgpt-logo-favicon-red-on-transparent.png)](https:///opening-up-chatgpt.github.io/) Opening up ChatGPT — [view live table](https://opening-up-chatgpt.github.io/) 

Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. “Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.” In Proceedings of CUI’23. Eindhoven. doi:10.1145/3571884.3604316.

> Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human annotation labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 

## Contents

- [Overview](#overview)
- [How to contribute](#how-to-contribute)
- [List of Projects](#list-of-projects)

## Overview
We classify projects for their degrees of openness across **a predefined set of criteria** in the areas of Availability, Documentation and Access. See the criteria [here](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/tree/main/projects#criteria).

| Availability                                                          | Documentation                                                      | Access          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|-----------------|
| <ul><li>Open code</li><li>LLM data</li><li>LLM weights</li><li>RL data</li><li>RL weights</li><li>License</li></ul> | <ul><li>Code</li><li>Architecture</li><li>Preprint</li><li>Paper</li><li>Model card</li><li>Data sheet</li></ul> | <ul><li>Package</li><li>API</li></ul> |


## How to contribute
You can contribute in (at least) two ways: either by editing specific data points for particular projects; or by updating the awesomelist below. Our goal is to have the awesomelist and the more detailed database of openness features by project roughly in sync, but awesomelists are by nature more free-form and text-driven
Template to add a project to the [List of Projects](#list-of-projects) section:

```markdown

1. Add entry to list of projects: 

## [{owner}/{project-name}]{https://github.com/link/to/project}

2. edit projects/newproject.md template
```

How to add a project to the live table:

```markdown

1. Copy and edit the /project/newproject.csv file in a pull request. 

## [{owner}/{project-name}]{https://github.com/link/to/project}

```

## Opening up ChatGPT: a curated list to track openness, transparency, and accountability in instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Overview of available open text generators with links to evidence of all above evaluation criteria.

https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/blob/4c6730ddef6a5501d64380227f3beba6afa0391a/projects/alpaca.yaml#L2-L70

**[bigscience-workshop xmtf](https://github.com/bigscience-workshop/xmtf)**

     - Availability
    
        -  Open code: https://github.com/bigscience-workshop/xmtf
    
        - LLM training data: https://github.com/bigscience-workshop/xmtf
    
        - LLM model weights: https://github.com/bigscience-workshop/xmtf
    
        - RLHF training data: https://github.com/bigscience-workshop/xmtf
    
        - RLHF model weights: https://github.com/bigscience-workshop/xmtf
    
        - License: https://github.com/bigscience-workshop/xmtf
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[LAION-AI Open-Assistant](https://github.com/LAION-AI/Open-Assistant)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

    
**[BELLE LianjiaTech](https://github.com/LianjiaTech/BELLE)**	

    - Availability
    
        -  Open code: https://github.com/LianjiaTech/BELLE
    
        - LLM training data: https://github.com/LianjiaTech/BELLE
    
        - LLM model weights: https://github.com/LianjiaTech/BELLE
    
        - RLHF training data: https://github.com/LianjiaTech/BELLE
    
        - RLHF model weights: https://github.com/LianjiaTech/BELLE
    
        - License: https://github.com/LianjiaTech/BELLE
    
    - Documentation
    
       - Code: https://github.com/LianjiaTech/BELLE
    
        - Architecture: https://github.com/LianjiaTech/BELLE
    
        - Preprint: https://github.com/LianjiaTech/BELLE
    
        - Paper: https://github.com/LianjiaTech/BELLE
    
        - Datasheets: https://github.com/LianjiaTech/BELLE
    
    - Access methods
    
        - Package: https://github.com/LianjiaTech/BELLE
    
        - API: https://github.com/LianjiaTech/BELLE


**[BlinkDL CharRWKV](https://github.com/BlinkDL/ChatRWKV)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf
        
**[databrickslabs dolly](https://github.com/databrickslabs/dolly)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[togethercomputer OpenChatKit](https://github.com/togethercomputer/OpenChatKit)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf


**[Cerebras Cerebras-GPT](https://github.com/bigscience-workshop/xmtf)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf


**[Tatsu labs stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[carperai trlx](https://github.com/carperai/trlx)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[ethanyanjiali minChatGPT](https://github.com/ethanyanjiali/minChatGPT)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[Facico Vicuna](https://github.com/Facico/Chinese-Vicuna)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[oobabooga text-generation-webu](https://github.com/Akegarasu/ChatGLM-webui)**

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf

**[lucidrainsPaLM-rlhf-pytorch](https://github.com/lucidrains/PaLM-rlhf-pytorch)**		

    - Availability
    
        -  Open code: https://github.com/LAION-AI/Open-Assistant
    
        - LLM training data: https://github.com/LAION-AI/Open-Assistant
    
        - LLM model weights: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF training data: https://github.com/LAION-AI/Open-Assistant
    
        - RLHF model weights: https://github.com/LAION-AI/Open-Assistant
    
        - License: https://github.com/LAION-AI/Open-Assistant
    
    - Documentation
    
       - Code: https://github.com/bigscience-workshop/xmtf
    
        - Architecture: https://github.com/bigscience-workshop/xmtf
    
        - Preprint: https://github.com/bigscience-workshop/xmtf
    
        - Paper: https://github.com/bigscience-workshop/xmtf
    
        - Datasheets: https://github.com/bigscience-workshop/xmtf
    
    - Access methods
    
        - Package: https://github.com/bigscience-workshop/xmtf
    
        - API: https://github.com/bigscience-workshop/xmtf


## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

List of contributors:

<a href="https://github.com/liesenf/awesome-open-chatgpt/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liesenf/awesome-open-chatgpt" />
</a>

Made with [contrib.rocks](https://contrib.rocks).
