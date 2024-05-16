# Pygame Animations
## Learning Objectives
In this task, you will learn about:
- drawing images
- animating images and shapes
- basic edge detection


<br><br>

## Task Description

Demonstrate the learning objectives by writing a Pygame program that implements the following animations:

### Level 2
- Image background.
- Animate an image sprite.
- Animate a shape.

### Level 3
In addition to Level 2 requirements, add:
- Basic edge detection such that at least one animated object does not permanently move off the screen.

### Level 4
In addtion to Level 3 requirements, add:
- A sprite or shape that moves in a non-linear path, e.g. circular, wave (sinusoidal), parabolic arc, etc.

<br><br>

## Lesson Materials
Use the following references for this activity:

### Sprites and Graphics
You can find sprites and backgrounds from [Open Game Art](https://opengameart.org/).

### Using `Rect` in Pygame
It is useful to use methods and attributes of a `Rect` in your Pygame program. A `Rect` represents a rectangle and is commonly used for handling the position and dimensions of objects in Pygame, such as sprites.

Here's a brief overview of some common methods and attributes of `Rect`:

#### Attributes:

- `rect.x`: The x-coordinate of the top-left corner of the rectangle.
- `rect.y`: The y-coordinate of the top-left corner of the rectangle.
- `rect.width`: The width of the rectangle.
- `rect.height`: The height of the rectangle.
- `rect.right`: The x-coordinate value of the right edge of the rectangle.
- `rect.left`: The x-coordinate value of the left edge of the rectangle.
- `rect.top`: The y-coordinate value of the top edge of the rectangle.
- `rect.bottom`: The y-coordinate value of the bottom edge of the rectangle.
- `rect.centerx`: The x-coordinate value of the center of the rectangle.
- `rect.centery`: The y-coordinate value of the center of the rectangle.

These attributes provide flexibility and convenience when working with rectangles and sprites in Pygame. They allow for easier access to different parts of the rectangle, making it simpler to manipulate and position objects within the game world.

#### Methods:

- `rect.move(dx, dy)`: Moves the rectangle by `dx` pixels horizontally and `dy` pixels vertically.
- `rect.inflate(dw, dh)`: Increases or decreases the size of the rectangle by `dw` pixels horizontally and `dh` pixels vertically.
- `rect.colliderect(other_rect)`: Returns `True` if the rectangle collides or overlaps with `other_rect`, otherwise `False`.
- `rect.contains(point)`: Returns `True` if the `(x, y)` point is inside the rectangle, otherwise `False`.

You can read more about the Pygame `Rect` object on the [official documentation](https://www.pygame.org/docs/ref/rect.html).

<br><br>

## Template File
The template file `main.py` has already been set up for you with a 800 by 600 screen. You can modify this as necessary.

As with previous Pygame assignments, insert your code in the main loop where indicated by the comments. Make sure to indent your code properly so that it resides within the main loop.

<br><br>
## Submission
- Commit changes as you make incremental progress. Make sure to write meaningful commit messages.
- Sync or push your changes at the end of every work session or class.
- Finally, take a screenshot(s) of your finished output window showing your design(s). Upload the screenshot(s) to Classroom.
