/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2019 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define GPIO_MODE             0x00000003U
#define EXTI_MODE             0x10000000U
#define GPIO_MODE_IT          0x00010000U
#define GPIO_MODE_EVT         0x00020000U
#define RISING_EDGE           0x00100000U
#define FALLING_EDGE          0x00200000U
#define GPIO_OUTPUT_TYPE      0x00000010U

#define GPIO_NUMBER           16U
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

uint8_t led_r[8]={LED_X7_Pin,LED_X8_Pin,LED_X6_Pin,LED_X5_Pin,LED_X4_Pin,LED_X3_Pin,LED_X1_Pin,LED_X2_Pin};//?????????,???????
//uint8_t led_c[8]={LED_Y2_Pin,LED_Y1_Pin,LED_Y3_Pin,LED_Y4_Pin,LED_Y5_Pin,LED_Y6_Pin,LED_Y8_Pin,LED_Y7_Pin};//?????????,???????
uint8_t led_code[][8] = {


{0x00,0x00,0x42,0x7E,0x42,0x00,0x00,0x00},	//×?·?I
{0x0c,0x12,0x22,0x44,0x44,0x22,0x12,0x0c},	//xin;
{0x00,0x3E,0x02,0x04,0x08,0x10,0x3E,0x00},	//×?·?N
{0x00,0x7e,0x4A,0x4A,0x4A,0x4A,0x00,0x00},	//×?·?E
{0x00,0x3E,0x40,0x40,0x40,0x40,0x3E,0x00},	//×?·?U
{0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00}	//null
};	

uint8_t i,j,l,m;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */
void move(void);
void SwCheck(void);
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void SetYOutPut(uint8_t set_value);

void SetGpioa(uint8_t gpio_temp);	
void SetGpiob(uint8_t gpio_temp);	
void SetGpioc(uint8_t gpio_temp);	


/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */
  uint8_t i;
  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
//  MX_GPIO_Init();
  /* USER CODE BEGIN 2 */
	RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;
	RCC->AHB1ENR |= RCC_AHB1ENR_GPIOBEN;
	RCC->AHB1ENR |= RCC_AHB1ENR_GPIOCEN;
	for(i=0;i<8;i++)
		SetGpioa(i);
	for(i=12;i<16;i++)
		SetGpiob(i);
	for(i=8;i<10;i++)
		SetGpiob(i);
	for(i=6;i<8;i++)
		SetGpioc(i);
			for(l=0;l<8;l++)
			{
				HAL_GPIO_WritePin(GPIOA, led_r[l], GPIO_PIN_SET);
			}
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {


		
			for(l=0;l<8;l++)
			{
			  for(j=0;j<8;j++)
			  {
				GPIOA->BSRR = (uint32_t)led_r[l] << 16U;
				HAL_GPIO_WritePin(GPIOA, led_r[l], GPIO_PIN_RESET);
				SetYOutPut(~(0x01<<j));
				HAL_Delay(100);
				GPIOA->BSRR = led_r[l];
				
			  }
			}
			for(l=0;l<8;l++)
			{

				
				GPIOA->BSRR = (uint32_t)led_r[l] << 16U;
				SetYOutPut(0);
				HAL_Delay(800);
				GPIOA->BSRR = led_r[l];

			}
			for(l=0;l<80;l++)
			{
			  for(j=0;j<8;j++)
			  {
				
				GPIOA->BSRR = (uint32_t)led_r[j] << 16U;
				SetYOutPut(0);
				HAL_Delay(1);
				GPIOA->BSRR = led_r[j];
			  }
			}
	
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage 
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOC_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOA, LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
                          |LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin, GPIO_PIN_SET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, LED_Y5_Pin|LED_Y6_Pin|LED_Y7_Pin|LED_Y8_Pin 
                          |LED_Y3_Pin|LED_Y4_Pin, GPIO_PIN_SET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOC, LED_Y1_Pin|LED_Y2_Pin, GPIO_PIN_SET);

  /*Configure GPIO pins : LED_X1_Pin LED_X2_Pin LED_X3_Pin LED_X4_Pin 
                           LED_X5_Pin LED_X6_Pin LED_X7_Pin LED_X8_Pin */
  GPIO_InitStruct.Pin = LED_X1_Pin|LED_X2_Pin|LED_X3_Pin|LED_X4_Pin 
                          |LED_X5_Pin|LED_X6_Pin|LED_X7_Pin|LED_X8_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : SW_S3_Pin SW_S4_Pin SW_S1_Pin SW_S2_Pin */
  GPIO_InitStruct.Pin = SW_S3_Pin|SW_S4_Pin|SW_S1_Pin|SW_S2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : LED_Y5_Pin LED_Y6_Pin LED_Y7_Pin LED_Y8_Pin 
                           LED_Y3_Pin LED_Y4_Pin */
  GPIO_InitStruct.Pin = LED_Y5_Pin|LED_Y6_Pin|LED_Y7_Pin|LED_Y8_Pin 
                          |LED_Y3_Pin|LED_Y4_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : LED_Y1_Pin LED_Y2_Pin */
  GPIO_InitStruct.Pin = LED_Y1_Pin|LED_Y2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

