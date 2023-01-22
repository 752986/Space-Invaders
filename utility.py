from gameObject import GameObject
import projectile

def is_hit(self: GameObject, game_objects: list[GameObject]) -> bool:
	for object in game_objects:
		# check if a projectile is colliding with the object:
		if (
			type(object) is projectile.Projectile
			and object.owner is not self
			and self.rect.colliderect(object.rect)
		):
			object.should_delete = True # remove the projectile
			return True
	return False