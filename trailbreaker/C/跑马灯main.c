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

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
uint8_t i = 0;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

void OpenRLed(void);
void CloseRLed(void);
void OpenGLed(void);
void CloseGLed(void);
void OpenYLed(void);
void CloseYLed(void);
void OpenBLed(void);
void CloseBLed(void);

void OpenRPad(void);
void CloseRPad(void);
void OpenGPad(void);
void CloseGPad(void);
void OpenYPad(void);
void CloseYPad(void);
void OpenBPad(void);
void CloseBPad(void);


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
	  
  
	
	if(0 == i)
	{		
		OpenRLed();
		OpenRPad();
		HAL_Delay(250);
		CloseRLed();
		OpenRPad();
		HAL_Delay(250);

		OpenGLed();
		OpenGPad();
		HAL_Delay(250);
		CloseGLed();
		CloseGPad();
		HAL_Delay(250);  


		OpenYLed();
		OpenYPad();
		HAL_Delay(250);
		CloseYLed();
		CloseYPad();
		HAL_Delay(250);

		OpenBLed();
		OpenBPad();
		HAL_Delay(250);
		CloseBLed();
		CloseBPad();
		HAL_Delay(250);
		
		
		
	}
	else
	{

		OpenBLed();
		OpenBPad();
		HAL_Delay(250);
		CloseBLed();
		CloseBPad();
		HAL_Delay(250);
		
		OpenYLed();
		OpenYPad();
		HAL_Delay(250);
		CloseYLed();
		CloseYPad();
		HAL_Delay(250);
		
		OpenGLed();
		OpenGPad();
		HAL_Delay(250);
		CloseGLed();
		CloseGPad();
		HAL_Delay(250);  
		
		OpenRLed();
		OpenRPad();
		HAL_Delay(250);
		CloseRLed();
		CloseRPad();
		HAL_Delay(250);

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
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, LED_G_Pin|LED_Y_Pin|LED_B_Pin|PAD_B_Pin 
                          |LED_R_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(PAD_Y_GPIO_Port, PAD_Y_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pins : LED_G_Pin LED_Y_Pin LED_B_Pin PAD_B_Pin 
                           LED_R_Pin */
  GPIO_InitStruct.Pin = LED_G_Pin|LED_Y_Pin|LED_B_Pin|PAD_B_Pin 
                          |LED_R_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pin : PAD_Y_Pin */
  GPIO_InitStruct.Pin = PAD_Y_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(PAD_Y_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : PB3 */
  GPIO_InitStruct.Pin = GPIO_PIN_3;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_FALLING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /* EXTI interrupt init*/
  HAL_NVIC_SetPriority(EXTI3_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(EXTI3_IRQn);

}

/* USER CODE BEGIN 4 */
void OpenRLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_R_Pin, GPIO_PIN_SET);
}
void CloseRLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_R_Pin, GPIO_PIN_RESET);
}
void OpenGLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_G_Pin, GPIO_PIN_SET);
}
void CloseGLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_G_Pin, GPIO_PIN_RESET);
}
void OpenYLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_Y_Pin, GPIO_PIN_SET);
}
void CloseYLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_Y_Pin, GPIO_PIN_RESET);
}
void OpenBLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_B_Pin, GPIO_PIN_SET);
}
void CloseBLed(void)
{
	HAL_GPIO_WritePin(GPIOB, LED_B_Pin, GPIO_PIN_RESET);
}


void OpenRPad(void)
{
//	HAL_GPIO_WritePin(GPIOA, PAD_R_Pin, GPIO_PIN_SET);
}
void CloseRPad(void)
{
//	HAL_GPIO_WritePin(GPIOA, PAD_R_Pin, GPIO_PIN_SET);
}
void OpenGPad(void)
{
//	HAL_GPIO_WritePin(GPIOA, PAD_G_Pin, GPIO_PIN_SET);
}
void CloseGPad(void)
{
//	HAL_GPIO_WritePin(GPIOA, PAD_G_Pin, GPIO_PIN_RESET);
}
void OpenYPad(void)
{
	HAL_GPIO_WritePin(GPIOA, PAD_Y_Pin, GPIO_PIN_SET);
}
void CloseYPad(void)
{
	HAL_GPIO_WritePin(GPIOA, PAD_Y_Pin, GPIO_PIN_RESET);
}
void OpenBPad(void)
{
	HAL_GPIO_WritePin(GPIOB, PAD_B_Pin, GPIO_PIN_SET);
}
void CloseBPad(void)
{
	HAL_GPIO_WritePin(GPIOB, PAD_B_Pin, GPIO_PIN_RESET);
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
