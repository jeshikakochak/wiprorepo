#traffic lights as input in a match case which yields meaning of lights
color = input("enter traffic light color:")
match color:
    case "red":
        print("stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("invalid color")