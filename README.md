# DummyDataGenerator-jihoonlee-23020975

**Dummy 데이터 생성 Tool** PoC입니다. 테스트를 위한 더미 Sample/Order 데이터를
생성하여 연결된 JSON DB(`data/`)에 추가합니다.

## 구조

```
generator.py   # 더미 데이터 생성 로직 및 CLI
data/          # 생성된 데이터가 누적 저장되는 폴더 (최초 실행 시 자동 생성)
```

## 실행

```
python generator.py --samples 5 --orders 10          # 더미 시료 5건, 주문 10건 생성
python generator.py --samples 3 --seed 42             # 재현 가능한 난수로 시료 3건 생성
python generator.py --orders 20 --data-dir ../DataPersistence-jihoonlee-23020975/data   # 다른 PoC의 DB에 직접 추가
```

- 시료 ID(`S-xxx`), 주문번호(`ORD-xxxx`)는 기존 데이터의 최대 번호 다음 순번으로 자동 채번됩니다.
- 주문 생성 시 `sample_id`는 이미 등록된 시료 중에서 무작위로 선택되어 참조 무결성을 유지합니다.

## 관련 리포지토리

개인과제 미션1(PoC 4종) + 미션2(최종 프로젝트)의 일부입니다. 여기서 검증한 자동 채번/참조
무결성 유지 방식은 최종 프로젝트인
[SampleOrderSystem-jihoonlee-23020975](https://github.com/jihoonlee91/SampleOrderSystem-jihoonlee-23020975)의
1000건 규모 스트레스 테스트(성능 검증용 더미 데이터 생성)에 활용되었습니다.

- [SampleOrderSystem-jihoonlee-23020975](https://github.com/jihoonlee91/SampleOrderSystem-jihoonlee-23020975) (미션2, 최종 프로젝트)
- [ConsoleMVC-jihoonlee-23020975](https://github.com/jihoonlee91/ConsoleMVC-jihoonlee-23020975) (PoC: MVC 스켈레톤)
- [DataPersistence-jihoonlee-23020975](https://github.com/jihoonlee91/DataPersistence-jihoonlee-23020975) (PoC: 데이터 영속성, 본 PoC가 데이터를 추가하는 대상)
- [DataMonitor-jihoonlee-23020975](https://github.com/jihoonlee91/DataMonitor-jihoonlee-23020975) (PoC: 데이터 모니터링, 본 PoC가 생성한 데이터를 조회)
