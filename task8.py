import json
python_object = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(python_object)
json_object = json.loads(python_object)
print("\nUnique Key in a JSON object:")
print(json_object)