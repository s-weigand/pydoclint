class MyClass:
    def __init__(self):
        pass

    @staticmethod
    def func1_1(arg1: int, arg2: float) -> None:
        pass

    @staticmethod
    def func1_1a(arg1: int, arg2: float) -> None:
        MyClass.func2(arg1, arg2)

    @staticmethod
    def func1_2(arg1: int, arg2: float) -> None:
        """"""
        pass

    @staticmethod
    def func1_3(arg1: str, arg2: list[int]) -> bool:
        """Something

        Returns
        -------
        bool
            Something else
        """
        return True

    @staticmethod
    def func1_4() -> bool:
        return False

    @staticmethod
    def func1_5() -> None:
        """Something

        Returns
        -------
        None
        """
        return None

    @staticmethod
    def func1_6() -> None:
        """
        Something

        Parameters
        ----------
        arg1 : int
            Arg 1

        Returns
        -------
        None
        """
        return None

    @staticmethod
    def func2(arg1: int, arg2: float | int | None) -> int | list[float]:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    @staticmethod
    def func3(arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1
        arg2 : float
            Arg 2
        arg3 : Optional[Union[float, int, str]]
            Arg 3

        Returns
        -------
        int :
            Result
        """
        return 1

    @staticmethod
    async def func4(arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg2 : float
            Arg 2
        arg1 : int
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    @staticmethod
    def func5(arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : list[str]
            Arg 1
        arg2 : str
            Arg 2

        Returns
        -------
        int :
            Result
        """
        return 1

    @staticmethod
    def func6(arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg2 : str
            Arg 2
        arg1 : list[str]
            Arg 1

        Returns
        -------
        int :
            Result
        """
        return 1

    @staticmethod
    def func7(arg1: int, arg2: float) -> int:
        """
        Do something.

        Parameters
        ----------
        arg1 : int
            Arg 1
        arg2 : float
            Arg 2

        Returns
        -------
        int :
            Result
        """

        def func72(arg3: list, arg4: tuple, arg5: dict) -> None:
            """
            Do something else

            arg100: int
                Some arg

            Returns
            -------
            None
            """
            return None

        return 2

    @staticmethod
    def func8(arg1: 'MyClass', arg2: 'SomeClass') -> int:
        """
        Something

        Parameters
        ----------
        arg1 : MyClass
            Arg 1
        arg2 : SomeClass
            Arg 2

        Returns
        -------
        int
            Result
        """
        return MyClass()
