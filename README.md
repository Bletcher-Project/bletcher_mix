![GitHub release (latest by date)](https://img.shields.io/github/v/release/Bletcher-Project/bletcher_mix?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/Bletcher-Project/bletcher_mix?style=for-the-badge) [![GitHub issues](https://img.shields.io/github/issues/Bletcher-Project/bletcher_mix?style=for-the-badge)](https://github.com/Bletcher-Project/bletcher_mix/issues) [![GitHub license](https://img.shields.io/github/license/Bletcher-Project/bletcher_mix?style=for-the-badge)](https://github.com/Bletcher-Project/bletcher_mix/blob/main/LICENSE)

# Bletcher-Mix 👩🏻‍🎨

![image](./README_image/nst_example.jpeg)

인공지능 예술 웹 서비스 [Bletcher Project](https://github.com/Bletcher-Project/Bletcher)의 **AI Repository** 입니다. Django로 이미지 합성 서버를 구현하였으며 Oracle Cloud에 배포되어 있습니다.

_👏 우리는 [bletcher-ml](https://github.com/Bletcher-Project/bletcher-ml) 저장소를 지나와 100여개의 commit과 8개의 issue를 통한 많은 토의 끝에 배포되었습니다!!_

_🚀 Version 1.1.0 Released_

## Technology

- Pytorch
- Django
- Cloudinary
- Heroku
- Oracle Cloud

<img src="./README_image/logic.png" alt="Logic" width="700" height="500"/>

## 프로젝트 배포

- Cloudinary를 통한 Storage Upload
- Heroku를 통한 어플리케이션 배포
  - [▶︎ Pull Request](https://github.com/Bletcher-Project/bletcher_mix/pull/5)
- Oracle Cloud를 통한 어플리케이션 배포
  - [▶︎ Issue](https://github.com/Bletcher-Project/bletcher_mix/issues/7)
  - [▶︎ Issue](https://github.com/Bletcher-Project/bletcher_mix/issues/8)
  - [▶︎ Pull Request](https://github.com/Bletcher-Project/bletcher_mix/pull/10)

## 핵심기능

- 두 이미지 합성 구현
  - pytorch 기반 neural-style기술을 활용한 이미지 합성
- 웹서버 구현
  - django를 이용하여 `/synthesizing`라우터를 통해 이미지 합성 및 이미지 백 클라우디너리에 결과 반환
- 클라우드 배포
  - Heroku와 Oracle Cloud를 활용하여 항상 작동하는 서버 배포

## 트러블 슈팅

- Heroku timeout issue
  - [▶︎ Issue](https://github.com/Bletcher-Project/bletcher_mix/issues/6)

## Run (수정 필요)

Oracle Cloud 에 배포되어 있습니다. `http://193.123.235.185:8000`의 `/synthesizing`라우터로 요청합니다.---

## Getting Started

Bletcher-mix는 Oracle Cloud에 배포되어있어 따로 환경을 구축할 필요가 없지만, 개발자 환경에서 커스터마이징 하고싶은 분은 아래의 절차를 따라주세요.

### Prerequisites

실행 전 [requirements](./requirements.txt)를 참고하여 Python 개발 환경을 구축하십시오. 가상 환경을 만들어 구축할 것을 권장합니다.

### Installation

1. `git clone https://github.com/Bletcher-Project/bletcher_mix`
2. `./bletcher_mix/` 경로의 [.env.example](./bletcher_mix/.env.example)를 참고하여 `.env` 파일을 생성합니다.

### Run Locally

이는 [bletcher-back](https://github.com/Bletcher-Project/bletcher-back), Heroku, Cloudinary 등의 서비스와 연결이 필수적이고 해당 서비스들에게 최적화되어 있습니다. 실행하려면 최소한 bletcher-back server의 실행과 Cloudinary 연동이 필요합니다.

1. 터미널에서 `python manage.py runserver`를 실행합니다.
2. [**bletcher-back**](https://github.com/Bletcher-Project/bletcher-back) repository를 clone하고 해당 python 서버에 `/synthesizing` 라우터로 요청합니다.

### 모델별 실행 결과 확인

> ❗️ neural style은 pytorch기반 CNN 모델로 **VGG19** 모델을 사용했을 때 최적의 성능을 볼 수 있습니다.

VGG19 모델을 통해 실행 결과를 보고 싶다면 [neural_style.py](./api/neural_style.py) 파일을 열어 layer와 model을 다음과 같이 수정해야 합니다.

```python
# VGG19 ver. Layer (line 83-89)
content_layers_default = ['conv_3']
style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']

# VGG19 ver. Model (line 214-218)
cnn = models.vgg19(pretrained=True).features.to(device).eval()
```

Resnet50 모델을 통해 실행 결과를 보고 싶다면 [neural_style.py](./api/neural_style.py) 파일을 열어 layer와 model을 다음과 같이 수정해야 합니다.

```python
# resnet50 ver. Layer (line 83-89)
content_layers_default = ['conv_1']
style_layers_default = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']

# resnet50 ver. Model (line 214-218)
cnn = models.resnet50(pretrained=True).to(device).eval()
```

## Reference

- [A Neural Algorithm of Artistic Style - Leon A. Gatys, Alexander S. Ecker, Matthias Bethge](https://arxiv.org/abs/1508.06576)
- [alexis-jacq/Pytorch-Tutorials](https://github.com/alexis-jacq/Pytorch-Tutorials)
- [NEURAL TRANSFER USING PYTORCH by Alexis Jacq - Winston Herring](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

## License

All of source codes under our project are using [MIT License](http://opensource.org/licenses/MIT).

## Bletcher Team

- 권혁진 - [@KimKwon](https://github.com/KimKwon) - khj9709@icloud.com
- 김동규 - [@kimdg1105](https://github.com/kimdg1105) - kimss7334@naver.com
- 서그림 - [@Seogeurim](https://github.com/Seogeurim) - geulims@naver.com
- 윤가영 - [@yoongoing](https://github.com/yoongoing) - rkdud0925@hanyang.ac.kr
