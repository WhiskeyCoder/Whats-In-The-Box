import os

# Root directory you want to scan
root_dir = r"YOUR/DIRECTORY"
output_file = "directory_structure.txt"

def build_tree(path, prefix=""):
    entries = sorted(os.listdir(path))
    tree_lines = []

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "└── " if index == len(entries) - 1 else "├── "
        tree_lines.append(prefix + connector + entry)

        if os.path.isdir(full_path):
            extension = "    " if index == len(entries) - 1 else "│   "
            tree_lines.extend(build_tree(full_path, prefix + extension))

    return tree_lines

if not os.path.exists(root_dir):
    print("❌ Directory does not exist")
else:
    tree_output = os.path.basename(root_dir) + "/\n"
    tree_output += "\n".join(build_tree(root_dir))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tree_output)

    print(f"✅ Directory structure written to '{output_file}'")