void SwCheck(void)
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


void SetYOutPut(uint8_t set_value)
{
	
	if(0x40 == (set_value&0x40))
	{

	  GPIOB->BSRR = LED_Y8_Pin;//????
		
	}
	else
	{

	  GPIOB->BSRR = (uint32_t)LED_Y8_Pin << 16U;//??μí
	}

	
	if(0x80 == (set_value&0x80))
	{
	  GPIOB->BSRR = LED_Y7_Pin;//????
	}
	else
	{
	  GPIOB->BSRR = (uint32_t)LED_Y7_Pin << 16U;//??μí
	}
	
	
	if(0x20 == (set_value&0x20))
	{
	  GPIOB->BSRR = LED_Y6_Pin;//????
	}
	else
	{
	  GPIOB->BSRR = (uint32_t)LED_Y6_Pin << 16U;//??μí
	}
	
	if(0x10 == (set_value&0x10))
	{
	  GPIOB->BSRR = LED_Y5_Pin;//????
	}
	else
	{
	  GPIOB->BSRR = (uint32_t)LED_Y5_Pin << 16U;//??μí
	}
	
	
	if(0x8 == (set_value&0x8))
	{
	  GPIOB->BSRR = LED_Y4_Pin;//????
	}
	else
	{
	  GPIOB->BSRR = (uint32_t)LED_Y4_Pin << 16U;//??μí
	}

	
	if(0x4 == (set_value&0x4))
	{
	  GPIOB->BSRR = LED_Y3_Pin;//????
	}
	else
	{
	  GPIOB->BSRR = (uint32_t)LED_Y3_Pin << 16U;//??μí
	}
	
	
	if(0x1 == (set_value&0x01))
	{
	  GPIOC->BSRR = LED_Y2_Pin;//????
	}
	else
	{
	  GPIOC->BSRR = (uint32_t)LED_Y2_Pin << 16U;//??μí
	}
	
	if(0x2 == (set_value&0x2))
	{
	  GPIOC->BSRR = LED_Y1_Pin;//????
	}
	else
	{
	  GPIOC->BSRR = (uint32_t)LED_Y1_Pin << 16U;//??μí
	}	

}

void line(uint8_t row,uint8_t colDisp)
{
  	HAL_GPIO_WritePin(GPIOA, led_r[8-row] , GPIO_PIN_RESET); //打开某行
	SetYOutPut(colDisp);
	HAL_Delay(1);
	HAL_GPIO_WritePin(GPIOA, led_r[8-row] , GPIO_PIN_SET); //打开某行
}



