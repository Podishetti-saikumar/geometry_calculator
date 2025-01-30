from shapes import Point, Line, Circle, Rectangle

def main():
    variables = {}
    allowed_classes = {'Point': Point, 'Line': Line, 'Circle': Circle, 'Rectangle': Rectangle}
    print("Geometric Calculator. Enter commands. Type 'exit' to quit.")
    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue
            if command.lower() == 'exit':
                break
            if '=' in command:
                var_name, expr = command.split('=', 1)
                var_name = var_name.strip()
                local_vars = {**allowed_classes, **variables}
                obj = eval(expr.strip(), {'__builtins__': None}, local_vars)
                variables[var_name] = obj
                print(f"{var_name}{repr(obj)}")
            else:
                result = eval(command, {'__builtins__': None}, variables)
                print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()