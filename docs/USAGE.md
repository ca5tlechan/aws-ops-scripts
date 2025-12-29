# Usage (aws-ops-scripts)

운영자/플랫폼 엔지니어 관점에서 반복 가능한 점검 스크립트를 제공합니다.

## Prerequisites
- Python 3.10+
- AWS CLI configured (`aws configure`)

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## AWS auth check
```bash
aws sts get-caller-identity
```

## sg_audit.py (planned)
- 목적: Security Group에서 과도하게 열린 인바운드 규칙(예: 0.0.0.0/0)을 탐지해 리포트합니다.
- 안전: 기본은 조회(Read-only)만 수행합니다.
- 범위: 기본적으로 `Project=aws-infra-blueprint` 태그가 있는 리소스만 대상으로 합니다.

## Evidence
- 결과 스크린샷/출력은 `docs/assets/`에 저장합니다.
- 파일명 규칙 권장: `YYYY-MM-DD-<topic>.png`
