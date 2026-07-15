# CLAUDE.md

이 파일은 Claude Code가 이 리포지토리에서 작업할 때 참고하는 규칙을 담는다.

## 기술 스택

- Python 3 (표준 라이브러리 `random`/`json`만 사용, 외부 의존성 없음)

## 실행 / 테스트

```
python generator.py --samples 5 --orders 10
python generator.py --samples 3 --seed 42                 # 재현 가능한 난수
python generator.py --orders 20 --data-dir <path>          # 다른 DB에 직접 추가
```

## 설계 원칙

- 시료 ID(`S-xxx`)/주문번호(`ORD-xxxx`)는 기존 데이터의 최대 번호 다음 순번으로 자동 채번한다(직접 랜덤 ID를 쓰지 않음).
- 주문 생성 시 `sample_id`는 반드시 이미 존재하는 시료 중에서 선택하여 참조 무결성을 유지한다(존재하지 않는 시료를 참조하는 주문을 만들지 않음).
- `--seed` 옵션은 테스트 재현성을 위한 것이며, 지정하지 않으면 매 실행마다 다른 데이터가 생성된다.
