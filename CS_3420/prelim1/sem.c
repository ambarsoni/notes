
typedef struct{
    lock_t lock;
    int count;
}sem_t;

//Initilialze semaphor with count as the limit on the resource
void inti(sem_t *s, int c){
    lock(s->lock);
    s->count = c;
    unlock(s->lock);
}

//Write: Adds 1 to the count
void v(sem_t *s){
    lock(s->lock);
    s->count++;
    unlock(s->lock);
}

//Read: Waits until atleast 1 resource, and then decrements count
void p(sem_t *s){
    lock(s->lock);
    while(s->count < 1){
        unlock(s->lock);
        while(!s->count);
        lock(s->lock);
    }
    s->count--;
    unlock(s->lock);
}



void v(sem_t *s){
    lock(s->lock);
    s->count++;
    if(waiting(s->lock,s->count > 0)){
        signal(s->lock,buff);
    }
    unlock(s->lock);
}

void p(sem_t *s){
    lock(s->lock);
    if(!s->count){
        wait(s->lock, s->count > 0);
    }
    s->count--;
    unlock(s->lock);
}

