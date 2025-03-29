import os
from typing import Any, Callable


def safe_call(scraper_method: Callable[[], Any]) -> Any:
    """Attempts to call a given scraper method, returning a default value when an error occurs.

    Args:
        scraper_method (Callable[[], Any]): A method from a `recipe_scrapers` object.

    Returns:
        Any: The method's output if succesfel, otherwise a fallback default value.
    """
    try:
        return scraper_method()
    except Exception:
        match scraper_method.__name__:
            case "author":
                return "Unknown"
            case "cuisine" | "category":
                return "Not specified"
            case "dietary_restrictions":
                return "None"
            case "prep_time" | "cook_time" | "total_time" | "yields":
                return "N/A"
            case "equipment":
                return []
            case "ingredients":
                return []
            case "instructions_list":
                return []
            case _:
                return "Information not available."


def generate_recipe_text(scraper: object, pretty_flag: bool) -> str:
    """Creates Markdown-formatted recipe text.

    Args:
        scraper (object): An object that contains the scraped recipe details.
        pretty_flag(bool): If True, the output is generated with emojis.

    Returns:
        str: A Markdown-formatted recipe string.
    """
    equipment = safe_call(scraper.equipment)
    ingredients = safe_call(scraper.ingredients)
    instructions = safe_call(scraper.instructions_list)

    if pretty_flag:
        md_recipe = f"""
# 🍽️ Recipe: {scraper.title()}

## 📎 Overview
- **Author:** {safe_call(scraper.author)}
- **Cuisine:** {safe_call(scraper.cuisine)}
- **Category:** {safe_call(scraper.category)}
- **Dietary Restrictions:** {safe_call(scraper.dietary_restrictions)}

## ⏲️ Time
- **Prep Time:** {safe_call(scraper.prep_time)} minutes
- **Cook Time:** {safe_call(scraper.cook_time)} minutes
- **Total Time:** {safe_call(scraper.total_time)} minutes
- **Yields:** {safe_call(scraper.yields)}

## 🥣 Equipment
{", ".join(equipment) if equipment else "No special equipment required."}

## 📝 Ingredients
{chr(10).join(f"- {ingredient}" for ingredient in ingredients) if ingredients else "Ingredients not available."}

## 🔪 Instructions
{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(instructions)) if instructions else "No instructions available."}

## 📌 Source
[Original Recipe]({safe_call(scraper.canonical_url)})
    """
    else:
        md_recipe = f"""
# Recipe: {scraper.title()}

## Overview
- **Author:** {safe_call(scraper.author)}
- **Cuisine:** {safe_call(scraper.cuisine)}
- **Category:** {safe_call(scraper.category)}
- **Dietary Restrictions:** {safe_call(scraper.dietary_restrictions)}

## Time
- **Prep Time:** {safe_call(scraper.prep_time)} minutes
- **Cook Time:** {safe_call(scraper.cook_time)} minutes
- **Total Time:** {safe_call(scraper.total_time)} minutes
- **Yields:** {safe_call(scraper.yields)}

## Equipment
{", ".join(equipment) if equipment else "No special equipment required."}

## Ingredients
{chr(10).join(f"- {ingredient}" for ingredient in ingredients) if ingredients else "Ingredients not available."}

## Instructions
{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(instructions)) if instructions else "No instructions available."}

## Source
[Original Recipe]({safe_call(scraper.canonical_url)})
    """

    return md_recipe
