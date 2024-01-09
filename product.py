class Product:
  def __init__(self, icon, prize):
    self.icon = icon
    self.prize = prize
    return Row(
                    [
                        Text(self.icon, size=50),
                        Text(self.prize),
                        Container(
                            width=100,
                            content=TextField(
                                value="0", read_only=True
                            ),
                        ),
                        IconButton(icon=icons.ADD),
                        IconButton(icon=icons.REMOVE),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
