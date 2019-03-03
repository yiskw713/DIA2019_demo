# Demonstration of task-oriented function detection

This reposiory is for demonstration of poster presentation in DIA2019, whose content is about "task-oriented function detection".
In our proposed method, the network takes as input RGB images and task vectors which are one-hot encoded, 
and outputs "task-oriented function" as below.
Thanks to task vectors, the network can infer different ways to use for the same object.
though networks in most existing works on affordance detection cannot.

![demo](demo.gif)

# Requirements

If you want to try my demo, you need the below packages:
* dash
* dash_core_components
* dash_html_components

After installing, please run ` python app.py`.

# References
I referred to [this repository](https://github.com/dychi/dash-action-segmentation-demo)
If you get interested in making a demo, I strongly recommend that you visit it. 

# Paper
石川裕地, 石川晴也, 秋月秀一, 青木義満. 操作タスク入力に基づく物体の機能部推定. In DIA, 2019. 