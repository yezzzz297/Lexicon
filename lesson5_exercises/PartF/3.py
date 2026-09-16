
def create_report(title, *sections, **metadata):
    report = {
        "title": title,
        "sections": list(sections),
    }
    report.update(metadata)
    return report


report = create_report(
    "Launch Notes",
    "Overview",
    "Risks",
    author="Nina",
    department="Operations",
    version=2,
    confidential=True,
    date="2026-09-16",
)
print(report)
