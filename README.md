# Prequisites

- Python 3
- Terminal
- Code Editor
- Organized dataset folder

# Usage

- Clone or download the python file
- Copy the script inside your dataset folder
- Run the script by typing `python split_script.py`

# Customizable Parameters

There's a few variables that you have to customize in order for this script to work with your specific dataset folder:

| Variables                                      | Type   | Description                                        | Example                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ignore_folders`                               | List   | Used to tell the script to ignore folders or files | `['train', 'validation', 'test'`                                                                                                                                                                                         |
| `parent_dir`                                   | String | Used to define parent dataset folder               | "D://DATASET//cocoa-ripeness-dataset-v3"                                                                                                                                                                                 |
| `train_split` `validation_split`, `test_split` | Float  | Decimal number to define portions to split         | if splitting train, validation, and testing 80%, 10%, and 10% repectively, then define `0.8`, `0.5`, `1`. Remember the order the splitting happens, because it affects the remainder of number of files in the directory |
