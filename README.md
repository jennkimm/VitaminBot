# VitaminBot

카카오톡 플러스친구에 '비타민챗봇' 채널을 개설하였습니다.

이 챗본은 크게 2개의 시나리오로 나뉘며, 각각 두 개의 스킬을 사용해 결과를 출력합니다.

### 스킬1 - 사용자가 증상을 입력하면 결핍된 비타민을 출력합니다.

이는 사전에 크롤링한 데이터를 csv 파일에 저장해놓고, 사용자 발화를 머신러닝으로 분석해 뽑아낸 증상 파라미터가 넘어면 csv 파일에 증상에 대응되는 비타민을 찾아 출력해줍니다.

python3.7, numpy, pandas 를 사용하였으며 AWS Lambda + API Gateway 를 활용해 API 를 생성했습니다.

* API URL: https://2x3b6faw4l.execute-api.us-east-2.amazonaws.com/default/get_symptom
* 참고 사이트 : https://medium.com/@korniichuk/lambda-with-pandas-fd81aa2ff25e

### 스킬2 - 아이허브 사이트에서 사용자 맞춤 비타민을 검색해 결과를 불러옵니다.

사용자의 성별, 나이대를 바탕으로 결핍된 비타민이 함유되어있는 비타민 제품들을 크롤링해 결과를 출력해줍니다.
이도 또한 AWS Lambda 를 이용해 API 를 생성하려고 했으나, webdriver 를 사용하는데 있어서 문제를 극복하지 못했습니다. AWS Lambda 에서 제공하는 파이썬 기본 라이브러리에 포함되지 않아 따로 설치해줘야 하는데, 버전호환성도 까다롭고, 배포서버(pythonanywhere) 의 보안문제가 있어,
Django 백엔드, Beautifulsoup 를 사용했고, AWS EC2 에 배포하였습니다.

* API URL : ec2-3-135-233-3.us-east-2.compute.amazonaws.com (현재 작동하지 않음)

