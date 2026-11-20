# project name normalizer service
import re
from errors import InvalidProjectName

"""""
Task: Given the string for a project name, strip the whitespace and normalize the string.
 ex. "   Cloud Nine   " -> "cloud-nine"         "MtSac C.S. Club" -> "mtsac-cs-club"
 ex. "Sunny California!" -> "sunny-california"  "Subaru FA24" -> "subaru-fa24"
 ex. "    " -> Raise error, reject empty strings.
"""""
def normalize_project(project: str) -> str:
    project = project.strip().lower()
    project = re.sub(r"[^a-z0-9]+", "-", project)
    project = project.strip("-")

    if not project:
        raise InvalidProjectName()

    return project