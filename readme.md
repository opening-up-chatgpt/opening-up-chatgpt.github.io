# ![Awesome](docs/logos/openchatgpt-logo-favicon-green-on-transparent.png)](https://liesenf.github.io/opening-up-chatgpt/)Opening up ChatGPT: a curated list to track openness, transparency, and accountability in instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

# [view live table](https://liesenf.github.io/opening-up-chatgpt/) 

Large language models that exhibit instruction-following behaviour represent one of the biggest recent upheavals in conversational interfaces, a trend in large part fuelled by the release of OpenAI's ChatGPT, a proprietary large language model for text generation fine-tuned through reinforcement learning from human feedback (LLM+RLHF). We review the risks of relying on proprietary software and survey the first crop of open-source projects of comparable architecture and functionality. The main contribution of this paper is to show that openness is differentiated, and to offer scientific documentation of degrees of openness in this fast-moving field. We evaluate projects in terms of openness of code, training data, model weights, reinforcement learning data, licensing, scientific documentation, and access methods. We find that while there is a fast-growing list of projects billing themselves as 'open source', many inherit undocumented data of dubious legality, few share the all-important RLHF components (a key site where human annotation labour is involved), and careful scientific documentation is exceedingly rare. Degrees of openness are relevant to fairness and accountability at all points, from data collection and curation to model architecture, and from training and fine-tuning to release and deployment. 

## Contents

- [Overview](#overview)
- [Criteria](#survey-criteria)
- [List of Projects](#list-of-projects)

## How to edit the awesome list and live table

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


## Criteria

- Availability

    -  **Open code**
Is the code of the project openly available for inspection? (green)

    - **LLM training data**:
 Is the training data of the base large language model (LLM) fully open for inspection (green)? We find that text generators often build on existing base LLMs and often inherit access and documentations restrictions from these models (orange).

    - **LLM model weights**:
 Is the fully trained base model made openly available including model weights (green)?

    - **RLHF training data**:
 Is the dataset for the reinforcement-learning from human feedback (RLHF) component fully available for inspection? (green)

    - **RLHF model weights**:
 Is the model including RLHF component fully available for inspection (green)?

    -  **License**:
 Is the project fully covered by any Open Source Initiative (OSI)-approved license (green)? Does the license only cover part of the project or are additional usage restrictions in place (orange)?

- Documentation

   - **Code**:
 Does the project come with professional and comprehensive documentation (green)? Are only parts of the software documented, e.g. API access or higher-order functions (orange)?

    - **Architecture**:
 Is the neural network architecture (base model and fine-tuning steps) fully documented (green)? Are only parts of the process documented? (orange)?

    - **Preprint**:
 Are archived preprint(s) available that cover all parts of the software including base models, fine-tuning, and RLHF components?

    - **Paper**:
 Is a peer-reviewed paper available that covers the model and all its relevant parts, including a discussion of model architecture, design, and limitations?

    - **Datasheets**:
 Are datasheets and model cards available that provide documentation on data collection and curation and on model architecture, training, fine-tuning, and evaluation? Do these cover all or most aspects (green), only some (orange), or are they not available at all (red)?

- Access methods

    - **Package**:
Is there a packaged release of the software/code (e.g. Python Package Index, Homebrew) (green)? Is the code shared but not as a versioned package (orange)?

    - **API**:
 Is an open API available that provides unrestricted access to the text generator (other than security and CDN restrictions) (green)? Is API access limited or monetized in any way (orange)?

## List of Projects

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
