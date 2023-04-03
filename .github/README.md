<div align="center">

# Unreal Diffusion : A Stable Diffusion Unreal Engine Implementation
![unreal-diffusion](/Unreal/docs/unreal_v0.8.png)

[![discord badge]][discord link]

[discord badge]: https://flat.badgen.net/discord/members/wg67wbA3aA?icon=discord
[discord link]: https://discord.gg/wg67wbA3aA
</div>

This is a Unreal Engine 5 implementation of Stable Diffusion. It provides a streamlined
GUI inside Unreal Engine to easily generate game-ready textures among other features. You can run Automatic1111 or InvokeAI as the backend server.

**Quick links**: [<a href="https://discord.gg/wg67wbA3aA">Discord Server</a>]


## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
3. [Latest Changes](#latest-changes)
4. [Troubleshooting](#troubleshooting)
5. [Support](#support)


### Installation

This plugin supports several SD backends. You can find individual installation instructions
below. Install Automatic1111 Stable Diffusion and/or InvokeAI

- #### [1a] Follow the install instructions at [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and get that running normally
- #### [1b] Follow the install instructions at [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) and get that running normally (WIP, use the legacy_InvokeAI in the meantime before I add support for their new API)
- #### [2] Copy the Unreal/Unreal_Diffusion folder into your Unreal plugin folder either for the project or the engine install location
- #### [3] Go to Plugins in unreal and then enable the "Unreal Diffusion" plugin and restart the engine
![plugin](/Unreal/docs/unreal_plugin.png)
- #### [4] Navigate to project settings then add the install location of Automatic1111 and/or InvokeAI in the settings
![editor settings](/Unreal/docs/unreal_plugin_settings.png)
- #### [4.1] Also add /Lib/site-packages from your python 3 install location on your computer like in the image below
![project logo](/Unreal/docs/python_paths.png)
- #### [5] (Optional) Go to Editor Preferences in Unreal and then "Loading & Saving" 
- #### [5.1] Add the "/outputs/img-samples/unreal-diffusion" to the Directories to monitor list to automatically import the generated images to unreal. You can map these to /Game/Unreal_Diffusion/Output as in the image below
![project logo](/Unreal/docs/loading_saving.png) 

### Running the plugin
Launch the main UI from the playbar here:
![unreal start ui](/Unreal/docs/unreal_button.png)
Main ui:
![unreal main ui](/Unreal/docs/unreal_main_ui.png)

Choose backend server and automatically launch it from the "Start Server" button. Make sure the plugin settings have the correct path
![unreal settings ui](/Unreal/docs/unreal_settings.png)


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
- v0.8.0 (03 April 2023)
  - Major rework
  - Added support for Automatic1111 backend server
  - Converted  from content to C++ plugin
  - Moved config settings to plugin settings
  - Adding WIP ChatGPT prompting support
- v0.6.0 (30 October 2022)
  - Added Img2Img support
  - Cleaned up UI.
  - Fixed reset button bugs.
  - Added export of texture if source file not found.
  - Added more sliders to UI
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

Original portions of the software are Copyright (c) 2023
[Emil Eldstål](https://github.com/emomilol1213)
