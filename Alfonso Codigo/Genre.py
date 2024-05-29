# Importar los módulos necesarios para la ejecución del programa.
from enum import Enum
class GENRE(Enum):
    """
    Enum for the genres of the books.

    This class defines the possible genres for the books.
    """
    FICTION=1
    NON_FICTION=2
    FANTASY=3
    SCIENCE_FICTION=4

def main():
    """Function main of the module.

    The function main of this module is used to test the Class GENRE.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class GENRE - Name.")
    print("=================================================================.")

    if isinstance(GENRE.FICTION, GENRE):
        print("Test PASS. The enum for FICTION has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.NON_FICTION, GENRE):
        print("Test PASS. The enum for NON_FICTION has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.FANTASY, GENRE):
        print("Test PASS. The enum for FANTASY has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(GENRE.SCIENCE_FICTION, GENRE):
        print("Test PASS. The enum for SCIENCE_FICTION has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()