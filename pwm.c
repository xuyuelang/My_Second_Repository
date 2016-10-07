#include"pwm.h"


void  TIM14_PWM_Init(u32 arr,u32 psc){
	
	GPIO_InitTypeDef GPIO_InitStructure;
	TIM_TimeBaseInitTypeDef TIM_TimeBaseInitStructure;
	TIM_OCInitTypeDef TIM_OCInitStructure;
/********************************************************/	
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM14,ENABLE);
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOF,ENABLE);
	//GPIO ��ʼ�����
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_UP;
	GPIO_InitStructure.GPIO_Speed=GPIO_Speed_100MHz;
	GPIO_Init(GPIOF,&GPIO_InitStructure);
/*****************************************************/
	GPIO_PinAFConfig(GPIOF,GPIO_PinSource9,GPIO_AF_TIM14);
/*********************��ʼ����ʱ��************************/
	TIM_TimeBaseInitStructure.TIM_ClockDivision=TIM_CKD_DIV1;
	TIM_TimeBaseInitStructure.TIM_CounterMode=TIM_CounterMode_Up;
	TIM_TimeBaseInitStructure.TIM_Period=arr;//�Զ�����װ��ֵ
	TIM_TimeBaseInitStructure.TIM_Prescaler=psc;

	TIM_TimeBaseInit(TIM3,&TIM_TimeBaseInitStructure);
	TIM_ITConfig(TIM3,TIM_IT_Update,ENABLE);
/**********************************************************/
	TIM_OCInitStructure.TIM_OCMode=TIM_OCMode_PWM1;
	TIM_OCInitStructure.TIM_OutputState=ENABLE;
	TIM_OCInitStructure.TIM_OCPolarity=TIM_OCPolarity_Low;
	TIM_OC1Init(TIM14,&TIM_OCInitStructure);
/***********ͨ��1********************************************/
	TIM_OC1PreloadConfig(TIM14,TIM_OCPreload_Enable);//ʹ��ͨ��1�ϵ�Ԥװ�ض�ʱ��
	TIM_ARRPreloadConfig(TIM14,ENABLE);//ʹ��ARR�Ĵ���Ԥװ��
	
	TIM_Cmd(TIM14,ENABLE);//ʹ�ܶ�ʱ��

}
