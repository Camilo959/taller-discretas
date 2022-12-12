class Lectura:

    def __init__(self) -> None:
        pass

    def read(self, route) -> str: 

        try:
            with open(route, 'r') as f_obj:
                lines = f_obj.readlines()
            return lines
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

            return 'Error'
# file = Lectura()

# mostrar = file.read('asdf')