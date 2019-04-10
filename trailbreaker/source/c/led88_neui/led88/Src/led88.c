#include "led88.h"
#include "main.h"
uint8_t i,j,l,m;

void SwCheck(uint8_t *led_r,uint8_t led_code[][8])
{
	if( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S1_Pin))
	{
		HAL_Delay(10);
		while( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S1_Pin))
		{
		  
		  for (l=0;l<50;l++)
		  {
			
			for(j=0;j<8;j++)
			{
			  HAL_GPIO_WritePin(GPIOA, LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
								|LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin, GPIO_PIN_SET);
			  HAL_GPIO_WritePin(GPIOA, led_r[j], GPIO_PIN_RESET);
			  SetYOutPut(~led_code[2][j]);
			  HAL_Delay(1);
			}
		  }
		
		}
		return;
	}
	
	if( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S2_Pin))
	{
		HAL_Delay(10);
		while( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S2_Pin))
		{
		  
		  for (l=0;l<50;l++)
		  {
			
			for(j=0;j<8;j++)
			{
			  HAL_GPIO_WritePin(GPIOA, LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
								|LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin, GPIO_PIN_SET);
			  HAL_GPIO_WritePin(GPIOA, led_r[j], GPIO_PIN_RESET);
			  SetYOutPut(~led_code[3][j]);
			  HAL_Delay(1);
			}
		  }
		
		}
		return;
	}	
	
	if( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S4_Pin))
	{
		HAL_Delay(10);
		while( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S4_Pin))
		{
		  
		  for (l=0;l<50;l++)
		  {
			
			for(j=0;j<8;j++)
			{
			  HAL_GPIO_WritePin(GPIOA, LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
								|LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin, GPIO_PIN_SET);
			  HAL_GPIO_WritePin(GPIOA, led_r[j], GPIO_PIN_RESET);
			  SetYOutPut(~led_code[1][j]);
			  HAL_Delay(1);
			}
		  }
		
		}
		return;
	}	
	
	if( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S3_Pin))
	{
		HAL_Delay(10);
		while( GPIO_PIN_RESET == HAL_GPIO_ReadPin(GPIOB, SW_S3_Pin))
		{
		  
		  for (l=0;l<50;l++)
		  {
			
			for(j=0;j<8;j++)
			{
			  HAL_GPIO_WritePin(GPIOA, LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
								|LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin, GPIO_PIN_SET);
			  HAL_GPIO_WritePin(GPIOA, led_r[j], GPIO_PIN_RESET);
			  SetYOutPut(~led_code[0][j]);
			  HAL_Delay(1);
			}
		  }
		
		}
		return;
	}

}

void line(uint8_t row,uint8_t colDisp,uint8_t *led_r)
{
  	HAL_GPIO_WritePin(GPIOA, led_r[8-row] , GPIO_PIN_RESET); //打开某行
	SetYOutPut(colDisp);
	HAL_Delay(1);
	HAL_GPIO_WritePin(GPIOA, led_r[8-row] , GPIO_PIN_SET); //打开某行
}



void SetYOutPut(uint8_t set_value)
{
	
	if(0x40 == (set_value&0x40))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y8_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y8_Pin , GPIO_PIN_RESET);
	}

	
	if(0x80 == (set_value&0x80))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y7_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y7_Pin , GPIO_PIN_RESET);
	}
	
	
	if(0x20 == (set_value&0x20))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y6_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y6_Pin , GPIO_PIN_RESET);
	}
	
	if(0x10 == (set_value&0x10))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y5_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y5_Pin , GPIO_PIN_RESET);
	}
	
	
	if(0x8 == (set_value&0x8))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y4_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y4_Pin , GPIO_PIN_RESET);
	}

	
	if(0x4 == (set_value&0x4))
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y3_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOB, LED_Y3_Pin , GPIO_PIN_RESET);
	}
	
	
	if(0x1 == (set_value&0x01))
	{
	  HAL_GPIO_WritePin(GPIOC, LED_Y2_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOC, LED_Y2_Pin , GPIO_PIN_RESET);
	}
	
	if(0x2 == (set_value&0x2))
	{
	  HAL_GPIO_WritePin(GPIOC, LED_Y1_Pin , GPIO_PIN_SET);
	}
	else
	{
	  HAL_GPIO_WritePin(GPIOC, LED_Y1_Pin , GPIO_PIN_RESET);
	}	

}
