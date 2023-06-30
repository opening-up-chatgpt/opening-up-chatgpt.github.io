# Opening up ChatGPT: a curated list to track openness, transparency, and accountability in instruction-following text generators [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

# [![Awesome](docs/logos/openchatgpt-logo-favicon-green-on-transparent.png)](https:///liesenf.github.io/opening-up-chatgpt/) [view live table](https://liesenf.github.io/opening-up-chatgpt/) 

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

**Availability**

 **Source code**

    🟥 Project is closed source code.
    
    🟧 Some source code is open.
    
    🟩 Project source code openly available and fully open available for inspection.

**LLM training data**
  
    🟥 Training data of base large language models (LLM) is not open for inspectionn.
    
    🟧 Some of the training data of the large language models (LLM) is open for inspection.
    
    🟩 The training data of all large language models (LLM) is fully open for inspection.

**LLM model weights**

    🟥 LLM weights are not shared and model training procedure is not open for inspection.
    
    🟧 LLM weights are not fully shared or model training procedure is not fully open for inspection.
    
    🟩 LLM weights are shared and model training procedure is fully open for inspection.

**RLHF training data**:

    🟥 Training data of the reinforcement-learning from human feedback (RLHF) component is not open for inspectionn.
    
    🟧 Some of the training data of the reinforcement-learning from human feedback (RLHF) component is open for inspection.
    
    🟩 The training data of for the reinforcement-learning from human feedback (RLHF) component is fully open for inspection.

**RLHF model weights**:

    🟥 RLHF component weights are not shared and model training procedure is not open for inspection.
    
    🟧 RLHF component weights are not fully shared or model training procedure is not fully open for inspection.
    
    🟩 RLHF component weights are shared and model training procedure is fully open for inspection.

**License**:

    🟥 The project is not licensed clearly or does not use a true Open Source Initiative (OSI)-approved license.
    
    🟧 Only parts of the project or components are fully covered by a true Open Source Initiative (OSI)-approved license.
    
    🟩 The project is fully covered by a true Open Source Initiative (OSI)-approved license.
       
**Documentation**

**Code**
 
    🟥 Code documentation not available.
    
    🟧 Some components of the project features code documentation.
    
    🟩 All components of the project features a comprehensive code documentation.

**Architecture**

    🟥 System architecture and model training setup are not documented.
    
    🟧 System architecture and model training setup is partially documented.
    
    🟩 System architecture and model training setup is fully documented.

**Preprint**

    🟥 No archived preprint(s) available.
    
    🟧 Archived preprint(s) that detail parts of the software including base models, fine-tuning, or RLHF components are available.
    
    🟩 Archived preprint(s) are available that cover all parts of the software including base models, fine-tuning, and RLHF components.

**Paper**

    🟥 No peer-reviewed paper(s) available.
    
    🟧 Peer-reviewed paper(s) detail parts of the software including base models, fine-tuning, or RLHF components.
    
    🟩 Peer-reviewed paper(s) are available that cover all parts of the software including base models, fine-tuning, and RLHF components.

**Datasheets**

    🟥 Datasheet(s) are not available.
    
    🟧 Datasheet(s) that provide partial insight on data collection and curation and on model architecture, training, fine-tuning, and evaluation are available.
    
    🟩 Datasheet(s) are available that provide comprehensive insight on data collection and curation and on model architecture, training, fine-tuning, and evaluation are available.


**Access methods**

**Package**

    🟥 No index software package is available.
    
    🟧 User-oriented code or web-interface is available but not as a versioned package.
    
    🟩 A packaged release of fully open-source software (e.g. a Python Package Index, Homebrew) is available.


**API**

    🟥 No API access.
    
    🟧 Commerial or restircted-access user API is available.
    
    🟩 An open API available that provides unrestricted access to the text generator (other than security and CDN restrictions).


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
