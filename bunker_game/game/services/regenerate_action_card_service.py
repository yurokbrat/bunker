from bunker_game.game.models import ActionCard, ActionCardUsage, Personage


class RegenerateActionCardService:
    def __call__(self, personage: Personage) -> ActionCardUsage:
        if (
            current_card_usage := ActionCardUsage.objects.filter(
                personage=personage,
                is_used=False,
            )
            .order_by("?")
            .first()
        ):
            current_card_usage.delete()
        new_card = ActionCard.objects.order_by("?").first()
        return ActionCardUsage.objects.create(  # type: ignore[misc]
            card=new_card,
            personage=personage,
            game=personage.game,
            is_used=False,
        )
