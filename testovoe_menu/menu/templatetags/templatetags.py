from django import template
from menu.models import MenuItem
from loguru import logger

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    current_url = context["request"].path
    menu_items = get_menu_items(menu_name)
    sorted_menu_items = sort_menu_items(menu_items)
    tree = create_menu_tree(sorted_menu_items, menu_name, current_url)
    activate_menu_items(tree, current_url)
    return {
        "menu_tree": tree,
    }


def get_menu_items(menu_name):
    return (
        MenuItem.objects.all()
        .select_related("menu_name", "parent")
        .filter(menu_name__name=menu_name)
        .order_by("parent_id")
    )


def sort_menu_items(menu_items):
    sorted_menu_items = []
    for item in menu_items:
        if item.parent_id is None:
            sorted_menu_items.append(item)
        else:
            for i, sort_item in enumerate(sorted_menu_items):
                if item.parent_id == sort_item.id:
                    sorted_menu_items.insert(i + 1, item)
    return sorted_menu_items


def create_menu_tree(sorted_menu_items, menu_name, current_url):
    tree = []
    active = True
    parent_last_id = root_id = last_active_id = sorted_menu_items[0].id
    for item in sorted_menu_items:
        tree.append(
            {
                "id": item.id,
                "name": item.name,
                "menu_name": menu_name,
                "parent": item.parent_id,
                "url": item.url if item.url != "" else "/",
                "active": active,
            }
        )
        if active:
            last_active_id = item.id
        if item.url == current_url or (item.url == "" and current_url == "/"):
            active = False
    for item in tree:
        if (
            item["parent"] is None
            or item["parent"] == last_active_id
            or item["parent"] == parent_last_id
            or item["parent"] == root_id
        ):
            item["active"] = True
        else:
            item["active"] = False
    return tree


def activate_menu_items(tree, current_url):
    for item in tree:
        if item["url"] == current_url:
            item["active"] = True
            parent_id = item["parent"]
            while parent_id is not None:
                for parent_item in tree:
                    if parent_item["id"] == parent_id:
                        parent_item["active"] = True
                        parent_id = parent_item["parent"]
                        break
                else:
                    parent_id = None
                if parent_id == 1:
                    break
        else:
            continue


@register.simple_tag(takes_context=True)
def render_menu(context, menu_tree, current_item=None):
    result = ""
    for item in menu_tree:
        if item["parent"] == current_item and item["active"] == True:
            result += f'<li><a href="{item["url"]}" {"class=active" if item["active"] else ""}>{item["name"]}</a>'
            sub_menu = render_menu(context, menu_tree, item["id"])
            if sub_menu:
                result += f"<ul>{sub_menu}</ul>"
            result += "</li>"
    return result
