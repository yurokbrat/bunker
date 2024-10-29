from collections.abc import Sequence

from rest_framework.permissions import BasePermission, OperandHolder


class PermissionByActionMixin:
    permission_action_classes: dict[str, type[BasePermission] | OperandHolder]

    def get_permissions(self) -> Sequence[BasePermission]:
        permissions = self.permission_action_classes.get(
            self.action,  # type: ignore[attr-defined]
            self.permission_classes,  # type: ignore[attr-defined]
        )
        if callable(permissions):
            return [permissions()]  # type: ignore[list-item]
        return [permission() for permission in permissions]
