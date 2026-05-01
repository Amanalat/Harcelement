import re
import base64
import os

html_file = "2_Insta_de_Clara.html"
images_dir = "images_clara"

os.makedirs(images_dir, exist_ok=True)

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'data:image/(jpeg|jpg|png|gif|webp);base64,([A-Za-z0-9+/=]+)'
matches = list(re.finditer(pattern, content))

print(f"{len(matches)} image(s) base64 trouvée(s)")

counters = {}
replacements = {}

for match in matches:
    full_data_uri = match.group(0)
    if full_data_uri in replacements:
        continue  # déjà traité

    ext = match.group(1)
    if ext == "jpg":
        ext = "jpeg"
    b64_data = match.group(2)

    counters[ext] = counters.get(ext, 0) + 1
    filename = f"clara_{ext}_{counters[ext]:02d}.{ext if ext != 'jpeg' else 'jpg'}"
    filepath = os.path.join(images_dir, filename)

    img_bytes = base64.b64decode(b64_data)
    with open(filepath, "wb") as img_file:
        img_file.write(img_bytes)

    replacements[full_data_uri] = f"{images_dir}/{filename}"
    print(f"  -> {filename} ({len(img_bytes)//1024} Ko)")

for data_uri, path in replacements.items():
    content = content.replace(data_uri, path)

output_file = "2_Insta_de_Clara.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nFait ! {len(replacements)} image(s) extraite(s) dans '{images_dir}/'")
print(f"HTML mis a jour : {output_file}")
