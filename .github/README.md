<div align="center">

# Unreal Diffusion : A Stable Diffusion Unreal Engine Implementation
![unreal-diffusion](/Unreal/docs/Unreal_DiffusionV0_5.png)

[![discord badge]][discord link]

[discord badge]: https://flat.badgen.net/discord/members/wg67wbA3aA?icon=discord
[discord link]: https://discord.gg/wg67wbA3aA
</div>

This is a fork of
[invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI),
a popular SD implementation with great features and GUI. It provides a streamlined
GUI inside Unreal Engine to easily generate game-ready textures. 

**Quick links**: [<a href="https://discord.gg/wg67wbA3aA">Discord Server</a>]


## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
3. [Latest Changes](#latest-changes)
4. [Troubleshooting](#troubleshooting)
5. [Support](#support)


### Installation

This fork is supported across multiple platforms. You can find individual installation instructions
below.

- #### [1] Follow the install instructions at [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) and get that running normally
- #### [2] Copy the Unreal_Diffusion/Unreal_Diffusion folder into your unreal project's content folder
- #### [3] Go to Project Settings in unreal and then plugin/Python
- #### [4] Navigate and add your content/Unreal_Diffusion/Python folder to the "Additional Paths" list
- #### [4.1] Also add /Lib/site-packages from your python 3 install location on your computer like in the image below
![project logo](/Unreal/docs/python_paths.png)
- #### [5] (Optional) Go to Editor Preferences in Unreal and then "Loading & Saving" 
- #### [5.1] Add the "/outputs/img-samples/unreal-diffusion" to the Directories to monitor list to automatically import the generated images to unreal. You can map these to /Game/Unreal_Diffusion/Output as in the image below
![project logo](/Unreal/docs/loading_saving.png) 

### Running the plugin

First switch to the correct folder and conda environment and then start the server. It should say "Point your browser at xxxxxxx" if launched succesfully
 ```bash
(base) conda activate invokeai
```
 ```bash
(invokeai) cd C:\AI\Unreal-Diffusion (example, depending on where you cloned the repo)
```
 ```bash
(invokeai) python scripts/legacy_api.py --web --port 3333 -o outputs/img-samples/unreal-diffusion
```

Back in unreal, go to the Unreal Diffusion folder and find the "Unreal_Diffusion" Editor Utility Widget, right-click that and press "Run Editor Utility Widget as in the image below.
![unreal start ui](/Unreal/docs/unreal_start_ui.png) 
This should start the UI which looks like this and you are ready to start generating images/textures
![unreal ui](/Unreal/docs/unreal_ui.png) 

### Features

#### Major Features

### Unreal UI
- Realtime - toggle that will generate the images without freezing unreal, but may generate slower. Off by default
- Seamless - Forces SD to generate seamless images. Sometimes you could try to have this off and instead type seamless in the prompt



Most docs here link to InvokeAI's as they are very detailed and show usecases and syntax

- [Prompts and Prompt Blending](https://invoke-ai.github.io/InvokeAI/features/PROMPTS/#prompt-blending)
- [Negative Prompts](https://invoke-ai.github.io/InvokeAI/features/PROMPTS/#negative-and-unconditioned-prompts)

- [Image To Image(WIP)](https://invoke-ai.github.io/InvokeAI/features/IMG2IMG/) 
- [Upscaling(WIP)](https://invoke-ai.github.io/InvokeAI/features/POSTPROCESS/)
- [Variations(WIP)](https://invoke-ai.github.io/InvokeAI/features/VARIATIONS/)

### Latest Changes

- v0.5.0 (23 October 2022)
  - initial version with prompt/negative prompts, cfg, steps features


### Troubleshooting

If the images won't generate due to VRAM, try lowering the resolution or temporarily load an empty level in unreal to generate images.

# Contributing

Anyone who wishes to contribute to this project, whether documentation, features, bug fixes, code
cleanup, testing, or code reviews, is very much encouraged to do so. If you are unfamiliar with how
to contribute to GitHub projects, here is a
[Getting Started Guide](https://opensource.com/article/19/7/create-pull-request-github).

A full set of contribution guidelines, along with templates, are in progress, but for now the most
important thing is to **make your pull request against the "development" branch**, and not against
"main". This will help keep public breakage to a minimum and will allow you to propose more radical
changes.

### Contributors

This fork is at the moment handled by me, with the main features/backend API coming from InvokeAI.

### Support

For support, please use this repository's GitHub Issues tracking service. Feel free to send me an
email if you use and like the plugin.

Original portions of the software are Copyright (c) 2022
[Emil Eldstål](https://github.com/emomilol1213)
