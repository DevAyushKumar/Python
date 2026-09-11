import os

def clear_clutter(folder_path, extension):
    if not extension.startswith("."):
        extension = f".{extension}"

    # 1. Filter out only files ending with the specified extension
    files = [f for f in os.listdir(folder_path) if f.endswith(extension)]

    # 2. Rename to temporary names to avoid collision with existing 1.png, 2.png, etc.
    temp_files = []
    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)
        temp_name = f"__temp_{i}{extension}"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, temp_path)
        temp_files.append(temp_name)

    # 3. Rename from temporary names to final sequential names (1.png, 2.png, ...)
    for count, temp_file in enumerate(temp_files, start=1):
        temp_path = os.path.join(folder_path, temp_file)
        final_name = f"{count}{extension}"
        final_path = os.path.join(folder_path, final_name)
        os.rename(temp_path, final_path)
        print(f"Renamed -> {final_name}")

# Call the function
clear_clutter("Questions/clutter", ".png")

# another meathod
files = os.listdir("clutter")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutter/{file}", f"clutter/{i}.png")
        i += 1
        