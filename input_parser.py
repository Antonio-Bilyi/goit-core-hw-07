def parse_input(user_input):

    try:

        cmd, *args = user_input.split()

        cmd = cmd.strip().lower()

        return cmd, *args
    
    except ValueError:

        return 'Error: You input invalid data!'