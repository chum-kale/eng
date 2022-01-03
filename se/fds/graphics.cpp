#include <graphics>
 
int main( )
{
    initwindow(800, 800, "First Sample");
    
    setcolor(WHITE);
    setfillstyle(SOLID_FILL ,WHITE);
    
    rectangle(0,0,800,800);
	floodfill(10,10, WHITE);
	
	
    setcolor(BLACK);
    
    setfillstyle(SOLID_FILL ,14);
    line(355,150,473,65);
    line(355,150,400,12);
    line(445,150,400,12);
    line(327,65,473,65);
    line(327,65,445,150);
    
    floodfill(400,14, 0);
    floodfill(400,67, 0);
    floodfill(360,67, 0);
    floodfill(465,67, 0);
    floodfill(440,145, 0);
    floodfill(360,145, 0);
    
    
    setfillstyle(SOLID_FILL ,2);
    
    line(435,470,435,550);
    line(365,470,365,550);
    
    ellipse(495,140,185,260,60,85);
    ellipse(305,140,280,355,60,85);
    
    ellipse(300,233,20,40,30,20);
    ellipse(350,214,200,340,30,20);
    ellipse(400,233,20,160,30,20);
    ellipse(450,214,200,340,30,20);
    ellipse(500,233,140,160,30,20);
   
    
    ellipse(540,220,180,260,60,85);
    ellipse(260,220,280,360,60,85);
    
    ellipse(300,289,200,340,30,20);
    ellipse(350,308,20,160,30,20);
    ellipse(400,289,200,340,30,20);
    ellipse(450,308,20,160,30,20);
    ellipse(500,289,200,340,30,20);
    
    
    
    ellipse(580,300,180,260,60,85);
    ellipse(220,300,280,360,60,85);
    
    
    ellipse(270,398,20,160,40,30);
    ellipse(335,366,200,340,40,30);
    ellipse(400,398,20,160,40,30);
    ellipse(465,366,200,340,40,30);
    ellipse(530,398,20,160,40,30);
    
    //////
    
    ellipse(615,380,175,260,60,85);
    ellipse(185,380,280,360,60,85);
    ellipse(185,380,0,5,60,85);
  
  
  
    ellipse(240,440,205,330,50,40);
    ellipse(320,487,30,150,50,40);
    ellipse(400,440,210,330,50,40);
    ellipse(480,487,30,150,50,40);
    ellipse(560,440,210,335,50,40);
    
    
    
    
    floodfill(400,160, 0);
    floodfill(400,230, 0);
    floodfill(400,320, 0);
    floodfill(400,410, 0);
    
    
    line(450,260,450,230);
    circle(450,270,10);
    
    
    line(340,250,340,230);
    circle(340,260,10);
    
    
    line(350,330,350,285);
    circle(350,340,10);
    
    line(490,345,490,305);
    circle(490,355,10);
    
    
    
    line(260,408,260,368);
    circle(260,418,10);
    
    line(400,420,400,368);
    circle(400,430,10);
    
    line(530,408,530,370);
    circle(530,418,10);
    
    
    
    line(280,497,280,460);
    circle(280,507,10);
    
    line(520,497,520,460);
    circle(520,507,10);
    
    setfillstyle(SOLID_FILL ,0);
    circle(280,507,3);
    circle(520,507,3);
    circle(530,418,3);
    circle(400,430,3);
    circle(260,418,3);
    circle(490,355,3);
    circle(350,340,3);
    circle(340,260,3);
    circle(450,270,3);
    floodfill(280,507, 0);
    floodfill(520,507, 0);
    floodfill(530,418, 0);
    floodfill(400,430,0);
    floodfill(260,418,0);
    floodfill(490,355,0);
    floodfill(350,340, 0);
    floodfill(340,260, 0);
    floodfill(450,270, 0);
    
 	setfillstyle(SOLID_FILL ,6);
    floodfill(280,502,0);
    setfillstyle(SOLID_FILL ,3);
    floodfill(400,425,0);
    floodfill(340,255,0);
    
    setfillstyle(SOLID_FILL ,4);
    floodfill(260,413,0);
    floodfill(450,265,0);
    floodfill(530,413,0);
    setfillstyle(SOLID_FILL ,5);
    floodfill(520,502,0);
    setfillstyle(SOLID_FILL ,1);
    floodfill(350,335,0);
    floodfill(490,350,0);   
    
    
    
    
    
    setfillstyle(SOLID_FILL ,6);
    
    
    line(435,465,435,550);
    line(365,465,365,550);
    
    setcolor(0);
    setfillstyle(4,WHITE);
    rectangle(420,475,425,545);
    floodfill(422,490,WHITE);
    
    setcolor(0);
    setfillstyle(SOLID_FILL ,6);
    ellipse(360,600,30,150,70,50);
    ellipse(440,600,30,140,70,50);
    
    floodfill(400,480, 0);
    
    ellipse(400,770,50,82,350,250);
    ellipse(400,770,98,130,350,250);
    
    ellipse(750,340,230,310,350,250);
    ellipse(50,340,230,310,350,250);
    
    
    
    
    while (!kbhit( ))
    {
        delay(100);
    }
    return 0;
}