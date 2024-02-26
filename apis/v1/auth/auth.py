"""Auth Module
"""
from typing import List


class Auth:
    """a class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path(str): Url path to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        if path in excluded_paths:
            return False
        else:
            for i_path in excluded_paths:
                if path.startswith(i_path) or i_path.startswith(path):
                    return False

        return False
