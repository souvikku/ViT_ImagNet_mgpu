# ViT_ImageNet_multi-gpu training
1. change your image and runAsUser number in the .yaml file to create a pod.

2. Use the interactive_vit_mgpu.yaml to create the pod.
Once the pod is created go to: /store/.local/lib/python3.8/site-packages/timm/models/layers/helpers.py and replace the 
second line with: ## import collections.abc as container_abcs to avoid contain related error

3. run command: python run_clean.py
