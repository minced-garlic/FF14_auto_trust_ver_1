# FF14_auto_trust_ver_1
파이널 판타지 14의 트러스트 던전을 자동으로 돌아주는 프로그램입니다. (작성 중. pretraining까지 완료.)

사용방법
1. 데이터 모으기
    0_get_data_from_keyboard.py 를 통해 트러스트 던전을 도는 딥러닝 데이터 파일을 만들 수 있습니다.
    해당 파일을 실행한 후, 's'를 누르면 코딩이 시작되며, 'e'를 누르면 코딩이 종료됩니다.
    (해당 코드는 던전을 돌면서 키보드만을 이용하기 때문에 키보드만을 이용하여 던전을 돌아 데이터 파일을 만들어야 합니다.)
2.  create pretraining data 
    1_create_pretraining_data.py 를 동해 pretraining 데이터를 만듭니다. ※해당 모델은 NLP의 bert-model을 차용, 변형한 것입니다.※
3.  run pretraining
    2_run_pretraining.py 를 통해 BERT모델의 pretraining을 합니다.
4.  run classifier
    3_run_classifier.py를 통해 BERT 모델 학습을 진행합니다.
5.  create data
    학습이 진행되고 나면, 해당 학습을 기반으로 만들어진 모델을 가지고 다시 예시 데이터를 만듭니다. 예시데이터는 4_create_data.py를 이용하면 만들 수 있습니다.
6.  다시, 학습
    4_create_data.py를 통해 만들어진 데이터를 학습하며 적용합니다. 중간에 HP 0이 되면 해당 데이터는 거기까지만 저장됩니다.
7.  만들어진 데이터를 가지고 다시금 2번부터 진행.

