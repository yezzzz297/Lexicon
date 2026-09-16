
def summarize_report(report):
    result = [f"Title: {report.get('title', 'No title')}"]

    for item in report.get('sections', []):
        result.append(f"- {item}")

    for key, value in report.items():
        if key not in {"title", "sections"}:
            result.append(f"{key}: {value}")

    return "\n".join(result)


report = {
    "title": "My Day",
    "sections": ["Morning", "Afternoon"],
    "name": "Yetnayet",
    "city": "Stockholm",
}
print(summarize_report(report))
