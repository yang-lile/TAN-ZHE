# Sprite is a moudle of python.

#### Now, let us learn it.

>## python.sprite.Sprite

```python
class Arbol(pygame.sprite.Sprite):
  def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load('Arboles2.png').convert_alpha()
```

by the code from *github*, we know that `pygame.sprite.Sprite` is a class of python. So we can use it by *`__init__()`*. such as:

```python
spriteA = python.sprite.Sprite()
```

But it is not enough to me. I always use an other class inherit it to complete something difficult.

>## python.sprite.Group

Group is a home for sprite, without it, they will go die.

So when we have a sprite, we should set it in a group.

like this:

```python
spriteA = python.sprite.Sprite()
groupHanpi = python.sprite.Group()
# add it by pygame.sprite.Group.add(xxx)
groupHanpi.add(spriteA)
```

# It is time to read code!

# please open [sprite1.py](sprite1.py)

Oh! you can learn a new grammer is how to add a link.

```markdown
[name](url)
```
