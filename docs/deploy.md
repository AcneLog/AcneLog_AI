# 배포

1. `aws ecr get-login-password --region region | docker login --username AWS --password-stdin xxxxxxxxxxxx.dkr.ecr.region.amazonaws.com`

2. 다음 명령을 사용하여 도커 이미지를 빌드합니다. 도커 파일을 처음부터 새로 빌드하는 방법에 대한 자세한 내용은 여기  지침을 참조하십시오. 이미지를 이미 빌드한 경우에는 이 단계를 건너뛸 수 있습니다.
`docker build -t acnelog/acnelog-ai .`

3. 빌드가 완료되면 이미지에 태그를 지정하여 이 리포지토리에 푸시할 수 있습니다.
`docker tag acnelog/acnelog-ai:latest xxxxxxxxxxxx.dkr.ecr.region.amazonaws.com/acnelog/acnelog-ai:latest`

4. 다음 명령을 실행하여 이 이미지를 새로 생성한 AWS 리포지토리로 푸시합니다.
`docker push xxxxxxxxxxxx.dkr.ecr.region.amazonaws.com/acnelog/acnelog-ai:latest`