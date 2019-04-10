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
TIM_HandleTypeDef htim3;
TIM_HandleTypeDef htim4;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_TIM3_Init(void);
static void MX_TIM4_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void ImprovePwm(TIM_HandleTypeDef *htim,uint32_t chanel,uint16_t pulse_value);
void tim4chanel3cfg(void);
void tim3chanel1cfg(void);
void tim3chanel1cfg(void);

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

  MX_TIM3_Init();

  /* USER CODE BEGIN 2 */
	SET_BIT(RCC->AHB1ENR, RCC_AHB1ENR_GPIOAEN);//使能时钟
	SET_BIT(RCC->AHB1ENR, RCC_AHB1ENR_GPIOBEN);//使能时钟
	SET_BIT(RCC->AHB1ENR, RCC_AHB1ENR_GPIOCEN);//使能时钟

	tim4chanel3cfg();
	tim3chanel1cfg();
	tim3chanel1cfg();
uint32_t tmp,tmpsmcr;
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
		for(i=0;i<300;i++)
		{
			ImprovePwm(&htim3,TIM_CHANNEL_1,i);
		
		tmp = TIM_CCER_CC1E << (TIM_CHANNEL_1 & 0x1FU); /* 0x1FU = 31 bits max shift */
		/* Reset the CCxE Bit */
		htim3.Instance->CCER &= ~tmp;
		/* Set or reset the CCxE Bit */
		htim3.Instance->CCER |= (uint32_t)(TIM_CCx_ENABLE << (TIM_CHANNEL_1 & 0x1FU)); /* 0x1FU = 31 bits max shift */
		/* Enable the Peripheral, except in trigger mode where enable is automatically done with trigger */
		tmpsmcr = htim3.Instance->SMCR & TIM_SMCR_SMS;
		__HAL_TIM_ENABLE(&htim3);
			i += 10;
			HAL_Delay(20);
		}
		for(i=0;i<300;i++)
		{
			ImprovePwm(&htim4,TIM_CHANNEL_3,i);
					tmp = TIM_CCER_CC1E << (TIM_CHANNEL_3 & 0x1FU); /* 0x1FU = 31 bits max shift */
		/* Reset the CCxE Bit */
		htim4.Instance->CCER &= ~tmp;
		/* Set or reset the CCxE Bit */
		htim4.Instance->CCER |= (uint32_t)(TIM_CCx_ENABLE << (TIM_CHANNEL_3 & 0x1FU)); /* 0x1FU = 31 bits max shift */
		/* Enable the Peripheral, except in trigger mode where enable is automatically done with trigger */
		tmpsmcr = htim4.Instance->SMCR & TIM_SMCR_SMS;
		__HAL_TIM_ENABLE(&htim4);
			i += 10;
			HAL_Delay(20);
		}	  

		for(i=0;i<300;i++)
		{
			ImprovePwm(&htim3,TIM_CHANNEL_2,i);
			tmp = TIM_CCER_CC1E << (TIM_CHANNEL_1 & 0x1FU); /* 0x1FU = 31 bits max shift */
			/* Reset the CCxE Bit */
			htim3.Instance->CCER &= ~tmp;
			/* Set or reset the CCxE Bit */
			htim3.Instance->CCER |= (uint32_t)(TIM_CCx_ENABLE << (TIM_CHANNEL_2 & 0x1FU)); /* 0x1FU = 31 bits max shift */
			/* Enable the Peripheral, except in trigger mode where enable is automatically done with trigger */
			tmpsmcr = htim3.Instance->SMCR & TIM_SMCR_SMS;
			__HAL_TIM_ENABLE(&htim3);
			i += 10;
			HAL_Delay(20);
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
  * @brief TIM3 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM3_Init(void)
{

  /* USER CODE BEGIN TIM3_Init 0 */

  /* USER CODE END TIM3_Init 0 */

  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM3_Init 1 */

  /* USER CODE END TIM3_Init 1 */
  htim3.Instance = TIM3;
  htim3.Init.Prescaler = 2000-1;
  htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim3.Init.Period = 160-1;
  htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_PWM_Init(&htim3) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim3, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.Pulse = 100;
  if (HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM3_Init 2 */

  /* USER CODE END TIM3_Init 2 */
  HAL_TIM_MspPostInit(&htim3);

}

/**
  * @brief TIM4 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM4_Init(void)
{

  /* USER CODE BEGIN TIM4_Init 0 */

  /* USER CODE END TIM4_Init 0 */

  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM4_Init 1 */

  /* USER CODE END TIM4_Init 1 */
  htim4.Instance = TIM4;
  htim4.Init.Prescaler = 2000-1;
  htim4.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim4.Init.Period = 160-1;
  htim4.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim4.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_PWM_Init(&htim4) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim4, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim4, &sConfigOC, TIM_CHANNEL_3) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM4_Init 2 */

  /* USER CODE END TIM4_Init 2 */
  HAL_TIM_MspPostInit(&htim4);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */
void ImprovePwm(TIM_HandleTypeDef *htim,uint32_t chanel,uint16_t pulse_value)
{
	TIM_OC_InitTypeDef sConfigOC = {0};
	
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = pulse_value;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(htim, &sConfigOC, chanel) != HAL_OK)
  {
    Error_Handler();
  }

}






