from typing import Any


def generate_model_expected_data(
    characteristic_type: str,
    characteristic_value: Any,
) -> dict[str, Any]:
    data = {
        characteristic_type: {
            "uuid": f"{characteristic_value.uuid}",
            "name": characteristic_value.name,
        },
    }

    match characteristic_type:
        case "profession":
            data[characteristic_type].update(
                {
                    "experience": characteristic_value.experience,
                    "additional_skill": characteristic_value.additional_skill,
                },
            )
        case "hobby":
            data[characteristic_type]["experience"] = characteristic_value.experience
        case "phobia":
            data[characteristic_type]["stage"] = characteristic_value.stage
        case "disease":
            data[characteristic_type].update(
                {
                    "degree_percent": characteristic_value.degree_percent,
                    "is_curable": characteristic_value.is_curable,
                },
            )
        case "baggage":
            data[characteristic_type]["status"] = characteristic_value.status

    return data
