#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdlib.h> //lib para gerar valores rand()
#include<time.h>
#include <unistd.h>


//Declaração das funções que serão executads pelas threads
void* ts1_function(void *arg);
void* ts2_function(void *arg);
void* ta_function(void *arg);

//Declaração mutex e threads
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;
pthread_t ts1, ts2, ta;

//Variáveis globais
int count_ts1, count_ts2, count_ta = 0;
float vs1[5], vs2[5];
time_t t;

//Função main
int main()
{
    //Criação das threads
    pthread_create( &ts1, NULL, &ts1_function, NULL);
    pthread_create( &ts2, NULL, &ts2_function, NULL);
    pthread_create( &ta, NULL, &ta_function, NULL);

    // Espera que as threads completem suas ações antes de continuar o main
    pthread_join( ts1, NULL);
    pthread_join( ts2, NULL);
    pthread_join( ta, NULL);

}

void* ts1_function(void *arg)
{
    /* Bloqueia a mutex para garantir 
	acesso exclusivo a variavel count. 
	Se a mutex já estiver bloqueada, a thread
	vai ficar bloqueda também.
	*/
    srand((unsigned) time(&t));
    pthread_mutex_lock(&mutex1);
    for(count_ts1 = 0; count_ts1 < 5; count_ts1 ++)
    {
      vs1[count_ts1] = (-8 + rand()%50)/(1.98+count_ts1);
      printf("VS1[%d] = %.2f\n", count_ts1, vs1[count_ts1]);
    }
	//Desbloqueia a mutex.
	pthread_mutex_unlock(&mutex1);
}

void* ts2_function(void *arg)
{
    /*sleep para mudar o horário da máquina e
    gerar novo seed para a srand()*/
    sleep(3);
    srand((unsigned) time(&t));
    pthread_mutex_lock(&mutex2);
    for(count_ts2 = 0; count_ts2 < 5; count_ts2 ++)
    {
      vs2[count_ts2] = (-8 + rand()%50)/(1.98+count_ts2);
      printf("VS2[%d] = %.2f\n", count_ts2, vs2[count_ts2]);
    }
	pthread_mutex_unlock(&mutex2);
}

void* ta_function(void *arg){
    
}
	
