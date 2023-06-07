float x = 0;
float y = 0;
PShape Point;
ArrayList<PShape> pointList = new ArrayList<PShape>(); 

/*
* Program displays a Sin wave
*/

void setup(){
  size(400,400);

}

void sinWave(){
  for (float i = 0; i < 400; i= i+.1){
   Point = createShape(POINT, x, y);
   x = i;
   y = 25 * sin(x);
   pointList.add(Point);
}
}

void draw(){
  background(255,255,255);
  strokeCap(ROUND);
  stroke(0, 0, 0);
  fill(0);
  strokeWeight(2);
  sinWave();
  
  /*
  
  Play with numbers underneath here
  to get different results in code
  
  */
  //draws the points 
  x = 0;
  for (PShape i : pointList){
    shape(i, x, 400/2);
    x += 1;
    
  } 
}
