#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define select_ratio 0.5f
#define population_size 12
#define mutation_ratio 0.05f
#define max_w 10
#define max_unchanged 40

typedef struct {
    int w;  // 금괴의 무게
    int v;  // 금괴의 값어치
} Gold;

typedef struct {
    int sum;    // 선택한 금괴의 무게 합계
    int val;    // 선택한 금괴의 값어치 총합
    int* code;  // 금괴 선택 여부를 나타내는 이진 코드 (0 : 선택하지 않음 / 1 : 선택함)
} Chromosome;   

// 금괴의 무게와 가치를 포함하여 금괴를 생성
void makeGold(Gold** golds) {
    *golds = (Gold*)malloc(6 * sizeof(Gold));
    (*golds)[0].w = 4;
    (*golds)[0].v = 6;
    // 나머지 금괴의 무게와 가치를 초기화해야 함
}

// 초기 염색체(population)를 생성하는 함수
// 각 금괴에 대해 무작위 확률을 사용하여 선택 여부를 결정하며, 선택된 금괴의 무게 및 가치의 합계 계산
void makeChromosomes(Gold* golds, Chromosome* population) {
    int cnt = 0;
    while (cnt < population_size) {
        Chromosome c;
        c.sum = 0;
        c.val = 0;
        c.code = (int*)malloc(6 * sizeof(int));
        for (int i = 0; i < 6; i++) {
            double rand_v = (double)rand() / RAND_MAX;
            if (rand_v > 0.5) {
                c.code[i] = 1;  // 금괴 선택
                c.sum += golds[i].w;
                c.val += golds[i].v;
            } else {
                c.code[i] = 0;  // 금괴 미선택
            }
        }
        if (c.sum <= max_w) {
            population[cnt++] = c;  // 염색체를 염색체 집단(population)에 추가
        } else {
            free(c.code);  // 무게가 최대값을 초과하는 경우 염색체를 버림
        }
    }
}


// 염색체의 값어치를 기준으로 내림차순으로 정렬하기 위한 비교 함수
int compare(const void* a, const void* b) {
    Chromosome* ch1 = (Chromosome*)a;
    Chromosome* ch2 = (Chromosome*)b;
    return ch2->val - ch1->val;
}


// 염색체의 적합도를 평가하고 지금까지 찾은 최적해를 업데이트하는 함수
void test(Chromosome* population, int* best_unchange_cnt, Chromosome* best_chr) {
    qsort(population, population_size, sizeof(Chromosome), compare);    //population 배열을 내림차순으로 정렬하기 위해 qsort 라이브러리 함수 사용
    if (best_chr->val < population[0].val) {
        *best_chr = population[0];  // 최적해를 업데이트
        *best_unchange_cnt = 0;
    } else {
        (*best_unchange_cnt)++;
    }
    // best_chr: 현재까지 찾은 최적해
    // best_unchange_cnt: 최적해가 변경되지 않은 세대 수
}

// 가장 적합한 개체들을 선택하고 나머지 개체를 염색체 집단에서 제거하여 선택된 개체들만 남게하는 함수
void select(Chromosome* population) {
    for (int i = (int)(population_size * select_ratio); i < population_size; i++) {
        free(population[i].code);  // 선택되지 않은 염색체의 메모리 해제
        population[i].code = NULL;
    }
}

// 선택된 염색체들 간에 교배를 수행하는 함수
// 유전 알고리즘 연산 방법 1 교배
void crossover(Chromosome* population) {
    for (int i = (int)(population_size * select_ratio); i < population_size; i++) {
        int p1 = rand() % (int)(population_size * select_ratio);    //무작위로 선택된 인덱스 p1
        int p2 = rand() % (int)(population_size * select_ratio);    
        //population 배열에서 select_ratio 비율에 따라 무작위로 선택된 두 번째 부모 염색체의 인덱스를 결정
        while (p1 == p2) {
            p2 = rand() % (int)(population_size * select_ratio);
        }
        Chromosome* parent1 = &population[p1];
        Chromosome* parent2 = &population[p2];
        Chromosome* child = &population[i];
        child->sum = 0;
        child->val = 0;
        child->code = (int*)malloc(6 * sizeof(int));
        for (int j = 0; j < 6; j++) {
            if (j < 2) {
                child->code[j] = parent1->code[j];
            } else {
                child->code[j] = parent2->code[j];
            }
            child->sum += child->code[j] * parent1->code[j];
            child->val += child->code[j] * parent2->code[j];
        }
    }
    // 선택된 부모로부터 교배하여 새로운 자식 염색체를 생성
}

// 염색체 집단에 무작위 돌연변이를 도입하는 함수
// 유전 알고리즘 연산 방법 2 돌연변이 
void mutation(Chromosome* population) {
    for (int i = 0; i < population_size; i++) {
        double rand_v = (double)rand() / RAND_MAX;
        if (rand_v < mutation_ratio) {
            int idx = rand() % 6;
            population[i].code[idx] = (population[i].code[idx] == 1) ? 0 : 1;
        }
    }
    // 염색체에 무작위 돌연변이를 도입
}

// 염색체 집단이 사용한 메모리를 해제하는 함수
void cleanup(Chromosome* population) {
    for (int i = 0; i < population_size; i++) {
        free(population[i].code);
    }
}

int main() {
    srand((unsigned int)time(NULL));  // 난수 시드 초기화

   Gold* golds;
    makeGold(&golds);  // 금괴 생성

    Chromosome* population = (Chromosome*)malloc(population_size * sizeof(Chromosome));
    makeChromosomes(golds, population);  // 초기 염색체 생성

    int t = 0;  // 세대 카운터
    int best_unchange_cnt = 0;  // 최적해가 변경되지 않은 세대 수 카운터
    Chromosome best_chr = population[0];  // 최적해를 첫 번째 염색체로 초기화

    while (best_unchange_cnt <= max_unchanged) {
        t++;  // 세대 카운터 증가
        test(population, &best_unchange_cnt, &best_chr);  // 적합도 평가 및 최적해 업데이트
        select(population);  // 가장 적합한 개체 선택
        crossover(population);  // 선택된 부모들 간에 교배 수행
        mutation(population);  // 염색체 집단에 무작위 돌연변이 도입
    }

    printf("best sum : %d best value : %d\n", best_chr.sum, best_chr.val);  // 최적해 출력

    cleanup(population);  // 메모리 정리
    free(population);
    free(golds);

    return 0;
}
