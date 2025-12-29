# aws-ops-scripts

AWS 운영/점검/정리 작업을 자동화하기 위한 스크립트 모음입니다.  
학습 노트가 아니라, 운영 도구 형태로 재현 가능하게 만드는 것이 목표입니다.

## What this repo focuses on
- 반복 점검을 스크립트로 자동화
- 태그 기반 조회로 안전하게 범위 제한
- 실행 결과를 문서/스크린샷으로 남겨 증빙

## Planned scripts
- `src/sg_audit.py`: Security Group 위험 규칙(예: 0.0.0.0/0) 탐지 리포트
- (추후) `inventory_ec2.py`: EC2 인벤토리(CSV) 출력

## Safety rules
- AWS 자격증명(Access Key/Secret)은 레포에 저장하지 않습니다.
- 기본 정책: `Project=aws-infra-blueprint` 태그가 있는 리소스만 조회합니다.

## Usage / Evidence
- 사용법: `docs/USAGE.md`
- 증빙 스크린샷: `docs/assets/` (YYYY-MM-DD-topic.png 규칙 권장)
