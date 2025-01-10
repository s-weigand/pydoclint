"""This case should not find the following violation:

DOC503: Function `ensure_unique_tuple` exceptions in the "Raises" section in the docstring do not
match those in the function body Raises values in the docstring: ['TupleDuplicateException'].
Raised exceptions in the body: ['TupleDuplicateException.from_tuple'].
"""

from __future__ import annotations


class TupleDuplicateException(Exception):
    """Exception raised when a tuple contains duplicates."""

    @classmethod
    def from_tuple(cls, value: tuple[int, ...]) -> TupleDuplicateException:
        """Create new exception instance from tuple ``value``.

        Parameters
        ----------
        value : tuple[int,...]
            Tuple containing duplicate values.

        Returns
        -------
        TupleDuplicateException
            New exception instance.
        """
        return cls(f"Duplicate values detected in: {value}")


def ensure_unique_tuple(value: tuple[int, ...]):
    """Ensure that all values in the tuple are unique.

    Parameters
    ----------
    value : tuple[int,...]
        Tuple to check

    Raises
    ------
    TupleDuplicateException
        If the tuple contains duplicate values.
    """
    if len(value) != len(set(value)):
        raise TupleDuplicateException.from_tuple(value)
