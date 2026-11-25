
class BaseBehavior:
    def update(self, enemy):
        raise NotImplementedError(
            "O comportamento precisa implementar o método update()."
        )
