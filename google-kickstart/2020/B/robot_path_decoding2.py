"""
Memory requirements were met by treating location as also vector.
"""


def movement(move, vector):
    EDGE = 10**9
    MOVEMENT_DICT = {
                "N" : (0, -1),
                "S": (0, 1),
                "W": (-1, 0),
                "E": (1, 0)
                }
    vector[0], vector[1] = (MOVEMENT_DICT[move][0] + vector[0]) % EDGE, (MOVEMENT_DICT[move][1] + vector[1]) % EDGE

def script_vector(i, script_list, vector):
    EDGE = 10**9
    while i < len(script_list):
        num_temp = list()
        # Special case: Start of program
        if script_list[i].isdigit():
            while script_list[i].isdigit():
                num_temp.append(script_list[i])
                i += 1
            multiplier = int("".join(num_temp))
            if script_list[i] == "(":
                i += 1
                program_vector = [0, 0]
                i = script_vector(i, script_list, program_vector)
                vector[0], vector[1] = (vector[0] + program_vector[0] * multiplier) % EDGE, (vector[1] + program_vector[1] * multiplier) % EDGE
            else:
                print("Something wrong.")

        # Special case: End of program
        elif script_list[i] == ")":
            return i + 1
        # Normal case: letter
        else:
            movement(script_list[i], vector)
            i += 1

    return i

def navigate(script):
    location = [0, 0]
    script_vector(0, list(script), location)
    return [x + 1 for x in location]


if __name__ =="__main__":
    cases = input()
    for case in range(int(cases)):
        script = input()
        w, h = navigate(script)
        print("Case #"+ str(case + 1) + ": " + str(w) + " " + str(h))
