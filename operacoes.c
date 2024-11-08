#include <stdio.h>
#include <sys/sysinfo.h>


double bytes_para_gb(long long bytes) {
    return (double)bytes / (1024 * 1024 * 1024);  
}

/
double segundos_para_hora(long long seconds) {
    return (double)seconds / 3600;  
}

int main() {
    struct sysinfo sys_info;

    
    if (sysinfo(&sys_info) != 0) {
        perror("Erro ao obter informações do sistema");
        return 1;
    }

    
    printf("Tempo de atividade (horas): %ld\n", segundos_para_hora(sys_info.uptime));
    printf("Memória total (GB): %ld\n", bytes_para_gb(sys_info.totalram));
    printf("Memória livre (GB): %ld\n", bytes_para_gb(sys_info.freeram));
    printf("Memória compartilhada (GB): %ld\n", bytes_para_gb(sys_info.sharedram));
    printf("Memória em buffer (GB): %ld\n", bytes_para_gb(sys_info.bufferram));
    printf("Quantidade total de swap (GB): %ld\n", bytes_para_gb(sys_info.totalswap));
    printf("Swap livre (GB): %ld\n", bytes_para_gb(sys_info.freeswap));
    printf("Número de processos em execução: %d\n", sys_info.procs);

    return 0;
}
