float x = 0;
float y = 0;
PShape Point;
ArrayList<PShape> pointList = new ArrayList<PShape>(); 

/*
* A fork of sinwave.pde which produces an 
* interesting graphical result
*/

void setup(){
  size(400,400);

}

void sinWave(){
  for (float i = 0; i < 400; i++){
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
  
  for (int n = 1; n < 400; n++){
  //draws the points 
  x = 0;
  for (PShape i : pointList){
    shape(i, x, 400/2 + n);
    x += 1;
    
  }
  } 
  
    for (int n = 1; n < 400; n++){
  //draws the points 
  x = 0;
  for (PShape i : pointList){
    shape(i, x, 400/2.5 - n);
    x += 1;
    
  }
  } 

  
}
