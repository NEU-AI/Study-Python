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
#include "led88.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

uint8_t led_r[8]={LED_X7_Pin,LED_X8_Pin,LED_X6_Pin,LED_X5_Pin,LED_X4_Pin,LED_X3_Pin,LED_X1_Pin,LED_X2_Pin};//?????????,???????
//uint8_t led_c[8]={LED_Y2_Pin,LED_Y1_Pin,LED_Y3_Pin,LED_Y4_Pin,LED_Y5_Pin,LED_Y6_Pin,LED_Y8_Pin,LED_Y7_Pin};//?????????,???????
uint8_t led_code[][8] = {

{0x00,0x3E,0x10,0x08,0x04,0x02,0x3E,0x00},	//×?·?N
{0x00,0x00,0x4A,0x4A,0x4A,0x4A,0x7E,0x00},	//×?·?E
{0x00,0x3E,0x40,0x40,0x40,0x40,0x3E,0x00},	//×?·?U
{0x00,0x00,0x42,0x7E,0x42,0x00,0x00,0x00},	//×?·?I
{0x0c,0x12,0x22,0x44,0x44,0x22,0x12,0x0c},	//xin;
{0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00}	//null
};

uint8_t i,j,l,m;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */
void move(void);
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
	
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */
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
  MX_GPIO_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

		  for (l=0;l<10;l++)
		  {
			SwCheck(led_r,led_code);
			for(j=0;j<8;j++)
			{

			  HAL_GPIO_WritePin(GPIOA, led_r[8-j], GPIO_PIN_RESET);//低
			  SetYOutPut(~(*(*(led_code+0)+j+m)));
			  HAL_Delay(1);
			  HAL_GPIO_WritePin(GPIOA, led_r[8-j], GPIO_PIN_SET);
			}
		  }
		  if(m>31) 
		  {
			m=0;
		  }
		  else m++;

	
	
	
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


void move(void)
{
	uint8_t i,j,l;
	
//	for(i=0;i<8;i++)
//	{
		for(j=0;j<8;j++)
		{
			line(i,led_code[0][j],led_r);
		}
//	}
			//一个循环后，某行的所有的点向左移动一位
		//8个循环后，一个字母的所有点向左一位
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