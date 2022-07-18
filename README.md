
# Runway-Detector-Satellite-Imagery

Hi y'all. You can detect/segment runways with this repo.

![App Screenshot](https://github.com/mahmutgemici0/Runway-Detector-Satellite-Imagery/blob/main/airport_dataset/runway/raw_data/2.png?raw=true)




## Demo

![App Screenshot](https://github.com/mahmutgemici0/Runway-Detector-Satellite-Imagery/blob/main/assets/results.gif?raw=true)

## Usage/Examples

```bash
path/to/repo/ $ streamlit run main.py
```


## Install & Run Locally
<!-- Install Git-lfs https://git-lfs.github.com/ -->

<!-- - Linux
```
  sudo apt-get install git-lfs
```
- Windows 
```
    pip install git-lfs
```
Initialize Git-LFS
```
  git install git-lfs
```
Clone the project -->

```bash
  git clone https://github.com/mahmutgemici0/Runway-Detector-Satellite-Imagery.git
```
Create a virtual environment.
```bash
  conda create -n torch python=3.8
```
Activate the virtual environment.
```bash
  conda activate torch
```
Install PyTorch
```bash
  pip install torch
```
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools":
```
https://visualstudio.microsoft.com/visual-cpp-build-tools/
```
Install GCC
```
sudo apt-get install gcc
```
Install G++
```
$ sudo apt install g++
```
Install build essentials
```
$ sudo apt install build-essential
```
Download Detectron2 Repository
```
  git clone https://github.com/facebookresearch/detectron2.git
```
Install Detectron2
```
  python -m pip install -e detectron2
```
Go to the project directory
```bash
  cd Runway-Detector-Satellite-Imagery
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Download pre-trained model and put it in outputs/ folder
```
https://drive.google.com/file/d/1c4CIq43EswXXpwJjV_peZw1XirwoWuR0/view?usp=sharing
```
Run
```
  streamlit run main.py 
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@mahmutgemici0](https://www.github.com/mahmutgemici0)

