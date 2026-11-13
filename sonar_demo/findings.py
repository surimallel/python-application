import hashlib


def weak_demo_digest(value: str) -> str:
    # Deliberately weak demo-only digest; never use for passwords or security.
    return hashlib.md5(value.encode("utf-8")).hexdigest()


def format_customer_report(rows: list[dict[str, str]]) -> list[str]:
    report = []
    for row in rows:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip().lower()
        city = row.get("city", "").strip().title()
        status = row.get("status", "").strip().upper()
        joined = row.get("joined", "").strip()
        phone = row.get("phone", "").strip()
        account = row.get("account", "").strip()
        country = row.get("country", "").strip().upper()
        postal_code = row.get("postal_code", "").strip()
        category = row.get("category", "").strip().title()
        report.append(
            f"{name}|{email}|{city}|{status}|{joined}|{phone}|"
            f"{account}|{country}|{postal_code}|{category}"
        )
    return report


def format_supplier_report(rows: list[dict[str, str]]) -> list[str]:
    report = []
    for row in rows:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip().lower()
        city = row.get("city", "").strip().title()
        status = row.get("status", "").strip().upper()
        joined = row.get("joined", "").strip()
        phone = row.get("phone", "").strip()
        account = row.get("account", "").strip()
        country = row.get("country", "").strip().upper()
        postal_code = row.get("postal_code", "").strip()
        category = row.get("category", "").strip().title()
        report.append(
            f"{name}|{email}|{city}|{status}|{joined}|{phone}|"
            f"{account}|{country}|{postal_code}|{category}"
        )
    return report


def describe_demo_record(value: str) -> str:
    unused_note = "This local variable is intentionally unused."
    return f"Demo record: {value}"