void SetGpioa(uint8_t gpio_temp)
{

	uint32_t temp = 0x00U;
	/*--------------------- GPIO Mode Configuration ------------------------*/

	/* Configure IO Direction mode (Input, Output, Alternate or Analog) */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOA->MODER;
	temp &= ~(GPIO_MODER_MODER0 << (gpio_temp * 2U));
	temp |= ((GPIO_MODE_OUTPUT_PP & GPIO_MODE) << (gpio_temp * 2U));//éè??PIN4í?íìê?3?
	GPIOA->MODER = temp;

	/* In case of Output or Alternate function mode selection */
	/* Configure the IO Speed */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOA->OSPEEDR; 
	temp &= ~(GPIO_OSPEEDER_OSPEEDR0 << (gpio_temp * 2U));
	temp |= (GPIO_SPEED_FREQ_LOW << (gpio_temp * 2U));//éè??PIN4μí?ù?êê?3?
	GPIOA->OSPEEDR = temp;

	/* Configure the IO Output Type */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOA->OTYPER;
	temp &= ~(GPIO_OTYPER_OT_0 << gpio_temp) ;
	temp |= (((GPIO_MODE_OUTPUT_PP & GPIO_OUTPUT_TYPE) >> 4U) << gpio_temp);//éè??PIN4ê?3??￡ê?
	GPIOA->OTYPER = temp;


	/* Activate the Pull-up or Pull down resistor for the current IO */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOA->PUPDR;
	temp &= ~(GPIO_PUPDR_PUPDR0 << (gpio_temp * 2U));
	
	temp |= ((GPIO_NOPULL) << (gpio_temp * 2U));//éè??PIN4?Té?à-?￡ê?
	GPIOA->PUPDR = temp;

}
void SetGpiob(uint8_t gpio_temp)
{

	uint32_t temp = 0x00U;
	/*--------------------- GPIO Mode Configuration ------------------------*/

	/* Configure IO Direction mode (Input, Output, Alternate or Analog) */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOB->MODER;
	temp &= ~(GPIO_MODER_MODER0 << (gpio_temp * 2U));
	temp |= ((GPIO_MODE_OUTPUT_PP & GPIO_MODE) << (gpio_temp * 2U));//éè??PIN4í?íìê?3?
	GPIOB->MODER = temp;

	/* In case of Output or Alternate function mode selection */
	/* Configure the IO Speed */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOB->OSPEEDR; 
	temp &= ~(GPIO_OSPEEDER_OSPEEDR0 << (gpio_temp * 2U));
	temp |= (GPIO_SPEED_FREQ_LOW << (gpio_temp * 2U));//éè??PIN4μí?ù?êê?3?
	GPIOB->OSPEEDR = temp;

	/* Configure the IO Output Type */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOB->OTYPER;
	temp &= ~(GPIO_OTYPER_OT_0 << gpio_temp) ;
	temp |= (((GPIO_MODE_OUTPUT_PP & GPIO_OUTPUT_TYPE) >> 4U) << gpio_temp);//éè??PIN4ê?3??￡ê?
	GPIOB->OTYPER = temp;


	/* Activate the Pull-up or Pull down resistor for the current IO */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOB->PUPDR;
	temp &= ~(GPIO_PUPDR_PUPDR0 << (gpio_temp * 2U));
	
	temp |= ((GPIO_NOPULL) << (gpio_temp * 2U));//éè??PIN4?Té?à-?￡ê?
	GPIOB->PUPDR = temp;

}
void SetGpioc(uint8_t gpio_temp)
{

	uint32_t temp = 0x00U;
	/*--------------------- GPIO Mode Configuration ------------------------*/

	/* Configure IO Direction mode (Input, Output, Alternate or Analog) */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOC->MODER;
	temp &= ~(GPIO_MODER_MODER0 << (gpio_temp * 2U));
	temp |= ((GPIO_MODE_OUTPUT_PP & GPIO_MODE) << (gpio_temp * 2U));//éè??PIN4í?íìê?3?
	GPIOC->MODER = temp;

	/* In case of Output or Alternate function mode selection */
	/* Configure the IO Speed */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOC->OSPEEDR; 
	temp &= ~(GPIO_OSPEEDER_OSPEEDR0 << (gpio_temp * 2U));
	temp |= (GPIO_SPEED_FREQ_LOW << (gpio_temp * 2U));//éè??PIN4μí?ù?êê?3?
	GPIOC->OSPEEDR = temp;

	/* Configure the IO Output Type */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOC->OTYPER;
	temp &= ~(GPIO_OTYPER_OT_0 << gpio_temp) ;
	temp |= (((GPIO_MODE_OUTPUT_PP & GPIO_OUTPUT_TYPE) >> 4U) << gpio_temp);//éè??PIN4ê?3??￡ê?
	GPIOC->OTYPER = temp;


	/* Activate the Pull-up or Pull down resistor for the current IO */
	/*********±￡′???′??÷3?ê?????*********************/
	temp = GPIOC->PUPDR;
	temp &= ~(GPIO_PUPDR_PUPDR0 << (gpio_temp * 2U));
	
	temp |= ((GPIO_NOPULL) << (gpio_temp * 2U));//éè??PIN4?Té?à-?￡ê?
	GPIOC->PUPDR = temp;

}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{ 
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
