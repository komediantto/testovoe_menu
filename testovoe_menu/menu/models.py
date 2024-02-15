from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название меню")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return str(self.name)


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
        verbose_name="Родитель",
    )
    url = models.CharField(max_length=255, blank=True)
    menu_name = models.ForeignKey(
        Menu, on_delete=models.CASCADE, verbose_name="Название меню"
    )

    class Meta:
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"

    def __str__(self):
        return str(self.name)
