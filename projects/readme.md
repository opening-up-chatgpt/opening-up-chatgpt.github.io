# How to contribute 

Every project is a separate file. The file some fields with contains basic metadata and then a set of triples of `_class`, `_link` and `_notes`. Class can be one of three values: 🟩 open, 🟧 partial or 🟥 closed (leave empty to signify NA). Link is a URL providing evidence for the openness classification. Notes provide context and reasoning for the classification.

# Criteria
The below list spells out for the openness criteria for features in the areas of Availability, Documentation and Access. Use these guidelines to reason about determinations of openness levels.

## **Availability**

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
       
## **Documentation**

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

**Model card**

    🟥 Model card(s) not available.
    
    🟧 Model card(s) that provide partial insight on model architecture, training, fine-tuning, and evaluation are available.
    
    🟩 Model card(s) are available that provide comprehensive insight on model architecture, training, fine-tuning, and evaluation are available.

**Datasheet**

    🟥 Datasheet(s) are not available.
    
    🟧 Datasheet(s) that provide partial insight on data collection and curation are available.
    
    🟩 Datasheet(s) are available that provide comprehensive insight on data collection and curation are available.


## **Access methods**

**Package**

    🟥 No index software package is available.
    
    🟧 User-oriented code or web-interface is available but not as a versioned package.
    
    🟩 A packaged release of fully open-source software (e.g. a Python Package Index, Homebrew) is available.


**API**

    🟥 No API access.
    
    🟧 Commerial or restircted-access user API is available.
    
    🟩 An open API available that provides unrestricted access to the text generator (other than security and CDN restrictions).

