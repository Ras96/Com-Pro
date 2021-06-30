#if 1
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

char flag[1000];
void PrintFlag()
{
    //本当はこれはC言語としてダメなんですけど動くので許して
    //（問題の本質とは関係ないです）
    fprintf(stderr, "segmentation fault!\n%s\n", flag);
    fflush(stderr);
    exit(1);
}

void ReadFlag()
{
    FILE *f = fopen("flag.txt","r");
    if(f == NULL){
        puts("internal server error(flag file missing). please concact contest's admin.");
        exit(-1);
    }
    fgets(flag, sizeof(flag), f);
    fclose(f);
}
int main()
{
	// Set the gid to the effective gid
	// this prevents /bin/sh from dropping the privileges
	gid_t gid = getegid();
	setresgid(gid, gid, gid);

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    char name[50];
    ReadFlag();
    if (signal(SIGSEGV, PrintFlag) == SIG_ERR){
        puts("internal server error(signal() == SIG_ERR). please concact contest's admin.");
        return -1;
    }

    puts("please input your name...");
    gets(name);
    printf("Hello %s!\n", name);
}
#endif