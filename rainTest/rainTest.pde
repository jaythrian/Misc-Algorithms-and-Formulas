import processing.sound.*;
SoundFile file;

/*
* Processing.sound takes 80 msecs for
* output to load.  That is why 
* it takes a little bit for the window
* to boot up
*/


int size = 200;
rainDrop[] array = new rainDrop[size];
rainDrop drop;

void setup(){
  size(500, 500);
  file = new SoundFile(this, "data/rain.mp3");
  //file.loop();
  for (int i = 0; i < size; i++){
    array[i] = new rainDrop();
    
  }
 
  drop = new rainDrop();
}

void draw(){
  background(71,67,91);
  if (!file.isPlaying()){
    file.loop();
  }
  
  
  for (int i=0; i<size; i++){
      array[i].fall();
      array[i].update();
      //drop = new rainDrop();
      //drop.fall();
      //drop.update();
  }
  

  /*  
  drop.fall();
  drop.update();
  */
}
