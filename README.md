![thumbnail](./thumbnail.png)

🔥 [![PyTorch Workflow](https://img.shields.io/badge/PyTorch-Workflow-FF69B4)](https://github.com/mehrshud/pytorch-workflow)
[![Banner](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDI0IiBoZWlnaHQ9IjU3NiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJnIiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIxMDAlIj48c3RvcCBvZmZzZXQ9IjAlIiBzdHlsZT0ic3RvcC1jb2xvcjojMGQxMTE3Ii8+PHN0b3Agb2Zmc2V0PSIxMDAlIiBzdHlsZT0ic3RvcC1jb2xvcjojMTYxYjIyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMjQiIGhlaWdodD0iNTc2IiBmaWxsPSJ1cmwoI2cpIi8+PHRleHQgeD0iNTEyIiB5PSIyODgiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iNDgiIGZpbGw9IiM1OGE2ZmYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiPnB5dG9yY2gtd29ya2Zsb3c8L3RleHQ+PC9zdmc+)](https://github.com/mehrshud/pytorch-workflow)
Streamline Your PyTorch Workflows



## Demo

<!-- Demo GIF placeholder —
     Record with: asciinema rec demo.cast && agg demo.cast demo.gif
     Or: npx terminalizer record demo -d 'npm start'
     Upload to imgbb.com and replace this comment with: ![Demo](<url>)
-->

![pytorch-workflow demo](https://placehold.co/800x400/0d1117/58a6ff?text=Demo+Recording+Coming+Soon)

## Why I Built This
I started `pytorch-workflow` as a weekend project to solve my own problems with managing PyTorch workflows. I was working on a deep learning project and found myself spending more time managing my workflows than actually training models. I tried using existing tools, but they were either too complex or didn't integrate well with my existing workflow. I decided to build my own tool, and `pytorch-workflow` was born. I've been using it for my own projects for months now, and I'm excited to share it with the community. I hope it can help you as much as it's helped me.

**My Workflow Problems**
Before `pytorch-workflow`, my workflows were a mess. I had multiple scripts for training, testing, and hyperparameter tuning, and it was hard to keep track of which version of the model was which. I spent hours debugging issues that could have been avoided if I had a more streamlined workflow. I knew I needed a better way to manage my workflows, and that's why I built `pytorch-workflow`.

### Features
* 🚀 Workflow automation
* 📊 Hyperparameter tuning
* 📈 Model versioning
* 🔄 Integration with popular PyTorch libraries
* 🌐 Web-based interface

## Real-World Usage Examples
Here are a few examples of how you can use `pytorch-workflow`:
```python
# Train a model
from pytorch_workflow import Trainer
trainer = Trainer(model='resnet50', dataset='cifar10')
trainer.train()


```python
# Tune hyperparameters
from pytorch_workflow import Tuner
tuner = Tuner(model='resnet50', dataset='cifar10')
tuner.tune()


```python
# Deploy a model
from pytorch_workflow import Deployer
deployer = Deployer(model='resnet50', dataset='cifar10')
deployer.deploy()


```python
# Use the web interface
from pytorch_workflow import WebInterface
web_interface = WebInterface()
web_interface.start()


```python
# Use the API
from pytorch_workflow import API
api = API()
api.train(model='resnet50', dataset='cifar10')


## Comparison Table
| Tool | Workflow Automation | Hyperparameter Tuning | Model Versioning | Web Interface |
| --- | --- | --- | --- | --- |
| `pytorch-workflow` | 🚀 | 📊 | 📈 | 🌐 |
| `pytorch-ignite` | ❌ | 📊 | ❌ | ❌ |
| `torchvision` | ❌ | ❌ | ❌ | ❌ |

## Architecture
### Component Diagram
```mermaid
graph TD
  A[Client] --> B[API]
  B --> C[DB]
  B --> D[Services]
  D --> C


### Sequence Diagram
```mermaid
sequenceDiagram
  Client->>API: request
  API-->>Client: response
  API->>Services: request
  Services-->>API: response


### Deployment Diagram
```mermaid
graph LR
  Internet --> LoadBalancer
  LoadBalancer --> AppServer
  AppServer --> Database


### C4 Context Diagram
```mermaid
C4Context


## Getting Started
1. Install `pytorch-workflow` using `pip install pytorch-workflow`
2. Create a new project using `pytorch-workflow init`
3. Start the web interface using `pytorch-workflow start`

## Advanced Configuration
| Environment Variable | Description |
| --- | --- |
| `PYTORCH_WORKFLOW_DB` | Database URL |
| `PYTORCH_WORKFLOW_MODEL_DIR` | Model directory |
| `PYTORCH_WORKFLOW_LOG_LEVEL` | Log level |

## Troubleshooting
* **Issue 1:** `pytorch-workflow` is not installing correctly.
	+ **Solution:** Try reinstalling using `pip install --force-reinstall pytorch-workflow`
* **Issue 2:** The web interface is not starting.
	+ **Solution:** Try restarting the web interface using `pytorch-workflow restart`
* **Issue 3:** Models are not training correctly.
	+ **Solution:** Try checking the model configuration and dataset using `pytorch-workflow train --verbose`

## Roadmap
- [ ] Add support for more PyTorch libraries
- [ ] Improve the web interface
- [ ] Add more hyperparameter tuning algorithms

## Contributing
Contributions are welcome! Please submit a pull request with your changes.

## Buy Me Coffee
If you like `pytorch-workflow`, consider buying me a coffee: https://buymeacoffee.com/omnilertlab
You can also visit my website at https://omnilertlab.com for more information about my projects.
Check out my blog at https://mehrshud.github.io for more articles on deep learning and PyTorch.