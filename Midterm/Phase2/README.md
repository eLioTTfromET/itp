# Phase 2

Okay okay, this is getting a little more complicated lol.

It wasn't too hard; it's just learning how to apply these concepts I easily understand on paper to code. I started by just copying and pasting the code that you created for the 8th notes. It was quite easy to understand. The rectangles were made with rect, the ellipses with ellipse. The color was made with fill, and the dimensions were quite easy to understand when I was changing up the values. I didn't even need to read the description you put on the .md file, but I read it anyways in case I missed anything.

I started moving around values for the first rectangle. I moved it over to the left and higher a little more. I then made the ellipse the right dimension for a circle and moved it over to the top left corner. It took some adjusting to get the placement right so that the ellipse would cover the rectangle right. Once I got the right placement of the first rectangle and circle, I looked into changing the colors of everything. I wanted the background to be black, the circles to be white and the rectangles to be gray. I looked up on Google how to make the background black. It was easier than I thought; literally just "background(0)". I tried doing "fill(0)" in the setup section at first, but it wasn't working. With the black background, I was then trying to figure out how to make the circles white while making the rectangles gray. I first tried to create another "draw()" function, but this just got rid of anytihng that was in the first draw function. So then I put another "fill()" function after the rectangles and before the circles, and this worked. I easily realized that black to white was 0 to 255. DUH! So I made the white circles 255 and made the gray rectangles 127.

The next part was getting more rectangles and more circles and putting them in the right place. I first got all the rectangles too long and the circles too far apart. The inner box was too big. So I kept making adjustments, making everything closer until the box on the inside looked like the size of a square that would fit inside the circle, like the drawing. This whole process took me about half an hour, and writing this .md file took me another half hour. Time to move onto phase 3...

Eliott