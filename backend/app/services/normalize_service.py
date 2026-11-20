# project name normalizer service


"""""
Task: Given the string for a project name, strip the whitespace and normalize the string.
 ex. "   Cloud Nine   " -> "cloud-nine"         "MtSac C.S. Club" -> "mtsac-cs-club"
 ex. "Sunny California!" -> "sunny-california"  "Subaru FA24" -> "subaru-fa24"
 ex. "    " -> Raise error, reject empty strings.
"""""
def normalize_project(project: str) -> str:
    project = project.strip().lower()
    project = project.replace(" ", "-")
    if project == "":
        raise ValueError("empty string is not allowed")
    return project
