# Bletcher-mix(V1.0)

Bletcher Project's **python server repository** for running AI and communication.
<br/>
<br/>

## Technology

- django
- python3
- pytorch
- Heroku
<br/>
<br/>

## environment

- python                3.8.5
- torch(cpu-only)       1.5.0
- torchvision(cpu-only) 0.6.0
- django                3.1.4
<br/>
<br/>

## Run

Bletcher-mix uses **Heroku** which is "Cloud Service" and it is communicating with Bletcher-back

We release Ver.1.0 on Heroku.
```bash
https://bletcher-mix.herokuapp.com/
```
then, you can see our api server Index-Page
<br/>
<br/>

## Run Locally(Development Mode)

when you want to run AI python server locally, 

1. Clone [**bletcher-back**](https://github.com/Bletcher-Project/bletcher-back) repository
```bash
git clone [Bletcher-back repository address]
```
<br/>

2. Refer to bletcher-back's **README.md** and run the server.
<br/>

3. Clone [**bletcher-mix**](https://github.com/Bletcher-Project/bletcher_mix) repository 
```bash
git clone [Bletcher-mix repository address]
```
<br/>

4. Go to the repository
```bash
cd bletcher_mix
```
<br/>

5. Enter following line
```bash
python manage.py runserver
```
<br/>

6. Refer to bletcher-back [**WIKI**](https://github.com/Bletcher-Project/bletcher-back/wiki) and run it locally with [**POSTMAN**](https://www.postman.com/)
<br/>
<br/>

> The original model VGG19 was modified from VGG19 to resnet50 due to the capacity limitation caused by Heroku free use.
If you want a better completeness, please refer to the comments in **neural-style.py** and modify it
<br/>
<br/>

## Reference
1. neural-style.py
<br/>

Our AI code was referenced [**here**](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html) and modified to suit our needs.







