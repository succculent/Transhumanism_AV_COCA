# Transhumanism_AV_COCA

F22 Transhumanism Coca Project - Name TBD


## Setup


Git is a great tool for collaboration and version control. Here are some resources to learn how to use git -

&ensp;&ensp;&ensp;&ensp;- https://git-scm.com/video/get-going
    
&ensp;&ensp;&ensp;&ensp;- _if you know any good resources please add them here_
    
&ensp;&ensp;&ensp;&ensp;- always remember ... commit, pull, push 

Copy this repository into the current directory of your terminal
```console
git clone https://github.com/succculent/Transhumanism_AV_COCA.git
```

This project uses _Conda_ for package management. This - 

&ensp;&ensp;&ensp;&ensp;(1) helps ensure that everyone is using the same versions for all packages
    
&ensp;&ensp;&ensp;&ensp;(2) doesn't mess up your other projects if you already have python installed
    
&ensp;&ensp;&ensp;&ensp;(3) makes it easy to get started


[Here](https://docs.conda.io/en/latest/miniconda.html) is a bare-bones version of conda called _miniconda_

### Mac


To create the environment -
```console
conda env create -f env.yml
```


To enter the environment - 
```console
conda activate t-av-env
```


To exit the environment - 
```console
conda deactivate
```


### Windows


...todo

...probably the same command set, but I have no way to test this


### Linux


To create the environment -
```console
conda env create -f env.yml
```


To enter the environment - 
```console
conda activate t-av-env
```


To exit the environment - 
```console
conda deactivate
```


## Run

To run the code once the environment has been set up and is _currently_ active  - 
```console
python main.py
```