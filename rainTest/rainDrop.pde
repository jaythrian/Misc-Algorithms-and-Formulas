class rainDrop{ 
  float x;
  float y;
  float yspeed;
  
  rainDrop(){
  x = random(width);
  y = random(-200, -100);
  yspeed = random(4, 10);
  }

  PShape rain = createShape(RECT, x, y,3, 5, 28);

  void fall(){
    if (y <= 500){
      y = y + yspeed;
      rain = createShape(RECT, x,y,3,5,28);
    } else{
      y = random(-200, -100);
      rain = createShape(RECT, x,y,3,5,28);
    }  
   }
  
  void update(){
    shape(rain);
  }
 }
  
