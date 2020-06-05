def right_justify(str):
    length_str=len(str)
    num_spaces=70-length_str
    print(" "*num_spaces+str)
right_justify("Hi, im duc")