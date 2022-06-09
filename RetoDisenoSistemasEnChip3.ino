//Reto de diseño de sistemas en chip. El programa leela entrada de un keypad y la envía por medio de UART
#include <Arduino_FreeRTOS.h>
#include "queue.h"
#include "semphr.h"

//macros para la configuración y manejo de pines
#define MakeInputPin(REG, PIN)       (REG &= (~(1 << PIN)))
#define MakeOutputPin(REG, PIN)      (REG |= (1 << PIN))
#define EnablePullUp(REG, PIN)       (REG |= (1 << PIN))
#define ReadInputPin(REG, PIN)       (REG & (1 << PIN))
#define WriteOutputPinLow(REG, PIN)  (REG &= ~(1 << PIN))
#define WriteOutputPinHigh(REG, PIN) (REG |= (1 << PIN))
#define ToggleOutputPin(REG, PIN)    (REG ^= (1 << PIN))

//declaraciones de la tasa de comunicación serial
#define F_CPU 16000000UL
#define USART_BAUDRATE 19200
#define UBRR_VALUE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)


//retardo en ms
const unsigned int period = 25;


//buffer para el UART
unsigned char mybuffer[25];

//handle para un queue
QueueHandle_t uartQueue;

//global variable to store the line
int line = 0;
int *ptrLine = &line;

//semaphore handle
SemaphoreHandle_t interruptSemaphore;

void setup() 
{
  //configuración del puerto serial
  UBRR0H = (uint8_t)(UBRR_VALUE >> 8);
  UBRR0L = (uint8_t)UBRR_VALUE;
  UCSR0C = 0x06;       // Set frame format: 8data, 1stop bit 
  UCSR0B |= (1 << RXEN0) | (1 << TXEN0);   // TX y RX habilitados

  // Renglones en alta impedancia
  MakeInputPin(DDRB, PB3); WriteOutputPinHigh(PORTB, PB3); 
  MakeInputPin(DDRB, PB2); WriteOutputPinHigh(PORTB, PB2);
  MakeInputPin(DDRB, PB1); WriteOutputPinHigh(PORTB, PB1);
  MakeInputPin(DDRB, PB0); WriteOutputPinHigh(PORTB, PB0);
  
  // Columnas en pullup
  MakeInputPin(DDRD, PD7); EnablePullUp(PORTD, PD7);
  MakeInputPin(DDRD, PD6); EnablePullUp(PORTD, PD6);
  MakeInputPin(DDRD, PD5); EnablePullUp(PORTD, PD5);
  MakeInputPin(DDRD, PD4); EnablePullUp(PORTD, PD4);
  //creación de tareas
  xTaskCreate(vScanTask,"SCAN TASK",100,NULL,1,NULL);
  xTaskCreate(vHandlerTask,"HANDLER TASK",100,NULL,1,NULL);
  
  //creación del semáforo binario
  interruptSemaphore = xSemaphoreCreateBinary();
  
  //creación de las queue
  uartQueue = xQueueCreate(10, sizeof(uint8_t));
  
  //si la interrupcion es creada, inicializa interrupción PCINT23 PD7
  if(interruptSemaphore != NULL)
  {
    //se habilita interrupción por cambio de estado en PORTD
    PCICR |= (1 << PCIE2);
    //se habilita interrupción PCINT23-20
    PCMSK2 |= (1 << PCINT23);
    PCMSK2 |= (1 << PCINT22);
    PCMSK2 |= (1 << PCINT21);
    PCMSK2 |= (1 << PCINT20);
    //se habilitan las interrupciones
    sei();
  }
}