void tim4chanel3cfg(void)
{
	TIM_ClockConfigTypeDef sClockSourceConfig = {0};
	TIM_MasterConfigTypeDef sMasterConfig = {0};
	TIM_OC_InitTypeDef sConfigOC = {0};


	htim4.Instance = TIM4;
	htim4.Init.Prescaler = 2000;
	htim4.Init.CounterMode = TIM_COUNTERMODE_UP;
	htim4.Init.Period = 160-1;
	htim4.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
	htim4.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;


	/* Allocate lock resource and initialize it */
	htim4.Lock = HAL_UNLOCKED;


	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	RCC->APB1ENR|=RCC_APB1ENR_TIM4EN;
	/* TIM4 interrupt Init */
	NVIC->ISER[(((uint32_t)TIM4_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM4_IRQn) & 0x1FUL));//使能中断


	/* Set the TIM state */
	htim4.State = HAL_TIM_STATE_BUSY;

	/* Set the Time Base configuration */
	uint32_t tmpcr1;
	tmpcr1 = htim4.Instance->CR1;

	/* Set TIM Time Base Unit parameters ---------------------------------------*/

	/* Select the Counter Mode */
	tmpcr1 &= ~(TIM_CR1_DIR | TIM_CR1_CMS);
	tmpcr1 |= TIM_COUNTERMODE_UP;

	/* Set the clock division */
	tmpcr1 &= ~TIM_CR1_CKD;
	tmpcr1 |= 2000;

	/* Set the auto-reload preload */
	tmpcr1=(tmpcr1 & (~(TIM_CR1_ARPE))) | (TIM_AUTORELOAD_PRELOAD_DISABLE);
	htim4.Instance->CR1 = tmpcr1;

	/* Set the Autoreload value */
	htim4.Instance->ARR = 160-1;

	/* Set the Prescaler value */
	htim4.Instance->PSC = 2000-1;

	/* Generate an update event to reload the Prescaler
	and the repetition counter (only for advanced timer) value immediately */
	htim4.Instance->EGR = TIM_EGR_UG;

	/* Initialize the TIM state*/
	htim4.State = HAL_TIM_STATE_READY;

	/* Allocate lock resource and initialize it */
	htim4.Lock = HAL_UNLOCKED;

	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	SET_BIT(RCC->APB1ENR, RCC_APB1ENR_TIM4EN);
	/* TIM4 interrupt Init */

	NVIC->ISER[(((uint32_t)TIM4_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM4_IRQn) & 0x1FUL));
	/* Set the TIM state */
	htim4.State = HAL_TIM_STATE_BUSY;  

	uint32_t tmpsmcr;
	htim4.State = HAL_TIM_STATE_BUSY;
	/* Check the parameters */

	/* Reset the SMS, TS, ECE, ETPS and ETRF bits */
	tmpsmcr = htim4.Instance->SMCR;
	tmpsmcr &= ~(TIM_SMCR_SMS | TIM_SMCR_TS);
	tmpsmcr &= ~(TIM_SMCR_ETF | TIM_SMCR_ETPS | TIM_SMCR_ECE | TIM_SMCR_ETP);
	htim4.Instance->SMCR = tmpsmcr;
	htim4.State = HAL_TIM_STATE_READY;

	/* Set the TIM state */
	htim4.State = HAL_TIM_STATE_BUSY;

	/* Init the base time for the PWM */
	TIM_Base_SetConfig(htim4.Instance, &htim4.Init);

	/* Initialize the TIM state*/
	htim4.State = HAL_TIM_STATE_READY;



	sConfigOC.OCMode = TIM_OCMODE_PWM1;
	sConfigOC.Pulse = 500;
	sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
	sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;

	HAL_TIM_PWM_ConfigChannel(&htim4, &sConfigOC, TIM_CHANNEL_3);

	htim4.State = HAL_TIM_STATE_BUSY;

	/* Configure the Channel 1 in PWM mode */
	uint32_t tmpccmrx;
	uint32_t tmpccer;
	uint32_t tmpcr2;

	/* Disable the Channel 1: Reset the CC1E Bit */
	htim4.Instance->CCER &= ~TIM_CCER_CC1E;

	/* Get the TIMx CCER register value */
	tmpccer = htim4.Instance->CCER;
	/* Get the TIMx CR2 register value */
	tmpcr2 =  htim4.Instance->CR2;

	/* Get the TIMx CCMR1 register value */
	tmpccmrx = htim4.Instance->CCMR1;

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
	htim4.Instance->CR2 = tmpcr2;

	/* Write to TIMx CCMR1 */
	htim4.Instance->CCMR1 = tmpccmrx;

	/* Set the Capture Compare Register value */
	htim4.Instance->CCR1 = 500;

	/* Write to TIMx CCER */
	htim4.Instance-> CCER = tmpccer;

	/* Set the Preload enable bit for channel1 */
	htim4.Instance->CCMR1 |= TIM_CCMR1_OC1PE;

	/* Configure the Output Fast mode */
	htim4.Instance->CCMR1 &= ~TIM_CCMR1_OC1FE;



	htim4.State = HAL_TIM_STATE_READY;



    __HAL_RCC_GPIOB_CLK_ENABLE();
    /**TIM4 GPIO Configuration    
    PB8     ------> TIM4_CH3 
    */
	GPIO_InitTypeDef GPIO_InitStruct;
    GPIO_InitStruct.Pin = GPIO_PIN_8;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM4;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);


}
void tim3chanel1cfg(void)
{
	TIM_ClockConfigTypeDef sClockSourceConfig = {0};
	TIM_MasterConfigTypeDef sMasterConfig = {0};
	TIM_OC_InitTypeDef sConfigOC = {0};


	htim3.Instance = TIM3;
	htim3.Init.Prescaler = 2000;
	htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
	htim3.Init.Period = 160-1;
	htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
	htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;


	/* Allocate lock resource and initialize it */
	htim3.Lock = HAL_UNLOCKED;


	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	RCC->APB1ENR|=RCC_APB1ENR_TIM3EN;
	/* TIM3 interrupt Init */
	NVIC->ISER[(((uint32_t)TIM3_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM3_IRQn) & 0x1FUL));//使能中断


	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;

	/* Set the Time Base configuration */
	uint32_t tmpcr1;
	tmpcr1 = htim3.Instance->CR1;

	/* Set TIM Time Base Unit parameters ---------------------------------------*/

	/* Select the Counter Mode */
	tmpcr1 &= ~(TIM_CR1_DIR | TIM_CR1_CMS);
	tmpcr1 |= TIM_COUNTERMODE_UP;

	/* Set the clock division */
	tmpcr1 &= ~TIM_CR1_CKD;
	tmpcr1 |= 2000;

	/* Set the auto-reload preload */
	tmpcr1=(tmpcr1 & (~(TIM_CR1_ARPE))) | (TIM_AUTORELOAD_PRELOAD_DISABLE);
	htim3.Instance->CR1 = tmpcr1;

	/* Set the Autoreload value */
	htim3.Instance->ARR = 160-1;

	/* Set the Prescaler value */
	htim3.Instance->PSC = 2000-1;

	/* Generate an update event to reload the Prescaler
	and the repetition counter (only for advanced timer) value immediately */
	htim3.Instance->EGR = TIM_EGR_UG;

	/* Initialize the TIM state*/
	htim3.State = HAL_TIM_STATE_READY;

	/* Allocate lock resource and initialize it */
	htim3.Lock = HAL_UNLOCKED;

	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	SET_BIT(RCC->APB1ENR, RCC_APB1ENR_TIM3EN);
	/* TIM3 interrupt Init */

	NVIC->ISER[(((uint32_t)TIM3_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM3_IRQn) & 0x1FUL));
	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;  

	uint32_t tmpsmcr;
	htim3.State = HAL_TIM_STATE_BUSY;
	/* Check the parameters */

	/* Reset the SMS, TS, ECE, ETPS and ETRF bits */
	tmpsmcr = htim3.Instance->SMCR;
	tmpsmcr &= ~(TIM_SMCR_SMS | TIM_SMCR_TS);
	tmpsmcr &= ~(TIM_SMCR_ETF | TIM_SMCR_ETPS | TIM_SMCR_ECE | TIM_SMCR_ETP);
	htim3.Instance->SMCR = tmpsmcr;
	htim3.State = HAL_TIM_STATE_READY;

	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;

	/* Init the base time for the PWM */
	TIM_Base_SetConfig(htim3.Instance, &htim3.Init);

	/* Initialize the TIM state*/
	htim3.State = HAL_TIM_STATE_READY;



	sConfigOC.OCMode = TIM_OCMODE_PWM1;
	sConfigOC.Pulse = 500;
	sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
	sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;

	HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_1);

	htim3.State = HAL_TIM_STATE_BUSY;

	/* Configure the Channel 1 in PWM mode */
	uint32_t tmpccmrx;
	uint32_t tmpccer;
	uint32_t tmpcr2;

	/* Disable the Channel 1: Reset the CC1E Bit */
	htim3.Instance->CCER &= ~TIM_CCER_CC1E;

	/* Get the TIMx CCER register value */
	tmpccer = htim3.Instance->CCER;
	/* Get the TIMx CR2 register value */
	tmpcr2 =  htim3.Instance->CR2;

	/* Get the TIMx CCMR1 register value */
	tmpccmrx = htim3.Instance->CCMR1;

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
	htim3.Instance->CR2 = tmpcr2;

	/* Write to TIMx CCMR1 */
	htim3.Instance->CCMR1 = tmpccmrx;

	/* Set the Capture Compare Register value */
	htim3.Instance->CCR1 = 500;

	/* Write to TIMx CCER */
	htim3.Instance-> CCER = tmpccer;

	/* Set the Preload enable bit for channel1 */
	htim3.Instance->CCMR1 |= TIM_CCMR1_OC1PE;

	/* Configure the Output Fast mode */
	htim3.Instance->CCMR1 &= ~TIM_CCMR1_OC1FE;



	htim3.State = HAL_TIM_STATE_READY;




	GPIO_InitTypeDef GPIO_InitStruct;


    __HAL_RCC_GPIOC_CLK_ENABLE();
    /**TIM3 GPIO Configuration    
    PC6     ------> TIM3_CH1
    PC7     ------> TIM3_CH2 
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6|GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);
}
void tim3chanel2cfg(void)
{

		TIM_ClockConfigTypeDef sClockSourceConfig = {0};
	TIM_MasterConfigTypeDef sMasterConfig = {0};
	TIM_OC_InitTypeDef sConfigOC = {0};


	htim3.Instance = TIM3;
	htim3.Init.Prescaler = 2000;
	htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
	htim3.Init.Period = 160-1;
	htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
	htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;


	/* Allocate lock resource and initialize it */
	htim3.Lock = HAL_UNLOCKED;


	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	RCC->APB1ENR|=RCC_APB1ENR_TIM3EN;
	/* TIM3 interrupt Init */
	NVIC->ISER[(((uint32_t)TIM3_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM3_IRQn) & 0x1FUL));//使能中断


	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;

	/* Set the Time Base configuration */
	uint32_t tmpcr1;
	tmpcr1 = htim3.Instance->CR1;

	/* Set TIM Time Base Unit parameters ---------------------------------------*/

	/* Select the Counter Mode */
	tmpcr1 &= ~(TIM_CR1_DIR | TIM_CR1_CMS);
	tmpcr1 |= TIM_COUNTERMODE_UP;

	/* Set the clock division */
	tmpcr1 &= ~TIM_CR1_CKD;
	tmpcr1 |= 2000;

	/* Set the auto-reload preload */
	tmpcr1=(tmpcr1 & (~(TIM_CR1_ARPE))) | (TIM_AUTORELOAD_PRELOAD_DISABLE);
	htim3.Instance->CR1 = tmpcr1;

	/* Set the Autoreload value */
	htim3.Instance->ARR = 160-1;

	/* Set the Prescaler value */
	htim3.Instance->PSC = 2000-1;

	/* Generate an update event to reload the Prescaler
	and the repetition counter (only for advanced timer) value immediately */
	htim3.Instance->EGR = TIM_EGR_UG;

	/* Initialize the TIM state*/
	htim3.State = HAL_TIM_STATE_READY;

	/* Allocate lock resource and initialize it */
	htim3.Lock = HAL_UNLOCKED;

	/* Init the low level hardware : GPIO, CLOCK, NVIC */
	SET_BIT(RCC->APB1ENR, RCC_APB1ENR_TIM3EN);
	/* TIM3 interrupt Init */

	NVIC->ISER[(((uint32_t)TIM3_IRQn) >> 5UL)] = (uint32_t)(1UL << (((uint32_t)TIM3_IRQn) & 0x1FUL));
	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;  

	uint32_t tmpsmcr;
	htim3.State = HAL_TIM_STATE_BUSY;
	/* Check the parameters */

	/* Reset the SMS, TS, ECE, ETPS and ETRF bits */
	tmpsmcr = htim3.Instance->SMCR;
	tmpsmcr &= ~(TIM_SMCR_SMS | TIM_SMCR_TS);
	tmpsmcr &= ~(TIM_SMCR_ETF | TIM_SMCR_ETPS | TIM_SMCR_ECE | TIM_SMCR_ETP);
	htim3.Instance->SMCR = tmpsmcr;
	htim3.State = HAL_TIM_STATE_READY;

	/* Set the TIM state */
	htim3.State = HAL_TIM_STATE_BUSY;

	/* Init the base time for the PWM */
	TIM_Base_SetConfig(htim3.Instance, &htim3.Init);

	/* Initialize the TIM state*/
	htim3.State = HAL_TIM_STATE_READY;



	sConfigOC.OCMode = TIM_OCMODE_PWM1;
	sConfigOC.Pulse = 500;
	sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
	sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;

	HAL_TIM_PWM_ConfigChannel(&htim3, &sConfigOC, TIM_CHANNEL_2);

	htim3.State = HAL_TIM_STATE_BUSY;

	/* Configure the Channel 1 in PWM mode */
	uint32_t tmpccmrx;
	uint32_t tmpccer;
	uint32_t tmpcr2;

	/* Disable the Channel 1: Reset the CC1E Bit */
	htim3.Instance->CCER &= ~TIM_CCER_CC1E;

	/* Get the TIMx CCER register value */
	tmpccer = htim3.Instance->CCER;
	/* Get the TIMx CR2 register value */
	tmpcr2 =  htim3.Instance->CR2;

	/* Get the TIMx CCMR1 register value */
	tmpccmrx = htim3.Instance->CCMR1;

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
	htim3.Instance->CR2 = tmpcr2;

	/* Write to TIMx CCMR1 */
	htim3.Instance->CCMR1 = tmpccmrx;

	/* Set the Capture Compare Register value */
	htim3.Instance->CCR1 = 500;

	/* Write to TIMx CCER */
	htim3.Instance-> CCER = tmpccer;

	/* Set the Preload enable bit for channel1 */
	htim3.Instance->CCMR1 |= TIM_CCMR1_OC1PE;

	/* Configure the Output Fast mode */
	htim3.Instance->CCMR1 &= ~TIM_CCMR1_OC1FE;



	htim3.State = HAL_TIM_STATE_READY;




	GPIO_InitTypeDef GPIO_InitStruct;


    __HAL_RCC_GPIOC_CLK_ENABLE();
    /**TIM3 GPIO Configuration    
    PC6     ------> TIM3_CH1
    PC7     ------> TIM3_CH2 
    */
    GPIO_InitStruct.Pin = GPIO_PIN_6|GPIO_PIN_7;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);
	

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
