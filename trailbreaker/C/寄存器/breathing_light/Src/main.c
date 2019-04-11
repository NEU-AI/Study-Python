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
TIM_HandleTypeDef htim2;

/* USER CODE BEGIN PV */
uint16_t get_key_value;
	//              ?7  1   2   3   4   5   6   7  ?1 ?2 ?3 ?4 ?5 ???
	uint16_t tone[] = {247,262,294,330,349,392,440,294,523,587,659,698,784,1000};//?????
	//????
	uint8_t music[]={5,5,6,8,7,6,5,6,13,13,//??
                5,5,6,8,7,6,5,3,13,13,
                2,2,3,5,3,5,6,3,2,1,
                6,6,5,6,5,3,6,5,13,13,

                5,5,6,8,7,6,5,6,13,13,
                5,5,6,8,7,6,5,3,13,13,
                2,2,3,5,3,5,6,3,2,1,
                6,6,5,6,5,3,6,1,	

                13,8,9,10,10,9,8,10,9,8,6,
                13,6,8,9,9,8,6,9,8,6,5,
                13,2,3,5,5,3,5,5,6,8,7,6,
                6,10,9,9,8,6,5,6,8};	
	uint8_t time[] = {2,4,2,2,2,2,2,8,4, 4, //??
                2,4,2,2,2,2,2,8,4, 4, 
                2,4,2,4,2,2,4,2,2,8,
                2,4,2,2,2,2,2,8,4 ,4, 

                2,4,2,2,2,2,2,8,4, 4, 
                2,4,2,2,2,2,2,8,4, 4, 
                2,4,2,4,2,2,4,2,2,8,
                2,4,2,2,2,2,2,8,

                4, 2,2,2, 4, 2,2,2, 2,2,8,
                4, 2,2,2,4,2,2,2,2,2,8,
                4, 2,2,2,4,2,2,5,2,6,2,4,
                2,2 ,2,4,2,4,2,2,12};	
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM2_Init(void);
/* USER CODE BEGIN PFP */
void ImprovePwm(uint16_t time);
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
	uint16_t i;
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

  /* USER CODE BEGIN 2 */

	SET_BIT(RCC->AHB1ENR, RCC_AHB1ENR_GPIOAEN);//使能时钟
	TIM_ClockConfigTypeDef sClockSourceConfig = {0};
	TIM_MasterConfigTypeDef sMasterConfig = {0};
	TIM_OC_InitTypeDef sConfigOC = {0};

	/* USER CODE BEGIN TIM2_Init 1 */

	/* USER CODE END TIM2_Init 1 */
	htim2.Instance = TIM2;
	htim2.Init.Prescaler = 2000;
	htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
	htim2.Init.Period = 160-1;
	htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
	htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;


	/* Allocate lock resource and initialize it */
	htim2.Lock = HAL_UNLOCKED;


	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	RCC->APB1ENR|=RCC_APB1ENR_TIM2EN;
	/* TIM2 interrupt Init */
	NVIC->ISER[(((uint32_t)TIM2_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM2_IRQn) & 0x1FUL));//使能中断


	/* Set the TIM state */
	htim2.State = HAL_TIM_STATE_BUSY;

	/* Set the Time Base configuration */
	uint32_t tmpcr1;
	tmpcr1 = htim2.Instance->CR1;

	/* Set TIM Time Base Unit parameters ---------------------------------------*/

	/* Select the Counter Mode */
	tmpcr1 &= ~(TIM_CR1_DIR | TIM_CR1_CMS);
	tmpcr1 |= TIM_COUNTERMODE_UP;

	/* Set the clock division */
	tmpcr1 &= ~TIM_CR1_CKD;
	tmpcr1 |= 2000;

	/* Set the auto-reload preload */
	tmpcr1=(tmpcr1 & (~(TIM_CR1_ARPE))) | (TIM_AUTORELOAD_PRELOAD_DISABLE);
	htim2.Instance->CR1 = tmpcr1;

	/* Set the Autoreload value */
	htim2.Instance->ARR = 160-1;

	/* Set the Prescaler value */
	htim2.Instance->PSC = 2000-1;

	/* Generate an update event to reload the Prescaler
	and the repetition counter (only for advanced timer) value immediately */
	htim2.Instance->EGR = TIM_EGR_UG;

	/* Initialize the TIM state*/
	htim2.State = HAL_TIM_STATE_READY;

	/* Allocate lock resource and initialize it */
	htim2.Lock = HAL_UNLOCKED;

	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	SET_BIT(RCC->APB1ENR, RCC_APB1ENR_TIM2EN);
	/* TIM2 interrupt Init */

	NVIC->ISER[(((uint32_t)TIM2_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM2_IRQn) & 0x1FUL));
	/* Set the TIM state */
	htim2.State = HAL_TIM_STATE_BUSY;  

	uint32_t tmpsmcr;
	htim2.State = HAL_TIM_STATE_BUSY;
	/* Check the parameters */

	/* Reset the SMS, TS, ECE, ETPS and ETRF bits */
	tmpsmcr = htim2.Instance->SMCR;
	tmpsmcr &= ~(TIM_SMCR_SMS | TIM_SMCR_TS);
	tmpsmcr &= ~(TIM_SMCR_ETF | TIM_SMCR_ETPS | TIM_SMCR_ECE | TIM_SMCR_ETP);
	htim2.Instance->SMCR = tmpsmcr;
	htim2.State = HAL_TIM_STATE_READY;

	/* Set the TIM state */
	htim2.State = HAL_TIM_STATE_BUSY;

	/* Init the base time for the PWM */
	TIM_Base_SetConfig(htim2.Instance, &htim2.Init);

	/* Initialize the TIM state*/
	htim2.State = HAL_TIM_STATE_READY;



	sConfigOC.OCMode = TIM_OCMODE_PWM1;
	sConfigOC.Pulse = 500;
	sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
	sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;

	HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1);

	htim2.State = HAL_TIM_STATE_BUSY;

	/* Configure the Channel 1 in PWM mode */
	uint32_t tmpccmrx;
	uint32_t tmpccer;
	uint32_t tmpcr2;

	/* Disable the Channel 1: Reset the CC1E Bit */
	htim2.Instance->CCER &= ~TIM_CCER_CC1E;

	/* Get the TIMx CCER register value */
	tmpccer = htim2.Instance->CCER;
	/* Get the TIMx CR2 register value */
	tmpcr2 =  htim2.Instance->CR2;

	/* Get the TIMx CCMR1 register value */
	tmpccmrx = htim2.Instance->CCMR1;

	/* Reset the Output Compare Mode Bits */
	tmpccmrx &= ~TIM_CCMR1_OC1M;
	tmpccmrx &= ~TIM_CCMR1_CC1S;
	/* Select the Output Compare Mode */
	tmpccmrx |= TIM_OCMODE_PWM1;

	/* Reset the Output Polarity level */
	tmpccer &= ~TIM_CCER_CC1P;
	/* Set the Output Compare Polarity */
	tmpccer |= TIM_OCPOLARITY_HIGH;


	/* Reset the Output N Polarity level */
	tmpccer &= ~TIM_CCER_CC1NP;
	/* Set the Output N Polarity */
	tmpccer |= TIM_OCPOLARITY_HIGH;
	/* Reset the Output N State */
	tmpccer &= ~TIM_CCER_CC1NE;



	/* Reset the Output Compare and Output Compare N IDLE State */
	tmpcr2 &= ~TIM_CR2_OIS1;
	tmpcr2 &= ~TIM_CR2_OIS1N;

	/* Write to TIMx CR2 */
	htim2.Instance->CR2 = tmpcr2;

	/* Write to TIMx CCMR1 */
	htim2.Instance->CCMR1 = tmpccmrx;

	/* Set the Capture Compare Register value */
	htim2.Instance->CCR1 = 500;

	/* Write to TIMx CCER */
	htim2.Instance-> CCER = tmpccer;

	/* Set the Preload enable bit for channel1 */
	htim2.Instance->CCMR1 |= TIM_CCMR1_OC1PE;

	/* Configure the Output Fast mode */
	htim2.Instance->CCMR1 &= ~TIM_CCMR1_OC1FE;



	htim2.State = HAL_TIM_STATE_READY;



	__HAL_RCC_GPIOA_CLK_ENABLE();
	/**TIM2 GPIO Configuration    
	PA15     ------> TIM2_CH1 
	*/
	GPIO_InitTypeDef GPIO_InitStruct;
	GPIO_InitStruct.Pin = GPIO_PIN_15;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF1_TIM2;
	HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);
	
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  
  while (1)
  {

	   
 

	for(i=000;i<300;)
	{
		ImprovePwm(i);


		

		/* Enable the Capture compare channel */
		TIM_CCxChannelCmd(htim2.Instance, TIM_CHANNEL_1, TIM_CCx_ENABLE);
		uint32_t tmp;
		tmp = TIM_CCER_CC1E << (TIM_CHANNEL_1 & 0x1FU); /* 0x1FU = 31 bits max shift */
		/* Reset the CCxE Bit */
		htim2.Instance->CCER &= ~tmp;
		/* Set or reset the CCxE Bit */
		htim2.Instance->CCER |= (uint32_t)(TIM_CCx_ENABLE << (TIM_CHANNEL_1 & 0x1FU)); /* 0x1FU = 31 bits max shift */
		/* Enable the Peripheral, except in trigger mode where enable is automatically done with trigger */
		tmpsmcr = htim2.Instance->SMCR & TIM_SMCR_SMS;
		__HAL_TIM_ENABLE(&htim2);
				HAL_Delay(15);
		i+=10;

	}
	for(i=300;i>000;)
	{
		ImprovePwm(i);

		/* Enable the Capture compare channel */
		TIM_CCxChannelCmd(htim2.Instance, TIM_CHANNEL_1, TIM_CCx_ENABLE);
		uint32_t tmp;
		tmp = TIM_CCER_CC1E << (TIM_CHANNEL_1 & 0x1FU); /* 0x1FU = 31 bits max shift */
		/* Reset the CCxE Bit */
		htim2.Instance->CCER &= ~tmp;
		/* Set or reset the CCxE Bit */
		htim2.Instance->CCER |= (uint32_t)(TIM_CCx_ENABLE << (TIM_CHANNEL_1 & 0x1FU)); /* 0x1FU = 31 bits max shift */
		/* Enable the Peripheral, except in trigger mode where enable is automatically done with trigger */
		tmpsmcr = htim2.Instance->SMCR & TIM_SMCR_SMS;
		__HAL_TIM_ENABLE(&htim2);
				HAL_Delay(15);
		i-=10;

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
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 2000;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 160-1;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 500;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */
  HAL_TIM_MspPostInit(&htim2);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOA_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */
static void ImprovePwm(uint16_t time)
{
  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
//  htim2.Instance = TIM2;
//  htim2.Init.Prescaler = 2000;
//  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
//  htim2.Init.Period = 3200-1;
//  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
//  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
//  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
//  {
//    Error_Handler();
//  }
//  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
//  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
//  {
//    Error_Handler();
//  }
//  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
//  {
//    Error_Handler();
//  }
//  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
//  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
//  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
//  {
//    Error_Handler();
//  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = time-1;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */
  HAL_TIM_MspPostInit(&htim2);
}

void Sound_music(uint16_t frq)
{
	uint16_t time;
	if(frq != 1000)
	{
		time = 5000/((uint16_t)frq);
		
	}
	else
		time = 0;
	ImprovePwm(time*2);
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
