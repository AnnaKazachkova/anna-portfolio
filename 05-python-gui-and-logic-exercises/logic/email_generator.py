"""Generate student e-mail addresses from a class list and organise the output.

Part 1  find the *_IE.txt files and read the 3rd one
Part 2  skip the 2 header lines; for each name take the first 3 letters of
        the first name and surname, lowercase, and add the domain
Part 3  write email.txt, move it to ./results, copy it back, rename the copy
Expects a folder called IEtxt next to this script.
"""
import shutil
from pathlib import Path

# Part 1
base_path = Path(__file__).parent / "IEtxt"
files = sorted(base_path.glob("*_IE.txt"))
file_lines = files[2].read_text(encoding="utf-8").splitlines()

# Part 2
domain = "@student.ie.edu"
emails = []
student_lines = file_lines[2:]  # skip the 2 header lines
for line in student_lines:
    line = line.strip()
    if not line:  # empty line
        continue
    parts = line.split()
    if len(parts) < 2:  # needs at least a name and a surname
        continue
    first_name = parts[0].lower()
    surname = parts[-1].lower()  # parts[-1] avoids middle names
    email_name = first_name[:3] + surname[:3]
    emails.append(f"{email_name}{domain}")

print(f"generated {len(emails)} emails.")

# Part 3
filename = "email.txt"
file_path = Path(filename)
file_path.write_text("\n".join(emails), encoding="utf-8")

results_folder = base_path / "results"
results_folder.mkdir(exist_ok=True)
moved_file_path = results_folder / filename
file_path.rename(moved_file_path)

copied_file_path = Path(".") / filename
shutil.copy(moved_file_path, copied_file_path)
copied_file_path.rename(Path("file_backup.txt"))

print(emails)
