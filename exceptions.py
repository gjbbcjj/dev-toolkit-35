class ValidationError(Exception):
    """Base class for input validation errors in gaming toolkit."""
    pass

class InvalidCommandError(ValidationError):
    """Exception for unrecognized or malformed commands."""
    pass

class InvalidParameterError(ValidationError):
    """Exception for invalid command parameters."""
    def __init__(self, param, reason):
        self.param = param
        self.reason = reason
        super().__init__(f"{param}: {reason}")

class OutOfBoundsError(ValidationError):
    """Exception for values outside allowed range."""
    def __init__(self, value, minv, maxv):
        self.value = value
        super().__init__(f"{value} not in [{minv}, {maxv}]")

def validate_input(command, params):
    """Perform input validation for game commands."""
    valid_cmds = {"move", "attack", "defend", "use_item"}
    if command not in valid_cmds:
        raise InvalidCommandError(f"Unknown command: {command}")
    if command == "move" and "dir" not in params:
        raise InvalidParameterError("dir", "direction required")
    if command == "attack":
        dmg = params.get("damage", 0)
        if not isinstance(dmg, int) or dmg < 5 or dmg > 200:
            raise OutOfBoundsError(dmg, 5, 200)
    return True

def process_command(command, params):
    """Process a validated command (stub for gaming logic)."""
    print(f"Processed {command} with {params}")

def main_processing_loop():
    """Main loop that reads, validates and processes inputs."""
    print("Starting dev-toolkit-35 game input loop")
    while True:
        try:
            line = input("game> ").strip().lower()
            if line == "quit":
                break
            tokens = line.split()
            if not tokens:
                continue
            command = tokens[0]
            params = {}
            if len(tokens) > 1:
                if command == "move":
                    params["dir"] = tokens[1]
                elif command == "attack":
                    params["damage"] = int(tokens[1]) if tokens[1].isdigit() else 10
                else:
                    params["args"] = tokens[1:]
            validate_input(command, params)
            process_command(command, params)
        except ValidationError as err:
            print(f"Validation error: {err}")
        except ValueError:
            print("Invalid number format")
        except EOFError:
            break

if __name__ == "__main__":
    main_processing_loop()