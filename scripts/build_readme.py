"""Regenerate the plan table in README.md from data/limits.json (stdlib only)."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- table:start -->", "<!-- table:end -->"


def price(plan):
    p = plan.get("priceUsd")
    if p is None:
        return f"{plan['name']} (custom)"
    if p == 0:
        return plan["name"] if "free" in plan["name"].lower() else f"{plan['name']} free"
    return f"{plan['name']} ${p:g}"


def main():
    data = json.loads((ROOT / "data" / "limits.json").read_text(encoding="utf-8"))
    rows = ["| Tool | Vendor | Plans (USD / month) | Limits, sources, FAQ |", "|---|---|---|---|"]
    for t in data["tools"]:
        plans = ", ".join(price(p) for p in t["plans"])
        rows.append(f"| {t['name']} | {t['vendor']} | {plans} | [{t['id']}]({t['page']}) |")
    table = "\n".join(rows) + f"\n\nData checked up to **{data['updated']}**."
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = re.sub(re.escape(START) + ".*?" + re.escape(END), f"{START}\n{table}\n{END}", readme, flags=re.S)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
