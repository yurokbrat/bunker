from rest_framework.serializers import BaseSerializer


class SerializerByActionMixin:
    serializer_action_classes: dict[str, type[BaseSerializer]]

    def get_serializer_class(self) -> type[BaseSerializer]:
        return self.serializer_action_classes.get(self.action, self.serializer_class)  # type: ignore[attr-defined]
