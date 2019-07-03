#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace std;

int main( int argc, char** argv )
{
    //leitura da imagem
    string imageName("ponte.png"); 
    if( argc > 1)
    {
        imageName = argv[1];
    }
    Mat image;
    Mat hsv;
   // image = imread(imageName.c_str(), IMREAD_GRAYSCALE); 
    image = imread(imageName.c_str(), IMREAD_COLOR); 
    //cvtColor(image,image,COLOR_BGR2GRAY);
    //printf("OpenCV: %s", cv::getBuildInformation().c_str());
    if( image.empty() )                      
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }
    namedWindow( "Display window", WINDOW_AUTOSIZE ); 
    imshow( "Display window", image );               
    waitKey(0);
    return 0;
}