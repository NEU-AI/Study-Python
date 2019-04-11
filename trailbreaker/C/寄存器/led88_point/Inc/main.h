/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
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

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define LED_X1_Pin GPIO_PIN_0
#define LED_X1_GPIO_Port GPIOA
#define LED_X2_Pin GPIO_PIN_1
#define LED_X2_GPIO_Port GPIOA
#define LED_X3_Pin GPIO_PIN_2
#define LED_X3_GPIO_Port GPIOA
#define LED_X4_Pin GPIO_PIN_3
#define LED_X4_GPIO_Port GPIOA
#define LED_X5_Pin GPIO_PIN_4
#define LED_X5_GPIO_Port GPIOA
#define LED_X6_Pin GPIO_PIN_5
#define LED_X6_GPIO_Port GPIOA
#define LED_X7_Pin GPIO_PIN_6
#define LED_X7_GPIO_Port GPIOA
#define LED_X8_Pin GPIO_PIN_7
#define LED_X8_GPIO_Port GPIOA
#define SW_S3_Pin GPIO_PIN_10
#define SW_S3_GPIO_Port GPIOB
#define SW_S4_Pin GPIO_PIN_11
#define SW_S4_GPIO_Port GPIOB
#define LED_Y5_Pin GPIO_PIN_12
#define LED_Y5_GPIO_Port GPIOB
#define LED_Y6_Pin GPIO_PIN_13
#define LED_Y6_GPIO_Port GPIOB
#define LED_Y7_Pin GPIO_PIN_14
#define LED_Y7_GPIO_Port GPIOB
#define LED_Y8_Pin GPIO_PIN_15
#define LED_Y8_GPIO_Port GPIOB
#define LED_Y1_Pin GPIO_PIN_6
#define LED_Y1_GPIO_Port GPIOC
#define LED_Y2_Pin GPIO_PIN_7
#define LED_Y2_GPIO_Port GPIOC
#define SW_S1_Pin GPIO_PIN_6
#define SW_S1_GPIO_Port GPIOB
#define SW_S2_Pin GPIO_PIN_7
#define SW_S2_GPIO_Port GPIOB
#define LED_Y3_Pin GPIO_PIN_8
#define LED_Y3_GPIO_Port GPIOB
#define LED_Y4_Pin GPIO_PIN_9
#define LED_Y4_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
