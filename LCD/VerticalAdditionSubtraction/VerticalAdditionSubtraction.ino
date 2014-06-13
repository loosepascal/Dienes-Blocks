
#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9340.h"

#if defined(__SAM3X8E__)
    #undef __FlashStringHelper::F(string_literal)
    #define F(string_literal) string_literal
#endif

// These are the pins used for the UNO
// for Due/Mega/Leonardo use the hardware SPI pins (which are different)
#define _sclk 13
#define _miso 12
#define _mosi 11
#define _cs 10
#define _dc 9
#define _rst 8

// Using software SPI is really not suggested, its incredibly slow
//Adafruit_ILI9340 tft = Adafruit_ILI9340(_cs, _dc, _mosi, _sclk, _rst, _miso);
// Use hardware SPI
Adafruit_ILI9340 tft = Adafruit_ILI9340(_cs, _dc, _rst);

void setup() {
  Serial.begin(9600);
  while (!Serial);
  
  Serial.println("Adafruit 2.2\" SPI TFT Test!"); 
 
  tft.begin();

 
}

void loop(void) {
uint8_t rotation=3;
tft.setRotation(rotation);
numberText();
delay(2000);
}

unsigned long numberText() {
  tft.fillScreen(ILI9340_BLACK);
  unsigned long start = micros();
  tft.setCursor(0, 0);
//x,y x is topleft to top right, y is top left to bottom left 
 
  tft.setTextColor(ILI9340_GREEN);
  tft.setTextSize(9); //SIZE n makes a char n(6*8) pixels where n*8 is the height and n*6 is the width. 5 is 30*40 pixels, 6 is 
  tft.println("1 2 3");
   tft.setCursor(0, 72);
   tft.println("4 5 6");

  return micros() - start;
}
/*code from Adafruit_GFX

#include "Adafruit_GFX.h"
#include "glcdfont.c"
#ifdef __AVR__
 #include <avr/pgmspace.h>
#else
 #define pgm_read_byte(addr) (*(const unsigned char *)(addr))
#endif

// Draw a character
void Adafruit_GFX::drawChar(int16_t x, int16_t y, unsigned char c,
			    uint16_t color, uint16_t bg, uint8_t size) {

  if((x >= _width)            || // Clip right
     (y >= _height)           || // Clip bottom
     ((x + 6 * size - 1) < 0) || // Clip left
     ((y + 8 * size - 1) < 0))   // Clip top
    return;

  for (int8_t i=0; i<6; i++ ) {
    uint8_t line;
    if (i == 5) 
      line = 0x0;
    else 
      line = pgm_read_byte(font+(c*5)+i); _____________________ font is in glcdfont.c (a massive array font[] of HEX shit) , c is the char (in HEX from ASCII table?)
    for (int8_t j = 0; j<8; j++) {
      if (line & 0x1) {
        if (size == 1) // default size
          drawPixel(x+i, y+j, color);
        else {  // big size
          fillRect(x+(i*size), y+(j*size), size, size, color);
        } 
      } else if (bg != color) {
        if (size == 1) // default size
          drawPixel(x+i, y+j, bg);
        else {  // big size
          fillRect(x+i*size, y+j*size, size, size, bg);
        }
      }
      line >>= 1;
    }
  }
}
*/