void vHandlerTask(void *pvParameters){
  char valueToSend;
  BaseType_t qStatus;
  const TickType_t xTicksToWait = pdMS_TO_TICKS(100);
  while(1){
    if (xSemaphoreTakeFromISR(interruptSemaphore, NULL) == pdPASS){
      //imprimir("Enter");
      taskENTER_CRITICAL();
      vTaskSuspendAll();
      if(*ptrLine == 1){
        if(ReadInputPin(PIND, PD7) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD7) == 0);
          valueToSend =  "1";
          imprimir("1\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD6) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD6) == 0);
          valueToSend =  "2";
          imprimir("2\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD5) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD5) == 0);
          valueToSend =  "3";
          imprimir("3\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD4) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD4) == 0);
          valueToSend =  "A";
          imprimir("A\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
      }
      else if(*ptrLine == 2){
        if(ReadInputPin(PIND, PD7) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD7) == 0);
          valueToSend =  "4";
          imprimir("4\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD6) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD6) == 0);
          valueToSend =  "5";
          imprimir("5\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD5) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD5) == 0);
          valueToSend =  "6";
          imprimir("6\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD4) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD4) == 0);
          valueToSend =  "B";
          imprimir("B\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
      }
      else if(*ptrLine == 3){
        if(ReadInputPin(PIND, PD7) == 0)
        {
        vTaskDelay(pdMS_TO_TICKS(period));
        while(ReadInputPin(PIND, PD7) == 0);
        valueToSend =  "7";
          imprimir("7\n");
        }
        if(ReadInputPin(PIND, PD6) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD6) == 0);
          valueToSend =  "8";
          imprimir("8\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD5) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD5) == 0);
          valueToSend =  "9";
          imprimir("9\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD4) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD4) == 0);
          valueToSend =  "C";
          imprimir("C\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
      }
      else if(*ptrLine == 4){
        if(ReadInputPin(PIND, PD7) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD7) == 0);
          valueToSend =  "*";
          imprimir("*\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD6) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD6) == 0);
          valueToSend =  "0";
          imprimir("0\n");
        }
        if(ReadInputPin(PIND, PD5) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD5) == 0);
          valueToSend =  "#";
          imprimir("#\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
        if(ReadInputPin(PIND, PD4) == 0)
        {
          vTaskDelay(pdMS_TO_TICKS(period));
          while(ReadInputPin(PIND, PD4) == 0);
          valueToSend =  "D";
          imprimir("D\n");
          vTaskDelay(pdMS_TO_TICKS(period));
        }
      }
      xTaskResumeAll();
      taskEXIT_CRITICAL();
    }
  }
  vTaskDelay(pdMS_TO_TICKS(10));
}


//Funcion reentrante para imprimir a UART
void imprimir(unsigned char msg[25])
{
  //entrando a la sección critica
  vTaskSuspendAll();  
  sprintf(mybuffer, msg);
  USART_Transmit_String((unsigned char *)mybuffer);
  vTaskDelay(pdMS_TO_TICKS(25)); 
  //saliendo de la sección critica
  xTaskResumeAll();
}

void vScanTask(void *pvParameters)
{
  int32_t valueToSend;
  BaseType_t qStatus;
  const TickType_t xTicksToWait = pdMS_TO_TICKS(100);
  // Barrido de renglones
  //renglón 1
  MakeOutputPin(DDRB, PB3); 
  WriteOutputPinLow(PORTB, PB3);
  *ptrLine = 1; 
  vTaskDelay(pdMS_TO_TICKS(25));
  // Regresa el renglón a alta impedancia
  WriteOutputPinHigh(PORTB, PB3); 
  MakeInputPin(DDRB, PB3); 
  //renglón 2
  MakeOutputPin(DDRB, PB2); 
  WriteOutputPinLow(PORTB, PB2);
  *ptrLine = 2;
  vTaskDelay(pdMS_TO_TICKS(25));
  // Regresa el renglón a alta impedancia
  WriteOutputPinHigh(PORTB, PB2); 
  MakeInputPin(DDRB, PB2); 
  //renglón 3
  MakeOutputPin(DDRB, PB1); 
  WriteOutputPinLow(PORTB, PB1);
  *ptrLine = 3;
  vTaskDelay(pdMS_TO_TICKS(25));
  // Regresa el renglón a alta impedancia
  WriteOutputPinHigh(PORTB, PB1); 
  MakeInputPin(DDRB, PB1); 
  //renglón 4
  MakeOutputPin(DDRB, PB0); 
  WriteOutputPinLow(PORTB, PB0);
  *ptrLine = 4;
  vTaskDelay(pdMS_TO_TICKS(25));
  // Regresa el renglón a alta impedancia
  WriteOutputPinHigh(PORTB, PB0); 
  MakeInputPin(DDRB, PB0); 
  vTaskDelay(10/portTICK_PERIOD_MS);  
}

ISR(PCINT2_vect){  
  //da el semáforo desde ISR
  xSemaphoreGiveFromISR(interruptSemaphore, NULL);
}

void loop() 
{

  //modo power down
  SMCR |= (1<<SM1); 
  //desactiva interrupciones
  cli(); 
  //habilita sleep           
  SMCR |= (1<<SE);
  //habilita interrupciones  
  sei();
  //aplica sleep
  asm("SLEEP");
  //deshabilita sleep
  SMCR &= ~(1<<SE); 
}


//////////funciones de transmisión del UART///////////////

void USART_Transmit(unsigned char data)
{
  //wait for empty transmit buffer
  while(!(UCSR0A & (1 << UDRE0)));
  
  //put data into buffer, send data
  UDR0 = data;  
}

void USART_Transmit_String(unsigned char * pdata)
{
  unsigned char i;
  //calculate string length
  unsigned char len = strlen(pdata);

  //transmit byte for byte
  for(i=0; i < len; i++)
  {
    //wait for empty transmit buffer
    while(!(UCSR0A & (1 << UDRE0)));
    //put data into buffer, send data
    UDR0 = pdata[i];
  }
}
//////////////////////////////////////////////////////////////
