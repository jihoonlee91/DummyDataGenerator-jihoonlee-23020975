"""
DummyDataGenerator-jihoonlee-23020975
테스트를 위한 Dummy Sample/Order 데이터를 생성하여 연결된 JSON DB에 추가하는 도구.

사용법:
  python generator.py --samples 5 --orders 10
  python generator.py --samples 5 --orders 10 --data-dir ../DataPersistence-jihoonlee-23020975/data
  python generator.py --samples 5 --orders 10 --seed 42   # 재현 가능한 난수 시드
"""
import argparse
import json
import os
import random

SAMPLE_NAME_POOL = [
    "실리콘 웨이퍼-8인치",
    "GaN 에피택셜-4인치",
    "SiC 파워기판-6인치",
    "포토레지스트-PR7",
    "산화막 웨이퍼-SiO2",
    "질화막 웨이퍼-Si3N4",
    "사파이어 기판-2인치",
    "게르마늄 웨이퍼-4인치",
]

CUSTOMER_POOL = [
    "삼성전자 파운드리",
    "SK하이닉스",
    "LG이노텍",
    "DB하이텍",
    "한양대 반도체연구실",
    "카이스트 나노랩",
]

ORDER_STATUS_POOL = ["RESERVED", "PRODUCING", "CONFIRMED", "RELEASE"]


def load_json(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, records: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def next_id(records: list[dict], id_field: str, prefix: str, width: int) -> str:
    max_seq = 0
    for record in records:
        raw = record.get(id_field, "")
        digits = "".join(ch for ch in raw if ch.isdigit())
        if digits:
            max_seq = max(max_seq, int(digits))
    return f"{prefix}{max_seq + 1:0{width}d}"


def generate_samples(count: int, existing: list[dict]) -> list[dict]:
    generated = []
    records = list(existing)
    for _ in range(count):
        sample_id = next_id(records, "sample_id", "S-", 3)
        record = {
            "sample_id": sample_id,
            "name": random.choice(SAMPLE_NAME_POOL),
            "avg_process_time": round(random.uniform(0.2, 1.0), 2),
            "yield_rate": round(random.uniform(0.75, 0.98), 2),
            "stock": random.randint(0, 500),
        }
        records.append(record)
        generated.append(record)
    return generated


def generate_orders(count: int, existing: list[dict], sample_ids: list[str]) -> list[dict]:
    generated = []
    records = list(existing)
    for _ in range(count):
        order_id = next_id(records, "order_id", "ORD-", 4)
        record = {
            "order_id": order_id,
            "sample_id": random.choice(sample_ids) if sample_ids else "S-001",
            "customer": random.choice(CUSTOMER_POOL),
            "quantity": random.randint(10, 500),
            "status": random.choice(ORDER_STATUS_POOL),
        }
        records.append(record)
        generated.append(record)
    return generated


def main() -> None:
    parser = argparse.ArgumentParser(description="Dummy 데이터 생성 도구")
    parser.add_argument("--data-dir", default="data", help="데이터를 추가할 폴더 경로")
    parser.add_argument("--samples", type=int, default=0, help="생성할 더미 시료 수")
    parser.add_argument("--orders", type=int, default=0, help="생성할 더미 주문 수")
    parser.add_argument("--seed", type=int, default=None, help="재현 가능한 난수 시드")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    samples_path = os.path.join(args.data_dir, "samples.json")
    orders_path = os.path.join(args.data_dir, "orders.json")

    existing_samples = load_json(samples_path)
    existing_orders = load_json(orders_path)

    if args.samples > 0:
        new_samples = generate_samples(args.samples, existing_samples)
        save_json(samples_path, existing_samples + new_samples)
        print(f"더미 시료 {len(new_samples)}건 생성 완료 -> {samples_path}")

    if args.orders > 0:
        all_samples = load_json(samples_path)
        sample_ids = [s["sample_id"] for s in all_samples]
        new_orders = generate_orders(args.orders, existing_orders, sample_ids)
        save_json(orders_path, existing_orders + new_orders)
        print(f"더미 주문 {len(new_orders)}건 생성 완료 -> {orders_path}")

    if args.samples <= 0 and args.orders <= 0:
        print("생성할 --samples 또는 --orders 개수를 지정하세요.")


if __name__ == "__main__":
    main()
