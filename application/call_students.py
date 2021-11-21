## call student names
import sys

def call_students(path = []):
    import os, json
    if len(path)==2: # if the function was called with a directory of the students
        path_to_json = path[1] # make the path what ever was called
        if not path_to_json.endswith("\\students"):
            raise ValueError("""Path entered doesn't end with 'students'. Probably wrong path.
            You may try calling the file without any path and it might work, otherwise try writing the correct path to the students folder""")

    else:
        # get path where file is saved (not where it is run from). it's longer but it's safer
        app_path = os.path.realpath(__file__)
        # take away the slashes and lose "application\\call_students.py":
        split_path = app_path.split('\\')[0:-2]
        if len(split_path) == 1:  # in case it is run on a different system, slashes might be forward slashes
            split_path = app_path.split('/')[0:-2]
            if len(split_path) == 1:
                raise FileNotFoundError("The script can't separate the file path of where 'call_students' is located and so it can't go back and approach the 'students' folder.")

            # add "students" folder to the path
            split_path.append("students")
            # join the strings and create a path
            path_to_json = "/".join(split_path)

        # add "students" folder to the path
        split_path.append("students")
        path_to_json = "\\".join(split_path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which names will be added
    name_list = list()

    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_text = json.load(current_json_file)
            # get name from text of current json file:
            current_name = current_json_text['name']
            # add name to list:
            name_list.append(current_name)

    # sort names (case insensitive)
    sorted_list = sorted(name_list, key=str.casefold)
    return (sorted_list)

def name_to_json(name):
    import os, json

    # get path where file is saved (not where it is run from). it's longer but it's safer
    app_path = os.path.realpath(__file__)
    # take away the slashes and lose "application\\call_students.py":
    split_path = app_path.split('\\')[0:-2]
    if len(split_path) == 1:  # in case it is run on a different system, slashes might be forward slashes
        split_path = app_path.split('/')[0:-2]
        if len(split_path) == 1:
            raise FileNotFoundError("The script can't separate the file path of where 'call_students' is located and so it can't go back and approach the 'students' folder.")

        # add "students" folder to the path
        split_path.append("students")
        # join the strings and create a path
        path_to_json = "/".join(split_path)

    # add "students" folder to the path
    split_path.append("students")
    path_to_json = "\\".join(split_path)

    # get the names of all the files as a list
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    # create empty list to which names will be added
    name_list = list()

    # create full directories using os.path.join
    for index, js in enumerate(json_files):
        # by using "with" we can execute the opening and the loading without needing to close the file
        with open(os.path.join(path_to_json, js)) as current_json_file:
            current_json_loaded = json.load(current_json_file)
            # get name from text of current json file:
            current_name = current_json_loaded['name']
            if current_name == name:
                break

    return (current_json_loaded)

def main(args):
    print(call_students(args))

if __name__ == '__main__':
    main(sys.argv)

